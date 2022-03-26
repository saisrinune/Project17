from django.urls import path
from.import views
app_name="Httpsessionapp"
urlpatterns = [
    path('',views.input,name='input',),
    path('add',views.add,name='add'),
    path('diplay',views.diplay,name='diplay')
    ]