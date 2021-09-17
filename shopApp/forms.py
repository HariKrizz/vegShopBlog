 
from django.forms.models import ModelForm
from .models import vegetables
from django.forms import TextInput

class vegForm(ModelForm):

    class Meta:
        model = vegetables
        fields= ['Name','Image','Quantity','Price']

        widgets = { 

            'Name' : TextInput(attrs={'class':'form-control',
                            'style': 'max-width: 300px;',
                            'placeholder':'Name'
                            }),
            'Quantity' : TextInput(attrs={'class':'form-control',
                            'style': 'max-width: 300px;',
                            'placeholder':'Quantity in kg'
                            }),
            'Price': TextInput(attrs={'class':'form-control',
                            'style': 'max-width: 300px;',
                            'placeholder':'Price'
                            })
        }