app_name= 'myapp'
from .import views					
from django.urls import path
				
urlpatterns = [
    path('', views.index,name="index"),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add',views.create_item,name= 'create_item'),
]