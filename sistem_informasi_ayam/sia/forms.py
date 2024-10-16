from django import forms
from .models import Produks

class ProduksForm(forms.ModelForm):
    class Meta:
        model = Produks
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'kategori', 'stok', 'image']