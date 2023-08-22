from django import forms
from .models import Advertisment

class AdvertismentForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ['title', 'descriptions', 'price', 'trades', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError('Title cannot start with a question mark.')
        return title
