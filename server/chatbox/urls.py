from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('chat/generate_response', views.generate_llm_response, name='response generator'),
    path('docs', views.doc_list, name='doc list'),
    path('docs/view', views.doc_viewer, name='doc viewer'),
    path('docs/upload', views.doc_upload_portal, name='doc upload portal'),
    path('docs/uploader', views.doc_uploader, name='doc uploader'),
]