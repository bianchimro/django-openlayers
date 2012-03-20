new OpenLayers.Map('map-{{ map.id }}',{
        controls : [    
                    {% if map.navigation_control %}
                        new OpenLayers.Control.Navigation(),
                    {% endif %}
                    {% if map.pan_zoom_bar_control %}
                        new OpenLayers.Control.PanZoomBar(),
                    {% endif %}
                    {% if map.layer_switcher_control %}
                        new OpenLayers.Control.LayerSwitcher(),
                    {% endif %}
                        //new OpenLayers.Control.Permalink(),
                    {% if map.scale_line_control %}
                        new OpenLayers.Control.ScaleLine(),
                    {% endif %}
                        //new OpenLayers.Control.Permalink('permalink'),
                        //new OpenLayers.Control.MousePosition(),
                        //new OpenLayers.Control.OverviewMap(),
                        //new OpenLayers.Control.KeyboardDefaults()
                    ]
        }
    )