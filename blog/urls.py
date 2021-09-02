from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('specific',views.specific,name='specific'),
    path('menu',views.menu,name='menu'),
    path('specials',views.specials,name='specials'),
    path('meals',views.meals,name='meals'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about')
]
