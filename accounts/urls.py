from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (
  login_view, 
  register_view, 
  profile_detail_view,
  logout_view,
  edit_profile
)
app_name = 'accounts'

urlpatterns = [
  path('', login_view, name='login-view'),





  path('accounts/logout/', logout_view, name='logout-view'),
  path('accounts/register/', register_view, name='register'),
  path('accounts/edit-profile/', edit_profile, name='edit-profile'),
  path('accounts/<slug>/', profile_detail_view, name='profile-detail-view'),

  

  

]

# Password reset 
# 1 - submit email form 
# 2 - email sent success message
# 3 - link to password reset form in email
# 4 - Passwrod successfully change message