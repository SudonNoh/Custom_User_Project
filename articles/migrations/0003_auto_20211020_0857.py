# Generated by Django 3.2.8 on 2021-10-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='articles.Tag'),
        ),
    ]
