from dataclasses import field
from django import forms
from snippets.models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'desc')
