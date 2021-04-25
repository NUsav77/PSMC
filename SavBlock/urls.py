from django.urls import path, include
from . import views
from register import views as v
from users.views import dashboard

urlpatterns = [
    path('', views.index, name='index'),
    path('list_tribes/', views.list_tribes, name='list_tribes'),
    path('register/', v.register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('anak_register/', v.anak_register, name='anak_register'),
]
