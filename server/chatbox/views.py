from django.shortcuts import render,  HttpResponse, redirect
from django.core.files.storage import FileSystemStorage

from .models import Documents
from .tasks import embed_document, generate_reponse

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
    if request.method == "POST":
        # if the post request has a file under the input name 'document', then save the file.
        request_file = request.FILES['file-upload'] if 'file-upload' in request.FILES else None
        if request_file:
            fs = FileSystemStorage()

            if not fs.exists(request_file.name):

                file_name = fs.save(request_file.name, request_file)

                doc = Documents(doc_name=file_name, size=fs.size(file_name) / 1000000)
                doc.save()

                # Start scheduled celery task to embed document in background.
                embed_document.delay(doc.doc_id)

    return redirect('/docs')