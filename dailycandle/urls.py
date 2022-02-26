from django.urls import path
from . import views

app_name = "dailycandle"

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('holding', views.holding, name="holding"),
    path('metrics', views.metrics, name="metrics"),
    path('<str:id>/stockdetails', views.stockdetails, name="stockdetails"),

]   