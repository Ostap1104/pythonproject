# Generated by Django 5.0.6 on 2024-05-30 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_article_category_alter_article_main_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
    ]
