from django.db import models

class Collection(models.Model):
    collection_name = models.CharField(max_length=70)
    card = models.IntegerField(default=0)


class Flashcard(models.Model):
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    card_word = models.CharField(max_length=50)
    card_definition = models.CharField(max_length=100)
