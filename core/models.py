from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # slug = models.SlugField(unique=True, max_length=100)

    # class Meta:
    #     verbose_name_plural = "Categories"
    #     ordering = ['name']

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    
    def __str__(self):
        return f'{self.name}'
    
class Post(models.Model):
    
    STATUS = [
        ('pending','pending'),
        ('approved', 'approved')
    ]
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='Post_images')
    body = CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices= STATUS,max_length=100, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True, max_length=200, blank=True)
    
    
    
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)  # always regenerate from name
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}   by {self.author}'
   