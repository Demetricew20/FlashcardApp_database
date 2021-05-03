from .models import Flashcard
from .models import Collection
from rest_framework import serializers


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = [
            'id','collection_id', 'card_word', 'card_definition',
        ]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'id', 'collection_name', 'card',
        ]