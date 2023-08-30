from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('first_name', 'last_name')}

  # def save_model(self, request, obj, form, change):
  #   obj.profile.create(first_name=obj.user.first_name, last_name=obj.user.last_name)
  #   # obj.user.first_name = obj.profile.first_name
  #   # obj.user.last_name = obj.profile.last_name
  #   obj.profile.save()
  #   super().save_model(request, obj, form, change)

admin.site.register(Profile, ProfileAdmin)
