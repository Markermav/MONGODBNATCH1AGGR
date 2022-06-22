from django.urls import include, path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name = 'home'),

    path('fetchall', views.getAll, name='getAll'),

    path('create', views.createPeople, name='createPeople'),


    path('people/<int:id>', views.people_details, name='people_details'),

    path('agr', views.aggregate_people, name='agr'),

    path('operation', views.search_api, name='operation'),




]

urlpatterns = format_suffix_patterns(urlpatterns)
