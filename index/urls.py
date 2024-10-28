from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('video/<int:pk>', views.video_page),
    path('search', views.search),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view)
]
