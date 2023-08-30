from django.urls import path
from .views import (
  home_view, 
  my_recipes_view,
  create_recipe,
  main_view,
  recipe_detail,
  edit_recipe,
  delete_recipe,
  draft_view, 
  edit_recipe_draft,
  delete_recipe_draft,
  search_recipes,
  category_view,
  about_view,
)

app_name = 'blog'

urlpatterns = [
  path('', main_view, name='main-view'),
  path('myrecipes/', my_recipes_view, name='myrecipes-view'),
  path('create-recipe/', create_recipe, name='create-recipe'),
  path('recipe-detail/<slug>/', recipe_detail, name='recipe-detail'),
  path('edit-recipe/<slug>/', edit_recipe, name='edit-recipe'),
  path('delete-recipe/<slug>/', delete_recipe, name='delete-recipe'),
  path('draft-view/', draft_view, name='draft-view'),

  path('edit-draft/<slug>', edit_recipe_draft, name='edit-draft'),
  path('delete-draft/<slug>', delete_recipe_draft, name='delete-draft'),
  path('search-recipes/', search_recipes, name='search-recipes'),
  path('category/<cats>/', category_view, name='category-view'),
  path('about/', about_view, name='about-view'),
  #path('rate-recipe/slug/', rate, name='rate-recipe'),
  #path('submit-review/<int:recipe_id>/', submit_review, name='submit-review'),
]