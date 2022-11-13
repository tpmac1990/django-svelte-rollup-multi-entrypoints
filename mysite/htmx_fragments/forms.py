from django import forms
from .models import Image

from imagekit.forms import ProcessedImageField
from imagekit.processors import Transpose, Anchor, ResizeToFit

class NameForm(forms.Form):
    first_name = forms.CharField(label='Your first name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)

class ImageForm(forms.ModelForm):
    image = ProcessedImageField(spec_id='mysite:htmx_fragments:image',
                                processors=[
                                    Transpose(), # wipes meta to prevent rotation
                                    ResizeToFit(width=1920,height=1080,upscale=False,anchor=Anchor.CENTER),
                                ],
                                format='WEBP',
                                options={'quality': 75})
    class Meta:
        model = Image
        fields = "__all__"
