from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('docs/view', views.doc_viewer, name='doc viewer'),
    path('docs/upload', views.doc_upload, name='doc uploader'),
]