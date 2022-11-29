from django.urls import path
from .views import stori_list, stori_detail
urlpatterns = [
    path("mastori/", stori_list, name="stori_list"),
    path("stori/<int:pk>/", stori_detail, name="stori_detail")
]