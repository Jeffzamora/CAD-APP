from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from cad.extraccion.forms import ExtraForm
from cad.extraccion.models import *


class ExtraListView(ListView):
    model = extraccion
    template_name = 'extracciones/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = extraccion.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Extracciones'
        context['create_url'] = reverse_lazy('cad:extra_create')
        context['list_url'] = reverse_lazy('cad:extra_list')
        context['entity'] = 'Extracciones'
        return context


class ExtraCreateView(CreateView):
    model = extraccion
    form_class = ExtraForm
    template_name = 'extracciones/create.html'
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
        context['title'] = 'Crear Un Extraccion'
        context['entity'] = 'Extraccion'
        context['list_url'] = reverse_lazy('cad:extra_list')
        context['action'] = 'add'
        return context


class ExtraUpdateView(UpdateView):
    model = extraccion
    form_class = ExtraForm
    template_name = 'extracciones/create.html'
    success_url = reverse_lazy('cad:extra_list')

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
        context['title'] = 'Editar una extraccion'
        context['entity'] = 'Extracciones'
        context['list_url'] = reverse_lazy('cad:extra_list')
        context['action'] = 'edit'
        return context


class ExtraDeleteView(DeleteView):
    model = extraccion
    template_name = 'extracciones/delete.html'
    success_url = reverse_lazy('cad:extra_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Extraccion'
        context['entity'] = 'Extracciones'
        context['list_url'] = reverse_lazy('cad:extra_list')
        return context
