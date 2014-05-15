from django.conf.urls import patterns, url
from django.views.generic import DetailView
from .models import Person

from polls import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^country/$', views.country, name='country'),
	url(r'^list_country/$', views.list_country, name='list_country'),
	url(r'^(?P<country_id>\d+)/country_detail/$', views.country_detail, name='country_detail'),
	url(r'^create_country/$', views.create_country, name='create_country'),
	url(r'^(?P<country_id>\d+)/update_country/$', views.update_country, name='update_country'),
	url(r'^(?P<country_id>\d+)/delete_country/$', views.delete_country, name='delete_country'),
	url(r'^search_country_by_name/$', views.search_country_by_name, name='search_country_by_name'),
	url(r'^persons/$',views.PersonList.as_view(),name='person_list'),
	url(r'^person/(?P<pk>\d+)/$', DetailView.as_view(model=Person,context_object_name = 'person'),name='person_detail'),
	url(r'^person$',views.PersonCreate.as_view(success_url="persons"),name='create_person'),
	url(r'^house$',views.HouseView.as_view(),name='house'),
)