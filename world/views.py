from django.shortcuts import render
from .models import Region
from django.core.serializers import serialize
from django.http import HttpResponse
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def getRegion(request):
    regions = serialize('geojson', Region.objects.all())
    return HttpResponse(regions,content_type='json')

def getRegion2(request):
    regions =GeoJSONSerializer().serialize(Region.objects.all(), use_natural_keys=True, with_modelname=False)
    return JsonResponse(regions, content_type='json')