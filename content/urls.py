from django.urls import path
from content import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test')
]
