from django import forms

class PostForm(forms.Form):
    image = forms.ImageField(label="Image")
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Content", max_length=1000)
    rate = forms.IntegerField(label="Rate")