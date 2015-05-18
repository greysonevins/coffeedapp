# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150518_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='alcohol',
            field=models.TextField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='bathrooms',
            field=models.TextField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='coffee',
            field=models.TextField(blank=True, null=True, choices=[(0, b'None'), (1, b'Truck Stop'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='food',
            field=models.TextField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='outdoor',
            field=models.TextField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='outlets',
            field=models.TextField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='seating',
            field=models.TextField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='wifi',
            field=models.TextField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
    ]
