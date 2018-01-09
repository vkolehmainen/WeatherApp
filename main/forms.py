from django import forms
from main.models import Observation

class ObservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ObservationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    temperature = forms.FloatField(min_value=-100.0, max_value=100)
    time = forms.DateTimeField(input_formats = ['%m/%d/%Y %H:%M'])

    class Meta:
        model = Observation
        fields = ('city', 'time', 'temperature', 'weather_type')
        labels = {
            'city': 'City',
            'time': 'Time',
            'temperature': 'Temperature (Celsius)',
            'weather_type' : 'Weather type'
        }
