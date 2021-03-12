from django import forms
from .models import Item


# value inside the () inherits the functionality of forms.ModelForm

class ItemForm(forms.ModelForm):
    # class meta - gives info about itself,
    # which model is going to be associated with
    class Meta:
        model = Item
        fields = ['name', 'done']
