# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'polls_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'polls', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'polls_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('notes', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'polls', ['Choice'])

        # Adding model 'Country'
        db.create_table(u'polls_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state_number', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('city_number', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'polls', ['Country'])

        # Adding model 'House'
        db.create_table(u'polls_house', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('person_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'polls', ['House'])

        # Adding model 'Family'
        db.create_table(u'polls_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'polls', ['Family'])

        # Adding model 'Person'
        db.create_table(u'polls_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Country'])),
        ))
        db.send_create_signal(u'polls', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'polls_poll')

        # Deleting model 'Choice'
        db.delete_table(u'polls_choice')

        # Deleting model 'Country'
        db.delete_table(u'polls_country')

        # Deleting model 'House'
        db.delete_table(u'polls_house')

        # Deleting model 'Family'
        db.delete_table(u'polls_family')

        # Deleting model 'Person'
        db.delete_table(u'polls_person')


    models = {
        u'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.country': {
            'Meta': {'object_name': 'Country'},
            'city_number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_number': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'polls.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.house': {
            'Meta': {'object_name': 'House'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.person': {
            'Meta': {'object_name': 'Person'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['polls']