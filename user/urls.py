from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('developing/', views.developing, name='developing'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
]