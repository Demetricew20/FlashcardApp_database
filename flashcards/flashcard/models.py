from django.db import models

class Flashcard(models.Model):
    collection_id = models.ForeignKey('flashcards.collection', on_delete=models.CASCADE)
    card_word = models.CharField(max_length=50)
    card_definition = models.CharField(max_length=100)