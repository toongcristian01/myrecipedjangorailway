from .models import Profile
from blog.models import Post, Category
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Q

#link/url to user profile
# def categories(request):

#   category_obj = Category.objects.all()
#   user_slug = profible_obj.slug
#   return { 'user_slug': user_slug } 

# def user_profile_detail(request):
#   recipe = Post.objects.filter(featured=True)[0]
#   profible_obj = Profile.objects.get()
#   user_slug = profible_obj.slug
#   return { 'user_slug': user_slug } 


def include_profile(request, slug):
  if not request.user.is_authenticated:
    profile = get_object_or_404(Profile, slug=slug)


    current_user = Profile.objects.get(user=request.user)
    myrecipes = Post.objects.filter(author=current_user)

    #display all recipes except yours/current user
    all_recipes = Post.objects.filter(Q(featured=True) & Q(status='published') & Q(author=profile))
    
    recipe_count = myrecipes.count()

    
    context = {
      'profile': profile,
      'myrecipes': myrecipes,
      'recipe_count': recipe_count,
      'all_recipes': all_recipes,

    }
    return (context)

def profile_recipe(request):
      
  current_user = Profile.objects.get(user=request.user)
  myrecipes = Post.objects.filter(author=current_user)
  return {'profile_recipe_context': myrecipes}

def category_list(request):
  #breakfast,lunch...
  category_list = Category.objects.all()
  return {'category_list': category_list}