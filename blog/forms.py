from django import forms
from .models import Post, Category

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content']
        labels = {
            'title': 'Title',
            'content': 'Content',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.order_by('name'),
        empty_label="Select a Category",  # Label for the empty/default choice
    )
 
