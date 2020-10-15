from django.urls import path

from .views import detail, fav, save, sub_list

app_name = "products"
urlpatterns = [
    path("", sub_list, name="sub_list"),
    path("save", save, name="sauve"),
    path("fav", fav, name="fav"),
    path("detail", detail, name="detail"),
]
