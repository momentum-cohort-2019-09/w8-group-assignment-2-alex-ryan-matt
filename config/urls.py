"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from flipasaurus import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'card', views.CardViewSet)
router.register(r'deck', views.DeckViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.dashboard, name='dashboard'),
    path('flipasaurus/create_deck/', views.create_deck, name='create_deck'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('flipasaurus/<int:pk>/delete', views.delete_card, name='delete_card'),
    path('flipasaurus/<int:pk>/edit_deck', views.edit_deck, name='edit_deck'),
    path('flipasaurus/<int:pk>/delete_deck', views.delete_deck, name='delete_deck'),
    path('flipasaurus/<int:pk>/edit/', views.edit_card, name="edit_card"),
    path('flipasaurus/<int:pk>/view_deck', views.view_deck, name="view_deck")
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
