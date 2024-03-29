from django.conf.urls import url, patterns
from rango import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^about/$', views.about, name = 'about'),
	url(r'^add_category/$', views.add_category, name = 'add_category'),
	url(r'^category/(?P<category_name_url>\w+)/$', views.category, name = 'category'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^login/$', views.user_login, name = 'login'),
	url(r'^logout/$', views.log_out, name = 'logout')
	)