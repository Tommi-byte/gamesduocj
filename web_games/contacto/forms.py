from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Su nombre", required=True
    , min_length=3, max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control mb-3', 'placeholder':'ingrese su nombre'}))
    correo = forms.EmailField(label="Su correo", required=True, widget=forms.EmailInput
    (attrs={'class':'form-control mb-3','placeholder':'Ingrese su correo'}))
    mensaje = forms.CharField(label="Su mensaje", required= True, min_length=10,
    max_length=1000, widget=forms.Textarea(attrs={'class':'form-control mb-3','placeholder':'Ingrese su mensaje','rows':3}))