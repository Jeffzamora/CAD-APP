from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from cad.retorno.forms import RetornoForm
from cad.retorno.models import *


class RetornoListView(ListView):
    model = retorno
    template_name = 'retorno/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = retorno.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Retornos'
        context['create_url'] = reverse_lazy('cad:retorno_create')
        context['list_url'] = reverse_lazy('cad:retorno_list')
        context['entity'] = 'Retornos'
        return context


class RetornoCreateView(CreateView):
    model = retorno
    form_class = RetornoForm
    template_name = 'retorno/create.html'
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
        context['title'] = 'Crear un Retorno'
        context['entity'] = 'Retorno'
        context['list_url'] = reverse_lazy('cad:retorno_list')
        context['action'] = 'add'
        return context


class RetornoUpdateView(UpdateView):
    model = retorno
    form_class = RetornoForm
    template_name = 'retorno/create.html'
    success_url = reverse_lazy('cad:retorno_list')

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
        context['title'] = 'Editar un Retorno'
        context['entity'] = 'Retornos'
        context['list_url'] = reverse_lazy('cad:retorno_list')
        context['action'] = 'edit'
        return context


class RetornoDeleteView(DeleteView):
    model = retorno
    template_name = 'retorno/delete.html'
    success_url = reverse_lazy('cad:retorno_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Retorno'
        context['entity'] = 'Retornos'
        context['list_url'] = reverse_lazy('cad:retorno_list')
        return context
