from django.urls import path
from . import views

urlpatterns = [
    path('/', views.chatbot, name='chatbot'),
    # path('login', views.login, name='login'),  # Comment this line out or remove it
    path('/register', views.register, name='register'),
    path('/logout', views.logout, name='logout'),
]




