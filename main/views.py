from django.shortcuts import render
from django.contrib import messages
from main.forms import ObservationForm
from main.models import Observation

def map(request):
    if request.method == 'POST':
        observationform = ObservationForm(data=request.POST)

        if observationform.is_valid():
            observation = observationform.save(commit=False)
            observation.save()
            messages.success(request, 'Observation added successfully!')

        else:
            print(observationform.errors)

    else:
        observationform = ObservationForm()

    observations = Observation.objects.all()

    return render(request,
            'map.html', {'observationform': observationform,
                         'observations' : observations})
