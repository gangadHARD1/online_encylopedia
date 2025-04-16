from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search,name="search"),
    path("new_page",views.new,name="new_page"),
    path("random",views.rdom,name="random"),
    path("<str:name>",views.entry,name="entry")
    
]
