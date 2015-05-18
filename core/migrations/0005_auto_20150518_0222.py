# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alcohol',
            field=models.TextField(blank=True, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='bathrooms',
            field=models.TextField(blank=True, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='coffee',
            field=models.TextField(blank=True, null=True, choices=[(b'None', b'None'), (b'Truck Stop', b'Truck Stop'), (b'Good', b'Good'), (b'Really Good', b'Really Good'), (b'Great', b'Great')]),
        ),
        migrations.AddField(
            model_name='location',
            name='food',
            field=models.TextField(blank=True, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor',
            field=models.TextField(blank=True, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outlets',
            field=models.TextField(blank=True, null=True, choices=[(b'None', b'None'), (b'Minmal', b'Minmal'), (b'Some', b'Some'), (b'Ample', b'Ample')]),
        ),
        migrations.AddField(
            model_name='location',
            name='seating',
            field=models.TextField(blank=True, null=True, choices=[(b'None', b'None'), (b'Minmal', b'Minmal'), (b'Some', b'Some'), (b'Ample', b'Ample')]),
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.TextField(blank=True, null=True, choices=[(b'None', b'None'), (b'Spotty', b'Spotty'), (b'Strong', b'Strong')]),
        ),
    ]
