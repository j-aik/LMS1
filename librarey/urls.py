from django.contrib import admin
from django.urls import path
from librarey import views

app_name = "librareyapp"


urlpatterns = [
    path('librarey',views.librarey,name="librarey"),


]