from django.urls import path
from apps.auth import views

app_name = 'auth'


urlpatterns = [
    path('', views.Dashboard.as_view(), name="home"),
]