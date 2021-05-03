from django.db import models

class Collection(models.Model):
    collection_name = models.CharField(max_length=70)
    cards = models.IntegerField(default=0)
