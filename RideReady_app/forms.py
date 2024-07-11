from django import forms
from .models import profile1

class cus_form(forms.ModelForm):
    class Meta:
        model = profile1
        fields = ["fnameName","fathernName","Occupation"]