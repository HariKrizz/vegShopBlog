from django.urls import path
from shopApp import views

urlpatterns = [
    path('',views.vegIndex,name='index'),
    path('veggies/',views.vegHome,name='home'),
    path('veggies/<int:v_id>',views.vegDetails,name='details'),
    path('addVeg/',views.addVeg,name='add'),
    path('update/<int:v_id>',views.updateVeg,name='update'),
    path('delete/<int:v_id>',views.deleteVeg,name='delete')
]