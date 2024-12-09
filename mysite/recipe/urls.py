from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ReciptView, CreateRecipeView, DetailRecipeView, UpdateRecipe

app_name = 'recipe'

urlpatterns = [
    path("", ReciptView.as_view(), name="index"),
    path("create_recipe/", CreateRecipeView.as_view(), name="create_recipe"),
    path("detail_recipe/<int:pk>/", DetailRecipeView.as_view(), name="detail_recipe"),
    path("update_recipe/<int:pk>/", UpdateRecipe.as_view(), name="update_recipe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
