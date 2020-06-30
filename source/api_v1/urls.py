from django.urls import path, include
from rest_framework import routers

from api_v1.views import UserProvideAccessView, DepriveUserAccessView

router = routers.DefaultRouter()


app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('file/<int:pk>/access/provide', UserProvideAccessView.as_view(), name='provide_access'),
    path('file/<int:pk>/access/deprive', DepriveUserAccessView.as_view(), name='deprive_user')
]