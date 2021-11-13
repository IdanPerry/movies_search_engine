from django.urls import path
from content_data import views

urlpatterns = [
    path('data_import/', views.import_data, name='data_import')
]
