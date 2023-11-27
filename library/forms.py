from django import forms
class BookCreateForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price=forms.IntegerField()
    category=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
