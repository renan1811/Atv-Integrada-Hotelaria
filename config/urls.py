
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from hotelaria.views.quarto import QuartoViewSet


router = DefaultRouter()

router.register(r"quartos", QuartoViewSet)


urlpatterns = [
    path('', RedirectView.as_view(url="api/")),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

