from django.shortcuts import render,  HttpResponse

# Create your views here.
def chat(request):
    return HttpResponse("Hello chat")

def doc_viewer(request):
    return HttpResponse("Hello doc viewer")

def doc_upload(request):
    return HttpResponse("Hello doc viewer")