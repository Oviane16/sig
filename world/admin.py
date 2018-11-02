
from django.contrib.gis import admin
from .models import Region
from leaflet.admin import LeafletGeoAdmin

class RegionAdmin(LeafletGeoAdmin):
    pass
#admin.site.register(Region,admin.OSMGeoAdmin)
admin.site.register(Region,RegionAdmin)
