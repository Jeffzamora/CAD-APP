from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from cad.solicitudes.forms import SolicitudesForm
from cad.solicitudes.models import *


class SolicitudesListView(ListView):
    model = solicitudes
    template_name = 'solicitudes/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = solicitudes.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Solicitudes'
        context['create_url'] = reverse_lazy('cad:solicitudes_create')
        context['list_url'] = reverse_lazy('cad:solicitudes_list')
        context['entity'] = 'Solicitudes'
        return context


class SolicitudesCreateView(CreateView):
    model = solicitudes
    form_class = SolicitudesForm
    template_name = 'solicitudes/create.html'
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
        context['title'] = 'Crear una Solicitud'
        context['entity'] = 'Solicitud'
        context['list_url'] = reverse_lazy('cad:solicitudes_list')
        context['action'] = 'add'
        return context


class SolicitudesUpdateView(UpdateView):
    model = solicitudes
    form_class = SolicitudesForm
    template_name = 'solicitudes/create.html'
    success_url = reverse_lazy('cad:solicitudes_list')

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
        context['title'] = 'Editar una Solicitud'
        context['entity'] = 'Solicitudes'
        context['list_url'] = reverse_lazy('cad:solicitudes_list')
        context['action'] = 'edit'
        return context


class SolicitudesDeleteView(DeleteView):
    model = solicitudes
    template_name = 'solicitudes/delete.html'
    success_url = reverse_lazy('cad:solicitudes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Solicitud'
        context['entity'] = 'Solicitudes'
        context['list_url'] = reverse_lazy('cad:solicitudes_list')
        return context
