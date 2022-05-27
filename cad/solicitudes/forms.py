from django.forms import *
from cad.solicitudes.models import *


class SolicitudesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['customer'].widget.attrs['autofocus'] = True
        self.fields['date_inicio'].input_formats = ['%d/%m/%Y %H:%M']
        self.fields['date_joined'].widget.attrs['readonly'] = True

    class Meta:
        model = solicitudes
        fields = '__all__'
        widgets = {
            'num': TextInput(
                attrs={
                    'placeholder': 'Numero de Contrato',
                    'type': 'number', 'rows': 3, 'cols': 3
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Escribir Descripcion',
                }
            ),
            'date_final': DateTimeInput(format='%d-%m-%Y %H:%M', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'date_final',
                'value': datetime.now().strftime('%d-%m-%Y %H:%M'),
                'data-toggle': 'datetimepicker',
                'data-target': '#date_final'
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
