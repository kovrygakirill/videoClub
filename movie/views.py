from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = self.model.objects.all()

        return context
