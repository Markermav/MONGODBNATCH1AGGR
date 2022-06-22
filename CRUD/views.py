from functools import partial
import http
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import status

from rest_framework.decorators import api_view

from django.db.models import Avg, Min, Max, Sum, Count

from django.db.models import Q

from .models import *
from .serializers import *
import math
# Create your views here.





@api_view(['GET'])
def home(request):
    return HttpResponse('Hi')


@api_view(['GET'])
def getAll(request, format=None):
    p = People.objects.all()
    serializeData = PeopleSerializer(p, many=True)
    return Response(serializeData.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createPeople(request):
    s  = PeopleSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED) 
    return Response({'message':'People obj creation failed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def people_details(request, id):
    try:
        p = People.objects.get(pk=id)
    except People.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  


    if request.method == 'GET':
        s = PeopleSerializer(p)
        return Response(s.data)


    elif request.method == 'PUT':
        putData = PeopleSerializer(p, data=request.data)
        if putData.is_valid():
            putData.save()
            return Response(putData.data)
        return Response (putData.errors, status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == 'DELETE':
        p.delete()
        return Response({'message': 'Item deleted'}, status=status.HTTP_200_OK)



@api_view(['GET'])
def aggregate_people(request):

    people = People.objects.all()

    average = people.aggregate(Avg('familymembers'))
    count = people.aggregate(Count('familymembers'))
    sum = people.aggregate(Sum('familymembers'))
    min = people.aggregate(Min('familymembers'))
    max = people.aggregate(Max('familymembers'))


    return Response({'average': average["familymembers__avg"], 
    'Total Count': count[ "familymembers__count"],
    'Sum': sum["familymembers__sum"],
    'Minimum Value': min[ "familymembers__min"],
    'Maximum Value': max["familymembers__max"]
    }, status=status.HTTP_206_PARTIAL_CONTENT)



@api_view(['GET'])
def search_api(request):

    searchVar = request.GET.get('search')

    sortVar = request.GET.get('sort')

    people = People.objects.all()

    if searchVar:
        people = people.filter(Q(name__icontains = searchVar) | Q(desc__icontains = searchVar)  )

    if sortVar == 'asc':
        people = people.order_by('familymembers')

    elif sortVar == 'desc':
        people = people.order_by('-familymembers')    


    serilizedata = PeopleSerializer(people, many=True)

    return Response(serilizedata.data)



