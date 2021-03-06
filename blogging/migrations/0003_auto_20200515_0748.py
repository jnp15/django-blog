# Generated by Django 2.1.15 on 2020-05-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
