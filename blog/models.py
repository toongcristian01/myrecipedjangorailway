from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from ckeditor.fields import RichTextField
from django.urls import reverse

from django.template.defaultfilters import slugify
from .utils import get_random_code
from django.db.models import Avg

from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='categories/')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"
  

  def get_url(self):
    #from urls.py, blog/category/category_name
    return reverse('blog:category-view', args=[self.name] )

OPTIONS = (
  #db       frontend/admin
  ('draft', 'Draft'),
  ('published', 'Published'),
)

class NewManager(models.Manager):
  #custom queryset
  def get_queryset(self):
    return super().get_queryset().filter(status='published')

class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    photo = models.ImageField(default='noimage.jpg', upload_to='posts/', null=True, blank=True)
    cooking_time = models.CharField(max_length=50, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    description = models.CharField(max_length=500, null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    status = models.CharField(max_length=10, choices=OPTIONS, default='draft')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()

    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    class Meta:
      ordering = ('-created',)


    def __str__(self):
        return self.title
    
    def average_review(self):
      reviews = Review.objects.filter(recipe=self).aggregate(average=Avg('rate'))
      avg = 0
      if reviews['average'] is not None:
        avg = float(reviews['average'])
      return avg
    
    def count_review(self):
      count_review = Review.objects.filter(recipe=self).count()
      return count_review
    
  

    
    #generate slug
    def save(self, *args, **kwargs):
      ex = False

      #if title is filled out
      if self.title:
        to_slug = slugify(str(self.title))

        #return true
        ex = Post.objects.filter(slug=to_slug).exists()

        #if slug already exists
        while ex:
          to_slug = slugify(to_slug + " " + str(get_random_code()))
          ex = Post.objects.filter(slug=to_slug).exists()

      #if title blank
      else:
        to_slug = str(self.title)

      self.slug = to_slug
      super().save(*args, **kwargs)
    

    @property
    def get_reviews(self):
      # Post.reviews.all(), reviews->from Post related name in Review model
      return self.reviews.all().order_by('-timestamp')
    

RATE_CHOICES = [
  (1, '1 - Bad'),
  (2, '2 - Poor'),
  (3, '3 - Average'),
  (4, '4 - Great'),
  (5, '5 - Excellent'),
]

class Review(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  recipe = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  #rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, blank=True)
  rate = models.FloatField()
  # rate = models.IntegerField(default=0, validators=[
  #   MaxValueValidator(5),
  #   MinValueValidator(0),
  # ])

  def __str__(self):
      return str(self.user)
  

  

  # def count_review()