from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from .models import Recipe, Category


class ReciptView(ListView):
    queryset = Recipe.objects.order_by('?').select_related('category')[:5]
    template_name = 'recipe/index.html'


class DetailRecipeView(DetailView):
    template_name = 'recipe/detail_recipe.html'
    queryset = Recipe.objects.select_related('category')


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = 'name', 'description', 'steps', 'time', 'image', 'ingredients', 'category'
    template_name = 'recipe/create_recipe.html'
    success_url = reverse_lazy('recipe:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateRecipe(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = 'name', 'description', 'steps', 'time', 'image', 'ingredients', 'category'
    template_name = 'recipe/update_recipe.html'

    def get_success_url(self):
        return reverse_lazy('recipe:detail_recipe', kwargs={'pk': self.object.pk})

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        created_by_current_user = self.get_object.author == self.request.user
        return created_by_current_user
