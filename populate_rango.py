import os

def populate():
	python_cat = add_cat('Python')

	add_page(cat = python_cat,
		title = "Pro Python",
		url = "http://google.com")

	add_page(cat = python_cat,
		title = "Effective Python",
		url = "http://gamek.com")

	ruby_cat = add_cat('Ruby')

	add_page(cat = ruby_cat,
		title = "Pro Ruby",
		url = "http://xuanvinh.com")

	add_page(cat=ruby_cat,
		title = "Ruby in 2 days",
		url = "http://soha.vn")

	java_cat = add_cat('Java')

	add_page(cat = java_cat,
		title = "Spring 3 + struct 2",
		url = "http://dantri.com")

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

def add_page(cat, title, url , views = 0):
	p = Page.objects.get_or_create(category = cat, title = title, url = url, views = views)
	return p

if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    from rango.models import Category, Page
    populate()