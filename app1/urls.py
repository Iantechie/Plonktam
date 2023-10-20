from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.index, name='index'),
    path('cover_detail/<int:pk>/', views.cover_details, name='cover_detail')
]
