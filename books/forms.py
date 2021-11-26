from django import forms
from .models import BookInfo

class BookForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = BookInfo
        fields = '__all__'