from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page,name='home_page'),
    path(r'project/new',views.submit_project,name='submit_project')
]	