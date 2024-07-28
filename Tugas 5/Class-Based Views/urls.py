from django.urls import path
from .views import PersonalDataUpdateView, PersonalDataDeleteView

urlpatterns = [
    path('personaldata/<int:pk>/update/', PersonalDataUpdateView.as_view(), name='personaldata_update'),
    path('personaldata/<int:pk>/delete/', PersonalDataDeleteView.as_view(), name='personaldata_delete'),
]
