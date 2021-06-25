from django.urls import path
from .views import (
  BandListView,
  BandDetailView,
  BandCreateView,
  BandUpdateView,
  BandDeleteView
)

urlpatterns = [
  path('', BandListView.as_view(), name='band_list'),
  path('<int:pk>/', BandDetailView.as_view(), name='band_detail'),
  path('create/', BandCreateView.as_view(), name='band_create'),
  path('<int:pk>/update/', BandUpdateView.as_view(), name='band_update'),
  path('<int:pk>/delete/', BandDeleteView.as_view(), name='band_delete')
]