from django.contrib import admin
from .models import Collection, Flashcard


admin.site.register(Collection, Flashcard)
