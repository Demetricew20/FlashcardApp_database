# Generated by Django 3.1.7 on 2021-05-03 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_auto_20210503_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashcard',
            old_name='collection_id',
            new_name='collection',
        ),
    ]
