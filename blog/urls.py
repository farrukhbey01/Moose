from django.urls import path
from .views import home, blog_detail_view, contact, about, blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('blog/<int:pk>/', blog_detail_view, name='blog_detail'),
    path('contact/', contact),
    path('about/', about),
    path('blog/', blog)

]
