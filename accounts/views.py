from django.shortcuts import render, redirect
from .models import Profile
from blog.models import Post, Review
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .forms import EditProfileForm
from django.db.models import Q
from random import randint


def login_view(request):
  recipes = Post.objects.filter(Q(featured=True) & Q(status='published'))
  # random_num = randint(0, len(recipes)-1)

  #random recipe featured
  # recipe_featured = Post.objects.filter(featured=True)[random_num]
  recipe_featured = Post.objects.filter(Q(featured=True) & Q(status='published'))
  recipe_published = Post.objects.filter(status='published')


  # print(recipe_featured)
  # user_recipe = recipe_featured.photo.url
  # profile_image = recipe_featured.author.avatar.url
  # profile_name = recipe_featured.author.user

  # print(user_recipe)
  # print(recipe_featured.author)
  if request.user.is_authenticated:
    return redirect('blog:main-view')
  else:
    if request.method == 'POST':
      user_name = request.POST['username']
      password = request.POST['password']

      user = authenticate(username=user_name, password=password)
      if user is not None:
        login(request, user)
        return redirect('blog:main-view')
      else:
        messages.error(request, 'Invalid credentials')
        return redirect('accounts:login-view')

  print(recipe_featured)
      
  context = {
    'recipes': recipes,
    'recipe_featured': recipe_featured,
    # 'profile_image': profile_image,
    # 'profile_name': profile_name,
    # 'user_recipe': user_recipe,
    'recipe_published': recipe_published,
  }


  return render(request, 'accounts/login.html', context)




@login_required(login_url="/")
def logout_view(request):
  logout(request)
  return redirect('accounts:login-view')



def register_view(request):
  if request.user.is_authenticated:
    return redirect('accounts:main-view')
  else:
  
    if request.method == 'POST':
      
      first_name = request.POST['firstname']
      last_name = request.POST['lastname']
      user_name = request.POST['username']
      email = request.POST['email']
      password = request.POST['password1']
      confirm_password = request.POST['password2']

      to_slug = f"{first_name}-{last_name}"

      if password == confirm_password:
        #check if username and email exists
        if User.objects.filter(username=user_name).exists():
          #username already exists
          messages.error(request, 'Username already exists')
          return redirect('accounts:register')
        else:
          if User.objects.filter(email=email).exists():
            #email already exists
            messages.error(request, 'Email already exists')
            return redirect('accounts:register')
          else:
            
            #*if valid
            
            # create User object
            user = User.objects.create_user(
              first_name=first_name,
              last_name=last_name,
              username=user_name,
              email=email,
              password=password,
            )

            # create Profile for User
            user_profile = Profile.objects.create(
              first_name=first_name,
              last_name=last_name,
              slug=to_slug,
              user=user,
            )
            
            user.save()
            #user_profile.save()
            messages.warning(request, 'Account Registered for ' + str(user))
            return redirect('accounts:login-view')
      else:
        messages.error(request, 'Password do not match')
        return redirect('accounts:register')
      
  return render(request, 'accounts/register.html')





  
# @login_required(login_url="/")
def profile_detail_view(request, slug):
  profile = get_object_or_404(Profile, slug=slug)
  # current_user = Profile.objects.get(user=request.user)
  # myrecipes = Post.objects.filter(author=current_user)

  all_reviews = []
 

  #display all recipes except current user
  all_recipes = Post.objects.filter(Q(status='published') & Q(author=profile))
  recipe_published = Post.objects.filter(Q(status='published') & Q(author=profile))
  reviews = Post.objects.filter(Q(status='published') & Q(author=profile) & Q(reviews__isnull=False))
  recipe_count = all_recipes.count()
  
  #*GET USER REVIEWS
  #loop tru all published recipes of user
  for recipe in recipe_published:
    all_reviews.append(recipe.reviews.all())

  #loop tru recipe has a review and review count (queryset.count())
  #delete empty queryset
  all_reviews_result = [reviews.count() for reviews in all_reviews if reviews]

  #get all user recipe reviews count
  user_reviews_count = sum(all_reviews_result)

  # print(all_reviews)
  # print(all_reviews_result)
  # print(user_reviews_count)


  #*GET USER RATING
  for recipe in recipe_published:
    all_reviews.append(recipe.reviews.all())
  
  all_avg_review = [reviews.average_review() for reviews in recipe_published]
  #delete empty queryset
  all_avg_review_result = [reviews for reviews in all_avg_review if reviews]
  
  try:
    get_avg_review = (sum(all_avg_review_result) / len(all_avg_review_result))
  except ZeroDivisionError:
    get_avg_review = 0

  get_count_review = len(all_avg_review_result)

  # print(all_avg_review)
  # print(all_avg_review_result)
  # print(get_avg_review)
  print(get_count_review)

  context = {
    'profile': profile,
    'recipe_count': recipe_count,
    'all_recipes': all_recipes,
    'recipe_published': recipe_published,
    'user_reviews_count': user_reviews_count,
    'get_avg_review': get_avg_review,
    'get_count_review': get_count_review,
  }

  return render(request, 'accounts/profile.html', context)



@login_required(login_url="/")
def edit_profile(request):
  #get profile of current logged in user
  user_profile = Profile.objects.get(user=request.user)
  
  if request.method == 'POST':
    edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
    if edit_profile_form.is_valid():
      edit_profile_form.save()
      return redirect('accounts:profile-detail-view', slug=user_profile.slug)
  else:
    #form with prefilled info
    edit_profile_form = EditProfileForm(instance=user_profile)
    
  context = {'form': edit_profile_form}
  
  return render(request, 'accounts/edit_profile.html', context)



