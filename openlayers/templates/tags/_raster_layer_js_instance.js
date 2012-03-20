{% load openlayers %}function(){
{% if layer.type == 'OSM' %}
    return new OpenLayers.Layer.OSM("{{ layer.name }}");
{% endif %}
{% if layer.type|contains:'GOOGLE' %}
    {% if layer.type == 'GOOGLE-STREET' %}
        var type = google.maps.MapTypeId.STREET;
    {% endif %}
    {% if layer.type == 'GOOGLE-SATELLITE' %}
        var type = google.maps.MapTypeId.SATELLITE;
    {% endif %}
    {% if layer.type == 'GOOGLE-TERRAIN' %}
        var type = google.maps.MapTypeId.TERRAIN;    
    {% endif %}
    {% if layer.type == 'GOOGLE-HYBRID' %}
        var type = google.maps.MapTypeId.HYBRID;
    {% endif %}
    return new OpenLayers.Layer.Google("{{ layer.name }}",
        { type : type }
    );
{% endif %}
}()