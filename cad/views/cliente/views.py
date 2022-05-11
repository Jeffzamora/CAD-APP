from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from cad.cliente.forms import clienteForm
from cad.cliente.models import *


class ClienteListView(ListView):
    model = Customer
    template_name = 'cliente/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Customer.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('cad:cliente_create')
        context['list_url'] = reverse_lazy('cad:cliente_list')
        context['entity'] = 'Clientes'
        return context


class ClienteCreateView(CreateView):
    model = Customer
    form_class = clienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy()

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
        context['title'] = 'Creacion de un Cliente'
        context['entity'] = 'Cliente'
        context['list_url'] = reverse_lazy('cad:cliente_list')
        context['action'] = 'add'
        return context


class ClienteUpdateView(UpdateView):
    model = Customer
    form_class = clienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('cad:cliente_list')

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


class ClienteDeleteView(DeleteView):
    model = Customer
    template_name = 'cliente/delete.html'
    success_url = reverse_lazy('cad:cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('cad:cliente_list')
        return context
