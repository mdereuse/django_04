from django.urls import path
from . import views

urlpatterns = [
    path("django", views.django_presentation, name="django_presentation"),
    path("affichage", views.display_presentation, name="display_presentation"),
    path("templates", views.templates_presentation, name="templates_presentation"),
]
