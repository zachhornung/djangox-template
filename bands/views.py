from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)
from django.urls import reverse_lazy
from .models import Band

class BandListView(ListView):
  template_name = 'bands/band_list.html'
  model = Band
  
class BandDetailView(DetailView):
  template_name = 'bands/band_detail.html'
  model = Band
  
class BandCreateView(CreateView):
  template_name = 'bands/band_create.html'
  model = Band
  fields = ['name', 'members', 'reviewer', 'genre', 'rating']
  success_url = reverse_lazy('band_list')
  
class BandUpdateView(UpdateView):
  template_name = 'bands/band_update.html'
  model = Band
  fields = ['name', 'members', 'genre', 'rating']
  success_url = reverse_lazy('band_list')
  
class BandDeleteView(DeleteView):
  template_name = 'bands/band_delete.html'
  model = Band
  success_url = reverse_lazy('band_list')