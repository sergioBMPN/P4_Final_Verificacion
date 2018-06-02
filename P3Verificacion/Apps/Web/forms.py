from django import forms


class formulario(forms.Form):
    pagina = forms.CharField(widget=forms.TextInput, label='Introduce la URL:')
