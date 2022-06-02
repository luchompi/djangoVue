from django.urls import path as p
from . import views as v
from rest_framework.urlpatterns import format_suffix_patterns
app_name="empresa"

urlpatterns=[
#HTML urls
p('sedes/',v.SedeList.as_view(),name="sedeIndex"),
#API urls
p('api/v1.0/',v.SedeAPI.as_view()),
p('api/v1.0/<int:pk>',v.SedeAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
