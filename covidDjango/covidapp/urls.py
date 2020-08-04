from django.urls import path
from rest_framework import routers, serializers, viewsets
from . import views
from covidapp.models import State, District
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import *

# Local
LOCAL_NUMBER="8888337754"
RASA_URL = "http://127.0.0.1:5105"
uri = "http://localhost:8000"
LOG_FILE = "./logs/rasa_renee.log"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    url('users/', include(router.urls)),
    path('', views.index, name='index'),
    # path('states/<int:state_id>/', views.statedetail, name='statedetail'),
    path('states/<state_name>/confirmedcases', statedetailconfirmedcases.as_view(), name='statedetailconfirmedcases'),
    path('states/<state_name>/activecases', statedetailactivecases.as_view(), name='statedetailactivecases'),
    path('states/<state_name>/deadcases', statedetaildeadcases.as_view(), name='statedetaildeadcases'),
    path('states/<state_name>/recoveredcases', statedetailrecoveredcases.as_view(), name='statedetailrecoveredcases'),
    path('districts/<district_name>/confirmedcases', districtdetailconfirmedcases.as_view(), name='districtdetailconfirmedcases'),
    path('districts/<district_name>/activecases', districtdetailactivecases.as_view(), name='districtdetailactivecases'),
    path('districts/<district_name>/deadcases', districtdetaildeadcases.as_view(), name='districtdetaildeadcases'),
    path('districts/<district_name>/recoveredcases', districtdetailrecoveredcases.as_view(), name='districtdetailrecoveredcases'),
]
