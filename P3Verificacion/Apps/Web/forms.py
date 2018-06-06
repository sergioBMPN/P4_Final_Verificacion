from django import forms


class formulario(forms.Form):
    pagina = forms.CharField(widget=forms.TextInput, label='Introduce la URL:')
    dia_consultar = forms.CharField(widget=forms.TextInput, label='Introduce el dia y mes para consultar en BBDD(Ej: 8_1):')
