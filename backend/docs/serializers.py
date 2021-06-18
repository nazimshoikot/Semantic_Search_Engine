# docs/serializers.py

from rest_framework import serializers
from .models import doc_information, doc_embedding

class docsInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = doc_information
    fields = ('id', 'doc_id', 'document_name', 'filepath', 'preview')


class docsEmbeddingsSerializer(serializers.ModelSerializer):

  class Meta:
    model = doc_embedding
    fields = ('id', 'doc_id', 'embeddings')