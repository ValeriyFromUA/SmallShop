from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView

from shop.models import Items


class ShopView(ListView):
    template_name = "shop.html"
    model = Items
    context_object_name = "items"
    ordering = ["-id"]

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by', '-price')

        if sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort_by == 'date_asc':
            queryset = queryset.order_by('created_at')
        elif sort_by == 'date_desc':
            queryset = queryset.order_by('-created_at')

        return queryset


class ItemDetailView(DetailView):
    template_name = "item.html"
    model = Items
    context_object_name = "item"


class AboutView(TemplateView):
    template_name = "about.html"
