from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(label='', max_length=100, required=False, )
