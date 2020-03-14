from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()


app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]