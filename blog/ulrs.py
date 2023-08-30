from django.urls import path
from . import views
app_name = 'blog'


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.create_blog, name='addblock'),
    path('<int:blog_id>/', views.detail, name='detail')
]