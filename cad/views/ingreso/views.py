from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from cad.ingreso.forms import IngresoForm
from cad.ingreso.models import *


class IngresoListView(ListView):
    model = ingreso
    template_name = 'ingreso/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = ingreso.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ingresos'
        context['create_url'] = reverse_lazy('cad:ingreso_create')
        context['list_url'] = reverse_lazy('cad:ingreso_list')
        context['entity'] = 'Ingresos'
        return context


class IngresoCreateView(CreateView):
    model = ingreso
    form_class = IngresoForm
    template_name = 'ingreso/create.html'
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
        context['title'] = 'Crear Un Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = reverse_lazy('cad:ingreso_list')
        context['action'] = 'add'
        return context


class IngresoUpdateView(UpdateView):
    model = ingreso
    form_class = IngresoForm
    template_name = 'ingreso/create.html'
    success_url = reverse_lazy('cad:ingreso_list')

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
        context['title'] = 'Editar un Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = reverse_lazy('cad:ingreso_list')
        context['action'] = 'edit'
        return context


class IngresoDeleteView(DeleteView):
    model = ingreso
    template_name = 'ingreso/delete.html'
    success_url = reverse_lazy('cad:ingreso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = reverse_lazy('cad:ingreso_list')
        return context
