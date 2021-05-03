from django.db import models

class Collection(models.Model):
    collection_name = models.CharField(max_length=70)
    card = models.IntegerField(default=0)


class Flashcard(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='collection id')
    card_word = models.CharField(max_length=50)
    card_definition = models.CharField(max_length=100)
