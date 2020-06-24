'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
 STATUS_CHOICES = (
 ('draft', 'Draft'),
 ('published', 'Published'),
 )
 title = models.CharField(max_length=250) # this is the field for the post title.
 slug = models.SlugField(max_length=250, # this field is intended to be used in urls
 unique_for_date='publish') # 
 author = models.ForeignKey(User, # this field defines a many to one relationship
 on_delete=models.CASCADE, #  The on_delete parameter specifies the behavior to adopt when the referenced object is deleted
 related_name='blog_posts')
 body = models.TextField()# this is the body of the post
 publish = models.DateTimeField(default=timezone.now) # This datetime indicates when the post was published
 created = models.DateTimeField(auto_now_add=True) # This datetime indicates when the post was created
 updated = models.DateTimeField(auto_now=True) #  This datetime indicates the last time the post was updated
 status = models.CharField(max_length=10, # This field shows the status of a post
 choices=STATUS_CHOICES,
 default='draft')

 class Meta:
     ordering = ('-publish',)
     def __str__(self):
         return self.title


class PublishedManager(models.Manager):
 def get_queryset(self):
     return super(PublishedManager,
 self).get_queryset()\
 .filter(status='published')

# class Post(models.Model):
     # ...
 #    def get_absolute_url(self):
  #        return reverse('blog:post_detail',
   #       args=[self.publish.year,
    #      self.publish.month,
    #      self.publish.day, self.slug])
'''
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])
