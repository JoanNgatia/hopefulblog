from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """create form based on model created"""
    class Meta:
        model = Post
        fields = ('title', 'text',)