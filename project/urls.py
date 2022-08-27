from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProjectListCreateAPIView.as_view(), name="project-list-create"),
]