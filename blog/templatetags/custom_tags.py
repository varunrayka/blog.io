from django import  template

register=template.Library()
@register.simple_tag()
def halfcontent(details):
	return details[:int(len(details)/3)]