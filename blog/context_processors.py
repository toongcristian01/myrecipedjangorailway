from .models import Category, Post, Review
from django.shortcuts import get_object_or_404
from accounts.models import Profile
from django.contrib.auth.models import AnonymousUser

def category_list(request):
  category_list = Category.objects.all()
  return {'category_list': category_list}



def check_if_review_submitted(request):
  is_reviewed = False
  try:
    Review.objects.get(user=request.user)
    is_reviewed = True
  except Review.DoesNotExist:
    is_reviewed = False
  return {'is_reviewed_context': is_reviewed}


def user_review_avatar(request):
  if not request.user.is_authenticated:
    profile = Profile.objects.get(user=request.user)
    profile_image = profile.avatar.url
    return {'user_review_avatar': profile_image}
 
  return {'user_review_avatar': profile_image}