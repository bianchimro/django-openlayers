from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms_models import MapPluginModel

class MapPlugin(CMSPluginBase):
    model = MapPluginModel
    name = _("Openlayers Map Plugin")
    render_template = "cms/map_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(MapPlugin)