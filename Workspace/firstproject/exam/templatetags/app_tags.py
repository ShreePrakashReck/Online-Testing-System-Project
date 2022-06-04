from django import template
import datetime 
register=template.Library()

@register.simple_tag(name="get_date")
def get_date():
    x=datetime.datetime.now()
    return x
@register.filter 
def quotes(value):
   x= '"'+str(value)+'"'
   return x