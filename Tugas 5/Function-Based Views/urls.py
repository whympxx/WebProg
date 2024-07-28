from django.urls import path
from .views import update_personal_data, delete_personal_data

urlpatterns = [
    path('personaldata/<int:pk>/update/', update_personal_data, name='personaldata_update'),
    path('personaldata/<int:pk>/delete/', delete_personal_data, name='personaldata_delete'),
]
