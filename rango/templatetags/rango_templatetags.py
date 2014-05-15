from django import template
from rango.models import Category

register = template.Library()
def hello_world(parser, token):
	tag_name, format_string = token.split_contents()
	print "format_string is ",format_string
	print "hellonode ", helloNode(format_string)
	return helloNode(format_string)

class helloNode(template.Node):
	def __init__(self, format_string):
		self.format_string = format_string
	def render(self, context):
		return self.format_string.upper()

register.tag('hello',hello_world)

@register.simple_tag(name="gb")
def goodbye(string_format):
	return string_format + "goodbye"

@register.inclusion_tag('rango/credit.html')
def show_credit():
	all_cate = Category.objects.all()
	return {"hale":"haleluya", "categories" : all_cate}
