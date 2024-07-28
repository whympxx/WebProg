from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import PersonalData

class PersonalDataUpdateView(UpdateView):
    model = PersonalData
    fields = ['name', 'age', 'email']
    template_name = 'personaldata_form.html'
    success_url = reverse_lazy('personaldata_list')

from django.views.generic.edit import DeleteView
from .models import PersonalData

class PersonalDataDeleteView(DeleteView):                            
    model = PersonalData
    template_name = 'personaldata_confirm_delete.html'
    success_url = reverse_lazy('personaldata_list')
