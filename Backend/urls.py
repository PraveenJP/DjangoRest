from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'student',StudentControl,base_name='student')

urlpatterns=[
	url(r'^',include(router.urls),name='index')
]