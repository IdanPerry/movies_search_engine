from django.urls import path
from content import views

urlpatterns = [
    path('', views.index, name='index'),
    path('content_import/', views.import_content, name='content_import'),
    path('search/', views.search, name='search'),
    path('search/<str:title>/', views.search, name='search')
]
