# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('inner', models.BooleanField(default=True, help_text='Defines whether the plugin is already inside a grid container or another Multi-column plugin.', verbose_name='inner')),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridColumn',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size', models.CharField(default=b'1', max_length=50, verbose_name='size', choices=[(b'1', b'grid-1'), (b'2', b'grid-2'), (b'3', b'grid-3'), (b'4', b'grid-4'), (b'5', b'grid-5'), (b'6', b'grid-6'), (b'7', b'grid-7'), (b'8', b'grid-8'), (b'9', b'grid-9'), (b'10', b'grid-10'), (b'11', b'grid-11'), (b'12', b'grid-12'), (b'13', b'grid-13'), (b'14', b'grid-14'), (b'15', b'grid-15'), (b'16', b'grid-16'), (b'17', b'grid-17'), (b'18', b'grid-18'), (b'19', b'grid-19'), (b'20', b'grid-20'), (b'21', b'grid-21'), (b'22', b'grid-22'), (b'23', b'grid-23'), (b'24', b'grid-24')])),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
