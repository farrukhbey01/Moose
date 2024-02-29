from django.urls import path
from .views import home, blog_detail,cantact,about,blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('blog/<int:pk>/', blog_detail, name = 'blog_detail'),
    path('contact/', cantact),
    path('about/',about),
    path('blog/',blog)



]