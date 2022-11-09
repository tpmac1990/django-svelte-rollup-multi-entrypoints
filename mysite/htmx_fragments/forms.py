from django import forms
from .models import Image

class NameForm(forms.Form):
    first_name = forms.CharField(label='Your first name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"