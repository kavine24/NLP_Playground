"""
Celery task file for generating things from the model. Model typically takes a while to return results so we make these background tasks.
"""
import time
import sys
import os
import numpy as np

from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama

from .models import Documents, ContextDocs

from celery import shared_task

OLLAMA_URL = 'http://localhost:11434'
@shared_task
def embed_document(document_id):
    # get document
    doc = Documents.objects.get(doc_id=document_id)

    # open document reader
    file_name = f'media/{doc.doc_name}'
    reader = PdfReader(file_name)

    # init splitter and embedder model
    splitter = RecursiveCharacterTextSplitter(['. ', ','],
                                            keep_separator=True,
                                            chunk_size=500,
                                            chunk_overlap=50)

    embedder = OllamaEmbeddings(
        base_url=OLLAMA_URL,
        model="llama3"
    )

    
    # loop thru document 
    for page in reader.pages:
        text = page.extract_text()

        print('here2', file=sys.stderr)
        # make text splits and embeddings
        contexts = splitter.split_text(text=text)
        embeddings = embedder.embed_documents(contexts)

        print('here3', file=sys.stderr)
        # save to db
        for i in range(len(contexts)):
            context_doc = ContextDocs(doc_id=document_id, doc_context = contexts[i], embedded_vector=embeddings[i])
            context_doc.save()

    # update original document row to show status
    doc.embedding_status = True
    doc.save()

def generate_reponse(query):
    # embedder = OllamaEmbeddings(
    #     base_url=OLLAMA_URL,
    #     model="llama3"
    # )

    # query_embedding = np.array(embedder.embed_query(query))


    # context = ''
    # for doc in docs:
    #     context += doc + '\n'


    # template = \
    # """
    # Use the following pieces of context to answer the question at the end.
    # If you don't know the answer, just say that you don't know, don't try to make up an answer.
    # Use three sentences maximum and keep the answer as concise as possible.

    # {context}

    # Question: {question}

    # Helpful Answer:
    # """


    # prompt_template = PromptTemplate.from_template(template)

    # formmatted_prompt = prompt_template.format(context=context, question=query)

    # print(formmatted_prompt)

    llm_chat = Ollama(
        base_url=OLLAMA_URL,
        model="llama3"
    )

    llm_response = llm_chat.invoke(
        input=query
    )

    return llm_response['response']