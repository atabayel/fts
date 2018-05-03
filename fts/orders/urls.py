from django.urls import path
from orders import views

app_name='orders'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new , name='new'),
    path('test/', views.test , name='test'),
    path('<int:or_id>/delete', views.delete , name='delete'),
   path('deleteall/', views.deleteall , name='deleteall'),
    ]

