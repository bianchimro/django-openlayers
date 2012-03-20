<script>
     
    var map{{ map.id }} = {% include "_map_instance.js" with map=map %};
    //raster layers
    {% for layer in map.raster_layers.all %}
        var layer_r_{{ layer.id }} = {% include "_raster_layer_js_instance.js" with layer=layer %};
        map{{ map.id }}.addLayer(layer_r_{{ layer.id }});
    {% endfor %}
    //vector layers
    {% for layer in map.vector_layers.all %}
        var layer_v_{{ layer.id }} = {% include "_vector_layer_js_instance.js" with layer=layer %};
        map{{ map.id }}.addLayer(layer_v_{{ layer.id }});
    {% endfor %}
    //zooming
    
     map{{ map.id }}.zoomToMaxExtent();
    

</script>