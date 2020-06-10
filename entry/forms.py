from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        model   = Entry
        fields  = ('name', 'title', 'content')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name..'
            }
        ),
            'title': forms.TextInput(attrs={
                'placeholder': 'Your title..'
            }
        ),
            'content': forms.Textarea(attrs={
                'placeholder': "What's on your mind?"
            }
        ),
    }