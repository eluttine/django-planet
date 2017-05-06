# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0002_auto_20151219_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='thumbnails', blank=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='thumbnail_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='thumbnails', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
