"""
URL configuration for webwakeonlan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from machines.views import (
    list_machines,
    new_machine,
    edit_machine,
    delete_machine,
    awake_machine,
    refresh_machine,
)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", list_machines, name="list_machines"),
    path("new/", new_machine, name="new_machine"),
    path("edit/<int:pk>/", edit_machine, name="edit_machine"),
    path("delete/<int:pk>/", delete_machine, name="delete_machine"),
    path("awake/<int:pk>/", awake_machine, name="awake_machine"),
    path("refresh/<int:pk>/", refresh_machine, name="refresh_machine"),
]
