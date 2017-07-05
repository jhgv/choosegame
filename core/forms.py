from django import forms

from .models import UserPreference

class UserPreferenceForm(forms.ModelForm):

    class Meta:
        model = UserPreference
        fields = ("plataforma", "price" , "genre")
    plataforma = forms.CharField(max_length=120)
    price = forms.CharField(max_length=1)
    genre = forms.CharField(max_length=120)
