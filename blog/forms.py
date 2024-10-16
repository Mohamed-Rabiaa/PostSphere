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
 
    def clean_title(self):
        title = self.cleaned_data.get('title')
        contains_alphabet = False

        # Check if the title contains at least one alphabetic character
        if not any(char.isalpha() for char in title):
            raise forms.ValidationError('Please enter a valid title containing letters')
        return title
