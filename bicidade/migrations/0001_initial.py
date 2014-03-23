# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Way'
        db.create_table(u'bicidade_way', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'bicidade', ['Way'])


    def backwards(self, orm):
        # Deleting model 'Way'
        db.delete_table(u'bicidade_way')


    models = {
        u'bicidade.way': {
            'Meta': {'object_name': 'Way'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bicidade']