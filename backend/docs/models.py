from django.db import models

# Create your models here.
class doc_information(models.Model):
  doc_id = models.AutoField(primary_key = True)
  document_name = models.TextField()
  filepath = models.TextField()
  preview = models.TextField(default="")

  def _str_(self):
    return self.document_name

class doc_embedding(models.Model):
  doc_id = models.ForeignKey(doc_information, on_delete=models.CASCADE)
  embeddings = models.BinaryField()

 