new OpenLayers.Layer.Vector("{{ layer.name }}", {
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: "{{ layer.layer_uri }}",
                format: new OpenLayers.Format.{{ layer.type|upper }}({
                    extractStyles: true, 
                    extractAttributes: true,
                    maxDepth: 2
                })
            })
        })