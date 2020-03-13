from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from webapp.views import IndexView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]