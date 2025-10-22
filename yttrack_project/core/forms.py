from django import forms
from .models import Quadro

class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadro
        fields = ['nome', 'cover_color', 'descricao']
        widgets = {
            'cover_color': forms.TextInput(attrs={'placeholder': '#ff7a7a ou linear-gradient(...)'}),
            'descricao': forms.Textarea(attrs={'rows':3}),
        }
