from django import forms

class createForm(forms.Form):
    pic = forms.ImageField(label="photo")