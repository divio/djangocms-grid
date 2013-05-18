from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from djangocms_grid.models import Grid, GridColumn, DJANGOCMS_GRID_SIZE
from django.utils.translation import ugettext_lazy as _
from djangocms_grid.forms import GridPluginForm
from cms.models import CMSPlugin


class GridPlugin(CMSPluginBase):
    model = Grid
    name = _('Multi Columns (grid)')
    module = _('Multi Columns')
    render_template = 'djangocms_grid/grid.html'
    allow_children = True
    child_classes = ['GridColumnPlugin']
    form = GridPluginForm

    def render(self, context, instance, placeholder):
        context.update({
            'grid': instance,
            'placeholder': placeholder,
            'GRID_SIZE': DJANGOCMS_GRID_SIZE,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(GridPlugin, self).save_model(request, obj, form, change)
        for x in xrange(int(form.cleaned_data['create'])):
            col = GridColumn(parent=obj, placeholder=obj.placeholder, language=obj.language, size=form.cleaned_data['create_size'], position=CMSPlugin.objects.filter(parent=obj).count(), plugin_type=GridColumnPlugin.__name__)
            col.save()
        return response


class GridColumnPlugin(CMSPluginBase):
    model = GridColumn
    name = _('Grid Column')
    module = _('Multi Columns')
    render_template = 'djangocms_grid/column.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'column': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(GridPlugin)
plugin_pool.register_plugin(GridColumnPlugin)
