from django.shortcuts import render
from .models import Automotriz, ModeloCarro
from django.views.generic import CreateView, ListView,  UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class AutomotrizCreateView(CreateView):
    model = Automotriz
    #form_class = AutomotizForm
    fields = '__all__'
    template_name = 'automotriz_form.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['modelos'] = ModeloCarro.objects.all()
        return context
    

        