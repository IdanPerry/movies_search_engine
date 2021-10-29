# Generated by Django 3.2.8 on 2021-10-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_moviedata_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterUniqueTogether(
            name='moviedata',
            unique_together={('title', 'year')},
        ),
    ]