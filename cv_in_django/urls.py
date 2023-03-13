from django.urls import path
from . import views

urlpatterns = [
    # path("", homePageView, name="home"),
    path("", views.displayPage, name="parametr"),
]