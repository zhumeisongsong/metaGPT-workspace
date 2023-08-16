from django.urls import path
from . import views

urlpatterns = [
    path('api/register', views.register, name='register'),
    path('api/login', views.login, name='login'),
    path('api/photos', views.upload_photo, name='upload_photo'),
    path('api/photos/<int:photo_id>/comments', views.add_comment, name='add_comment'),
    path('api/photos/<int:photo_id>/likes', views.add_like, name='add_like'),
    path('api/photos/<int:photo_id>/likes/<int:like_id>', views.remove_like, name='remove_like'),
    path('api/logout', views.logout, name='logout'),
]
