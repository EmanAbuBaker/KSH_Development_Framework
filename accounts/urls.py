from django.conf.urls import handler404
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib import admin
from accounts import views

urlpatterns = [
    path('', views.usersListView.as_view(), name='user_list'),
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),


]
