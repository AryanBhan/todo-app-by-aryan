from django.contrib import admin
from django.urls import path
from todo_start import views
from todo_start.views import edit
urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.index,name="home"),
    path("about",views.about,name="about"),
    path("edit/<list_id>",views.edit,name='edit'),
    path("delete/<list_id>",views.delete,name='delete'),
    path("cross/<list_id>",views.cross,name='cross'),
    path('uncross/<list_id>',views.uncross,name='uncross')
]