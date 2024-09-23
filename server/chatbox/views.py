from django.shortcuts import render,  HttpResponse
from chatbox.models import Documents
import ollama

import sys

# Create your views here.
def chat(request):
    return HttpResponse("Hello chat")

def doc_viewer(request):
    response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ])

    return HttpResponse(response['message']['content'])
    docs = Documents.objects.all()

    return render(request, 'doc_viewer.html')

def doc_upload(request):
    return HttpResponse("Hello doc viewer")