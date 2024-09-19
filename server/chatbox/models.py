from django.db import models

# Create your models here.
class Documents(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    doc_name = models.CharField(max_length=100)


class ContextDocs(models.Model):
    cd_id = models.BigAutoField(primary_key=True)
    doc_id = models.CharField(max_length=30)