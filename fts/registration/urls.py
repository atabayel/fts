from django.urls import path
from registration import views

app_name='registration'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cl_id>/edit', views.edit , name='edit'),
    path('<int:cl_id>/save', views.save , name='save'),
    path('new/', views.new  , name='new'),
    path('<int:cl_id>/delete', views.delete , name='delete'),
    path('authentication/', views.authentication, name='authentication'),
    ]
