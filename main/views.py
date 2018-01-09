from django.shortcuts import render
from main.forms import ObservationForm

def map(request):
    return render(request, 'map.html')

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

    return render(request,
            'map.html',
            {'observationform': observationform})
