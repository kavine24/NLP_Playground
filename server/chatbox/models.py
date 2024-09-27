from django.db import models
from pgvector.django import VectorField

# Create your models here.
class Documents(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    doc_name = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)
    size = models.IntegerField(default=0)
    embedding_status = models.BooleanField(default=False)

class ContextDocs(models.Model):
    cd_id = models.BigAutoField(primary_key=True)
    doc_id = models.ForeignKey(Documents, on_delete=models.CASCADE)
    doc_context = models.CharField(max_length=500)
    embedded_vector = VectorField(dimensions=4096) # 4096 is the size of ollama llama3 embed vector from langchain.