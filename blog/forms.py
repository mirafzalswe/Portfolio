from django import forms
from .models import Model
class AddBlock(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['image', 'title', 'description']


