# Generated by Django 3.1.7 on 2021-05-05 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_auto_20210505_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='card',
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcard.collection'),
        ),
    ]
