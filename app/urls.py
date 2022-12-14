from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name ='logout'),
    path('profile/<str:pk>', views.profile , name='profile'),
    path('upload' , views.upload, name = 'upload'),
    path('delete' , views.delete, name='delete'),
]