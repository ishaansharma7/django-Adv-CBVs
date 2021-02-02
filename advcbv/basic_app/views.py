from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.http import HttpResponse
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location') # fields must be given
    model = models.School
    template_name = 'basic_app/school_update_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal') # fields must be given
    model = models.School
    template_name = 'basic_app/school_update_form.html'

class SchoolDeleteView(DeleteView):
    context_object_name = 'school'
    model = models.School
    template_name = 'basic_app/school_delete.html'
    success_url = reverse_lazy('basic_app:list')

    