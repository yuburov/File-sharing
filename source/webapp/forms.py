from django import forms
from webapp.models import File


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ['author']