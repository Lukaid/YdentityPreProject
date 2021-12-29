from django.urls import path

from jitsi import views

app_name = 'jitsi'

urlpatterns = [
    path('', views.get_jitsi),
]
