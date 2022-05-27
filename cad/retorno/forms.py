from django.forms import *
from cad.retorno.models import *


class RetornoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['customer'].widget.attrs['autofocus'] = True
        self.fields['date_joined'].widget.attrs['readonly'] = True

    class Meta:
        model = retorno
        fields = '__all__'
        widgets = {
            'num': TextInput(
                attrs={
                    'placeholder': 'Numero de Contrato',
                    'type': 'number',
                    'rows': 6,
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Escribir Descripcion',
                }
            ),
            'date_inicio': DateTimeInput(
                attrs={
                    'type': 'date',
                }
            ),
            'date_final': DateTimeInput(
                attrs={
                    'type': 'date',
                }
            ),
            'active': CheckboxInput(
                attrs={
                    'type': 'checkbox',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
