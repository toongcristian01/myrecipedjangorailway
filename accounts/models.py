from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import slugify
from .utils import get_random_code
from django.urls import reverse


# SOCIAL_CHOICES = (
#   #db          #frontend 
#   'facebook', 'facebook',
#   'instagram', 'instagram',
#   'pinterest', 'pinterest',
#   'twitter', 'twitter',
# )

class Profile(models.Model):
  first_name = models.CharField(max_length=200, blank=True)
  last_name = models.CharField(max_length=200, blank=True)
  avatar = models.ImageField(default='avatar.jpg', upload_to='avatars/')
  slug = models.SlugField(max_length=200, unique=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.URLField(max_length=50, blank=True)
  location = models.CharField(max_length=200, blank=True)
  bio = models.TextField(max_length=200, blank=True)
  email = models.EmailField(max_length=200, blank=True)
  facebook = models.CharField(max_length=200, blank=True)
  twitter = models.CharField(max_length=200, blank=True)
  instagram = models.CharField(max_length=200, blank=True)
  pinterest = models.CharField(max_length=200, blank=True)
  others = models.CharField(max_length=200, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created',)

  def __str__(self):
    return str(self.user)
  
  #profile detail slug
  def get_absolute_url(self):
    return reverse('accounts:profile-detail-view', kwargs={'slug': self.slug})
  
  #generate slug
  # def save(self, *args, **kwargs):
  #   ex = False

  #   #if fname & lname exist
  #   if self.first_name and self.last_name:
  #     to_slug = slugify(str(self.first_name) + " " + str(self.last_name))

  #     #return true
  #     ex = Profile.objects.filter(slug=to_slug).exists()

  #     #if slug exists
  #     while ex:
  #       to_slug = slugify(to_slug + " " + str(get_random_code()))
  #       ex = Profile.objects.filter(slug=to_slug).exists()

  #   #if fname & lname blank
  #   else:
  #     to_slug = str(self.user)
  #   self.slug = to_slug
  #   super().save(*args, **kwargs)

  
  



