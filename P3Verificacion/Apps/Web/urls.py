from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contador/', views.contador, name='contador'),
]