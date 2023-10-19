from django import forms

from .models import Mybooksread

class BookForm(forms.ModelForm):


    class Meta:
        model = Mybooksread
        fields = ('book_title','authors','image','comment','category',)

        
        
        