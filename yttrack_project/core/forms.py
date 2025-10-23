from django import forms
from .models import Quadro
from .models import Video


class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadro
        fields = ['nome', 'cover_color', 'descricao']
        widgets = {
            'cover_color': forms.TextInput(attrs={'placeholder': '#ff7a7a ou linear-gradient(...)'}),
            'descricao': forms.Textarea(attrs={'rows':3}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'video_arquivo', 'video_link', 'thumbnail']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
