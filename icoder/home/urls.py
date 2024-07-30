from django.contrib import admin
from django.urls import path, include
from home import views                                          #directly import the dir which is present locally, not the central one using '.'


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('featured_block/', views.featured_block, name = 'featured_block'),
    path('search/', views.search, name = 'search'),
    path('signup/', views.handleSignup, name = 'handleSignup'),
    path('login/', views.handleLogin, name = 'handleLogin'),
    path('logout/', views.handleLogout, name = 'handleLout'),
    path('update/', views.UpdateUserView.as_view(), name='update_user'),
]