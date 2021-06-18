
# Register your models here.
from django.contrib import admin
from .models import doc_information, doc_embedding

class docInformationAdmin(admin.ModelAdmin): 
  list_display = ('doc_id', 'document_name', 'filepath', 'preview') 

class docEmbeddingAdmin(admin.ModelAdmin):
  list_display = ('doc_id', 'embeddings')

# Register your models here.
admin.site.register(doc_information, docInformationAdmin)
admin.site.register(doc_embedding, docEmbeddingAdmin)




