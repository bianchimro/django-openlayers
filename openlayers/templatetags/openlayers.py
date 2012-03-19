from django import template
register = template.Library()

@register.filter()
def contains(value, arg):
  """
  Usage:
  {% if text|contains:"http://" %}
  This is a link.
  {% else %}
  Not a link.
  {% endif %}
  """
  
  return arg in value 



@register.inclusion_tag('tags/_div_for_map.html')
def div_for_map(map):
    '''
    Inclusion tag sample
    '''
    return {'map':map}
    
@register.simple_tag
def map_var(map):
    
    return "map" + str(map.id)
    
@register.inclusion_tag('tags/_map_instance.js')
def map_instance(map):
    '''
    Inclusion tag sample
    '''
    return {'map':map}