from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Sample API')

router = DefaultRouter()
router.register(r'student',StudentControl,base_name='student')

urlpatterns=[
	url(r'^',include(router.urls),name='index'),
	url(r'^swagger/$', schema_view)
]