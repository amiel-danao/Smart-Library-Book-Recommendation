# Generated by Django 4.2.9 on 2024-02-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_book_author_alter_book_course_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='total_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='course',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='popularity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
