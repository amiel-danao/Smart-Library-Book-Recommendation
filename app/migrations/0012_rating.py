# Generated by Django 4.2.9 on 2024-02-14 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_book_image_alter_book_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=300)),
                ('rating', models.PositiveIntegerField(default=0, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.book')),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
    ]
