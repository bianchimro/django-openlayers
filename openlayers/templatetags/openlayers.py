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
def div_for_map(mapid):
    '''
    Inclusion tag sample
    '''
    return {'mapid':mapid}

    
@register.simple_tag
def map_var(mapid):
    return "map-" + str(mapid)


@register.simple_tag
def raster_layer_var(layer):
    return "layer_r_" + str(layer.id)
    
    
@register.simple_tag
def vector_layer_var(layer):
    return "layer_v_" + str(layer.id)
    
    
@register.inclusion_tag('tags/_map_instance.js')
def map_instance(map):
    return {'map':map}
    

@register.inclusion_tag('tags/_vector_layer_js_instance.js')
def vector_layer_instance(layer):
    return {'layer':layer}
    
@register.inclusion_tag('tags/_raster_layer_js_instance.js')
def raster_layer_instance(layer):
    return {'layer':layer}
    
    
