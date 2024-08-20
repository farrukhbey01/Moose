from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

class RequestLog(models.Model):
    user_type = models.CharField(max_length=50, default='Nomalum shaxs')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    requested_url = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    request_body = models.TextField(null=True, blank=True)
    response_status_code = models.IntegerField()
    response_body = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_type} - {self.requested_url} - {self.timestamp}"




class Category(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='post/')
    author = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to='author/', default=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)


class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Comments(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ----  {self.email}'
