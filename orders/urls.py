from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.MakeOrder.as_view(), name='MakeOrder'),
]

