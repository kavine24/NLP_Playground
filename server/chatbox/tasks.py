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

import ollama

from .models import Documents, ContextDocs

from celery import shared_task

@shared_task
def embed_document(document_id):
    print('here' + str(document_id), file=sys.stderr)
    print(os.getcwd())
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

@shared_task
def generate_reponse(query):
    pass
    # embedder = OllamaEmbeddings(
    #     model="llama3"
    # )

    # query = 'What are the recent advancements in computer vision'

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


    # llm_response = ollama.generate(
    #     model='llama3',
    #     prompt=formmatted_prompt
    # )

    # print(llm_response['response'])