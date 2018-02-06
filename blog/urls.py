from django.urls import path
from . import views
urlpatterns = [
    path('', views.list, name='blog'),
    path('<int:id>/', views.post, name='post'),#blog/id
]
#blog/java/id
#blog/python/django/id
