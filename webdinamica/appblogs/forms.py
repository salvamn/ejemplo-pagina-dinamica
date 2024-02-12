from django import forms
from ckeditor.widgets import CKEditorWidget


class FormularioPost(forms.Form):
    titulo = forms.CharField(required=True)
    contenido_del_post = forms.CharField(widget=CKEditorWidget(), required=True)
    imagen = forms.ImageField(required=False)
