function(){
    return new OpenLayers.Layer.Vector("{{ layer.name }}", {
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: "{{ layer.layer_uri }}",
                format: new OpenLayers.Format.{{ layer.type|upper }}({
                    extractStyles: {{ layer.extract_styles }}, 
                    extractAttributes: {{ layer.extract_attributes }},
                    maxDepth: 2
                })
            })
        })
}()