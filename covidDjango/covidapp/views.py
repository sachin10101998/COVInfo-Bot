from django.shortcuts import render
from covidapp.models import State, District
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
from django.db import transaction
from rest_framework import viewsets
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Covid Bot API",
        default_version='v1',
        description="Covid bot statistics and hospital finder",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sachin.chopra@piri.ai"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
def index(request):
    return HttpResponse("Hello, world. You're at the covid app index.")

class statedetailconfirmedcases(APIView):
    """
    View Confirmed cases from state
    """

    def get(self, request, state_name):
        try:
            q=State.objects.get(state_name=state_name)
            t=q.confirmed_cases
            return HttpResponse(t)
        except: print("An exception occured while getting Confirmed Cases data from state")

class statedetailactivecases(APIView):
    """
    View Active Casesfrom state
    """

    def get(self, request, state_name):
        try:
            q=State.objects.get(state_name=state_name)
            t=q.active_cases
            return HttpResponse(t)
        except: print("an Exception occured while getting Active cases from state")


class statedetaildeadcases(APIView):
    """
    View Dead Cases by State
    """
    def get(self, request, state_name):
        try: 
            q=State.objects.get(state_name=state_name)
            t=q.dead_cases
            return HttpResponse(t)
        except: print("an Exception occured while geeting dead cases from state")

class statedetailrecoveredcases(APIView):
    """
    View Recovered Cases by State
    """

    def get(self, request, state_name):
        try:
            q=State.objects.get(state_name=state_name)
            t=q.confirmed_cases
            return HttpResponse(t)
        except: print("an Exception occured while getting recovered cases data from state")

class districtdetailconfirmedcases(APIView):
    """
    View Confirmed cases by District
    """
    def get(self, request, district_name):
        try:
            q=District.objects.get(district_name=district_name)
            t=q.confirmed_cases
            return HttpResponse(t)
        except: print("an Exception occurd while getting confirmed cases data from district")

class districtdetailactivecases(APIView):
    """
    View Active Cases by District
    """
    def get(self, request, district_name):
        try:
            q=District.objects.get(district_name=district_name)
            t=q.active_cases
            return HttpResponse(t)
        except: print("An Exception occured while getting active cases data from district")

class districtdetaildeadcases(APIView):
    """
    View Dead cases by District
    """
    def get(self, request, district_name):
        try:
            q=District.objects.get(district_name=district_name)
            t=q.dead_cases
            return HttpResponse(t)
        except: print("an Exception occured while getting dead cases data from District")

class districtdetailrecoveredcases(APIView):
    """
    View Recovered Cases by District
    """
    def get(self, request, district_name):
        try:
            q=District.objects.get(district_name=district_name)
            t=q.recovered_cases
            return HttpResponse(t)
        except: print("an Exception occured while getting recovered cases data from District")


