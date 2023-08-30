from django.shortcuts import render, redirect
from .forms import CreateRecipeForm, EditRecipeForm, EditDraftForm, RateForm
from accounts.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Category, Review
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser


def home_view(request):
  return render(request, 'blog/home.html')

def about_view(request):
  return render(request, 'blog/about.html')


@login_required(login_url="/")
def main_view(request):
  recipes = Post.objects.filter(status='published')

  context = {
    'recipes': recipes,
    }
  
  return render(request, 'blog/home.html', context)


def recipe_detail(request, slug):
  
  recipe = get_object_or_404(Post, slug=slug)
  profile_image = recipe.author.avatar.url
  profile_name = recipe.author.user
  user = request.user 
  user1 = request.user 

  
  #Check if you submitted a review on a recipe already
  is_reviewed = False

  
  recipe_user = ''
  test = Review.objects.filter(recipe=recipe)
  for t in test:
    recipe_user = t.user
    #print(t.recipe)
  
  if request.method == 'POST':
    form = RateForm(request.POST)

    rating = request.POST['rating']
    content = request.POST['content']


    obj = Review.objects.create(
      content=content,
      rate=rating,
      user=user,
      recipe=recipe
    )
    obj.save()
    print('success')
    return redirect('blog:recipe-detail', slug=recipe.slug)
  else:
    print('failed')



  #review form
  # if request.method == 'POST':
  #   rate_form = RateForm(request.POST)
  #   if rate_form.is_valid():
  #     rate = rate_form.save(commit=False)
  #     rate.user = user
  #     rate.recipe = recipe
  #     rate.save()
  #     return redirect('blog:recipe-detail', slug=slug)
  # else:
  #   rate_form = RateForm()


  # if request.method == 'POST':
  #   form = RateForm(request.POST or None)
  #   if form.is_valid():
  #     data = form.save(commit=False)
  #     data.rate = form.cleaned_data['rating']
  #     data.content = form.cleaned_data['content']
  #     data.recipe_id = recipe.id
  #     data.user_id = request.user.id
  #     data.save()
  #     return redirect('recipe-detail', slug=recipe.slug)
  #   else:
  #     print('failed')

  context = {
    'recipe': recipe,
    'profile_image': profile_image,
    'profile_name': profile_name,
    #'rate_form': rate_form,
    'is_reviewed': is_reviewed,
    'test': test,
    'recipe_user': recipe_user,
    #'get_count_review': get_count_review,

  }

  
  return render(request, 'blog/recipe_detail.html', context)



# def submit_review(request, recipe_id):
#   #current url
#   url = request.META.get('HTTP_REFERER')

#   if request.method == 'POST':
#     form = RateForm(request.POST)
#     if form.is_valid():
#       data = Review()
#       data.rate = form.cleaned_data['rating']
#       data.content = form.cleaned_data['content']
#       data.recipe_id = recipe_id
#       data.user_id = request.user.id
#       data.save()
#       return redirect(url)




@login_required(login_url="/")
def my_recipes_view(request):
  profile = Profile.objects.get(user=request.user)
  myrecipes = Post.objects.filter(author=profile)
  published_recipe = Post.objects.filter(Q(status='published') & Q(author=profile))
  

  context = {
    'myrecipes': myrecipes,
    'published_recipe': published_recipe,
    }
  return render(request, 'blog/my_recipes.html', context)



@login_required(login_url="/")
def create_recipe(request):
  profile = Profile.objects.get(user=request.user)
  print(profile)

  if request.method == 'POST':
    create_recipe_form = CreateRecipeForm(request.POST, request.FILES)

    if create_recipe_form.is_valid():
      instance = create_recipe_form.save(commit=False)
      instance.author = profile
      instance.save()

      print('succes created')
      # messages.success(request, 'Recipe Created')
      return redirect('blog:create-recipe')
    else:
      print('failed')
  else:
    create_recipe_form = CreateRecipeForm()

  context = {
    'create_recipe_form': create_recipe_form,
  }
      
  return render(request, 'blog/create_recipe.html', context)


@login_required(login_url="/")
def edit_recipe(request, slug):
  # profile = Profile.objects.get(user=request.user)
  # recipe = Post.objects.get(author=profile)

  recipe = get_object_or_404(Post, slug=slug)

  if request.method == 'POST':
    edit_recipe_form = EditRecipeForm(request.POST, request.FILES, instance=recipe)
    
    if edit_recipe_form.is_valid():
      edit_recipe_form.save()
      return redirect('blog:myrecipes-view')
  else:
    edit_recipe_form = EditRecipeForm(instance=recipe)
  
  context = {
    'edit_recipe_form': edit_recipe_form
  }

  return render(request, 'blog/edit_recipe.html', context)

def delete_recipe(request, slug):
  recipe = get_object_or_404(Post, slug=slug)

  if request.method == 'POST':
    recipe.delete()
    return redirect('blog:myrecipes-view')

  context = {'recipe': recipe}
  return render(request, 'blog/delete_recipe.html', context)

@login_required(login_url="/")
def draft_view(request):
  recipe_draft = ''
  if request.method == 'POST':
    profile = Profile.objects.get(user=request.user)
    searched_draft = request.POST['searched-draft']
    searched_recipe_draft = Post.objects.filter(Q(title__contains=searched_draft) & Q(status='draft') & Q(author=profile))

    searched_count = searched_recipe_draft.count()

    context = {
      'searched_draft': searched_draft,
      'searched_recipe_draft': searched_recipe_draft,
      'searched_count': searched_count,
    }
   
    
    return render(request, 'blog/draft_view.html', context)
  else:
    profile = Profile.objects.get(user=request.user)
    recipe_draft = Post.objects.filter(Q(status='draft') & Q(author=profile))
    recipe_draft_count = recipe_draft.count()

    context = {
      'recipe_draft': recipe_draft,
      'recipe_draft_count': recipe_draft_count,
    }
  return render(request, 'blog/draft_view.html', context)


@login_required(login_url="/")
def edit_recipe_draft(request, slug):
  recipe = get_object_or_404(Post, slug=slug)

  if request.method == 'POST':
    edit_draft_form = EditDraftForm(request.POST, instance=recipe)
    
    if edit_draft_form.is_valid():
      edit_draft_form.save()
      return redirect('blog:draft-view')
  else:
    edit_draft_form = EditDraftForm(instance=recipe)
  
  context = {
    'edit_recipe_form': edit_draft_form,
    'recipe': recipe,
  }

  return render(request, 'blog/edit_draft.html', context)

@login_required(login_url="/")
def delete_recipe_draft(request, slug):
  recipe = get_object_or_404(Post, slug=slug)

  if request.method == 'POST':
      recipe.delete()
      return redirect('blog:draft-view')

  context = {
      'recipe': recipe
  }
  return render(request, 'blog/delete_draft.html', context)


def search_recipes(request):
  #recipes = Post.objects.filter(status='published')

  if request.method == 'POST':
    searched = request.POST['searched']
    recipes = Post.objects.filter(Q(title__contains=searched) & Q(status='published'))

    searched_count = recipes.count()

    context = {
      'searched': searched,
      'recipes': recipes,
      'searched_count': searched_count,
    }
    
    return render(request, 'blog/search.html', context)
  else:
    return render(request, 'blog/search.html')

def category_view(request, cats):
  category_recipes = Post.objects.filter(Q(category__name=cats) & Q(status='published'))
  category = Category.objects.filter(name=cats)[0]

  context = {
    'cats': cats,
    'category_recipes': category_recipes,
    'category': category,

  }
  return render(request, 'blog/categories.html', context)


