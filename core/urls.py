from django.urls import path

from .  import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('post/create/', views.Create_Post, name="create"),
    path('post-details/<int:pk>/', views.PostDetails, name='post-details'),
    path('post/update/<int:pk>/edit/', views.Update_Post, name ="update"),
    path('post/<int:pk>/delete/', views.delete_post, name='delete'),
]
