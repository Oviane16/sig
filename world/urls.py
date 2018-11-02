from django.urls import path
from . import views
app_name = 'world'

urlpatterns = [
        path('index', views.index, name='index'),
        path('getRegion', views.getRegion, name='getRegion'),
        path('getRegion2', views.getRegion2, name='getRegion2'),
]