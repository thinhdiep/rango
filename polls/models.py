from django.db import models
from django.utils import timezone
import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    notes = models.CharField(default='', max_length=200)

class Country(models.Model):
	name = models.CharField(max_length=100)
	language = models.CharField(max_length=100)
	state_number = models.IntegerField(default=1)
	city_number = models.IntegerField(default=1)
	# def __str__(self):
	# 	return self.name


class House(models.Model):
	address = models.CharField(max_length=200)
	person_number = models.IntegerField (default=0)

class Family(models.Model):
	person_number = models.IntegerField(default=0)
	house = models.ManyToManyField(House)

class Person(models.Model):
	name = models.CharField("person_name" , max_length=100)
	age  = models.IntegerField(default=0)
	family = models.ForeignKey(Family,null = True)
	country = models.ForeignKey(Country)
	def __unicode__(self):
		return '%s %s %s' % (self.name, self.age, self.country)

	

