# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_auto_20160116_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='is_rotation',
            new_name='repeat',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='creation_date',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='remind_before',
        ),
        migrations.AddField(
            model_name='tasks',
            name='set_reminder_before',
            field=models.DecimalField(default=Decimal('0.0000'), max_digits=20, decimal_places=4),
        ),
    ]
