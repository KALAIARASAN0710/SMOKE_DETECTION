
from django.urls import path
from . import views

urlpatterns = [
    # Other URLs
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('urldata/', views.urldata, name='urldata'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('submit_form/', views.your_form_processing_view, name='your_form_processing_view'),
]
