from django.shortcuts import render, get_object_or_404, redirect
from models import PersonalData
from forms import PersonalDataForm

def update_personal_data(request, pk):
    personal_data = get_object_or_404(PersonalData, pk=pk)
    if request.method == "POST":
        form = PersonalDataForm(request.POST, instance=personal_data)
        if form.is_valid():
            form.save()
            return redirect('personaldata_list')
    else:
        form = PersonalDataForm(instance=personal_data)
    return render(request, 'personaldata_form.html', {'form': form})

def delete_personal_data(request, pk):
    personal_data = get_object_or_404(PersonalData, pk=pk)
    if request.method == "POST":
        personal_data.delete()
        return redirect('personaldata_list')
    return render(request, 'personaldata_confirm_delete.html', {'object': personal_data})

