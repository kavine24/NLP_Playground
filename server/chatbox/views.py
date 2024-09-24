from django.shortcuts import render,  HttpResponse, redirect
from chatbox.models import Documents
import ollama

import sys

# Create your views here.
def chat(request):
    return render(request, 'chatbox.html')

def doc_list(request):
    docs_list = Documents.objects.all()

    return render(request, 'doc_list.html', {'docs_list': docs_list})

def doc_viewer(request):
    return render(request, 'doc_viewer.html')

def doc_upload_portal(request):
    return render(request, 'doc_upload.html')

def doc_uploader(request):
    redirect('doc_list')