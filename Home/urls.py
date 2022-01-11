from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="result-index"),
    path('predict/',views.predict,name="result-predict"),
]
