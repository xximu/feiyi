from django.urls import path
from . import views
app_name = 'webpage'
urlpatterns = [
    path('introduce/', views.introduce, name='introduce'),
    path('exhibit/', views.exhibit, name='exhibit'),
    path('inheritor/inheritorChart/', views.InheritorChart, name='inheritorChart'),
    path('inheritor/traditionalSkill/', views.traditionalSkill, name='traditionalSkill'),
    path('inheritor/folkActivities/', views.folkActivities, name='folkActivities'),
    path('inheritor/operaAndMusic/', views.operaAndMusic, name='operaAndMusic'),
    path('vedio/', views.vedio, name='vedio'),
    path('ask/', views.ask, name='ask'),
    path('visualization/', views.visualization, name='visualization'),
    path('inheritor/knowledge/', views.kg_view, name='knowledge'),
]