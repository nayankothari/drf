from django.urls import path, include
from .views import RetriveData, ListDisplay


urlpatterns = [
    path('data/', ListDisplay.as_view()),
    path("data/curd/<int:pk>", RetriveData.as_view()),
    path("auth", include("rest_framework.urls")),
]
