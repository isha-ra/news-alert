# Generated by Django 3.1.2 on 2020-10-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
