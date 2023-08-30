from django import forms
from .models import Post, Review, RATE_CHOICES


class CreateRecipeForm(forms.ModelForm):
  # featured = forms.BooleanField(widget=forms.RadioSelect(attrs={'class': 'featured-radio-btn'}))
  class Meta:
    model = Post
    fields = ('title', 'photo', 'cooking_time', 'description', 'content', 'category', 'status', 'featured')
    #exclude = ('author', 'liked', 'updated', 'created')

class EditRecipeForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ('author', 'liked', 'updated', 'created', 'slug')

class EditDraftForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('status',)

class RateForm(forms.ModelForm):
  #content = forms.CharField(widget=forms.Textarea(attrs={'class': 'review-content'}), required=False)
  # rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'class': 'review-rate'}), required=True)


  class Meta:
    model = Review
    fields = ('content', 'rate')
  
  # def clean(self):
  #   cleaned_data = super().clean()
  #   rate = cleaned_data.get("rating")







