from django.db import models

# Create your models here.
class Documents(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    doc_name = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)
    size = models.IntegerField(default=0)

class ContextDocs(models.Model):
    cd_id = models.BigAutoField(primary_key=True)
    doc_id = models.BigIntegerField()