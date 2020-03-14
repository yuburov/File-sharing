from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from webapp.views import IndexView, FileCreateView, FileView, FileUpdateView, FileDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileView.as_view(), name='file_detail'),
    path('file/create/', FileCreateView.as_view(), name='file_create'),
    path('files/<int:pk>/update/', FileUpdateView.as_view(), name='file_update'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),

]