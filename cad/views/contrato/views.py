from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator

from cad.mixins import ValidatePermissionRequiredMixin
from cad.contrato.forms import ContratoForm
from cad.contrato.models import *


class ContratoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = contrato
    template_name = 'contrato/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = contrato.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Contratos'
        context['create_url'] = reverse_lazy('cad:contrato_create')
        context['list_url'] = reverse_lazy('cad:contrato_list')
        context['entity'] = 'Contratos'
        return context


class ContratoCreateView(CreateView):
    model = contrato
    form_class = ContratoForm
    template_name = 'contrato/create.html'
    success_url = reverse_lazy()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Un Contrato'
        context['entity'] = 'Contrato'
        context['list_url'] = reverse_lazy('cad:contrato_list')
        context['action'] = 'add'
        return context


class ContratoUpdateView(UpdateView):
    model = contrato
    form_class = ContratoForm
    template_name = 'contrato/create.html'
    success_url = reverse_lazy('cad:contrato_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('cad:cliente_list')
        context['action'] = 'edit'
        return context


class ContratoDeleteView(DeleteView):
    model = contrato
    template_name = 'contrato/delete.html'
    success_url = reverse_lazy('cad:contrato_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Contrato'
        context['entity'] = 'Contratos'
        context['list_url'] = reverse_lazy('cad:contrato_list')
        return context
