from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('blog/', views.BlogView, name='Blog'),
    path('blog/<slug>/', views.detailBlog, name='DetailBlog'),
    path('add_blog/', views.addBlog, name='addblog')
]