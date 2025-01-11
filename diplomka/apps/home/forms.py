from django import forms
from . import models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'resize: none;'
            })
        }