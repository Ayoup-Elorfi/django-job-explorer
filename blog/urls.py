from django.urls import path
from .views import blog_view, blog_detail_view

app_name = 'blog'

urlpatterns = [

    path('', blog_view, name='blogs'),
    path('<slug:slug>/', blog_detail_view, name='detail'),
]
