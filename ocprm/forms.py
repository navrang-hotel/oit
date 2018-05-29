# ==============================
# Addede by developer after this
# ==============================

from django import forms

from .models import StartProjectRequest

class StartProjectRequestForm(forms.ModelForm):
    """Class for start project request model form."""

    #email = forms.EmailField(
    #    widget=forms.EmailInput(
    #        attrs = {
    #            'class':"form-control",
    #            'id':'email',
    #            'name':'email',
    #            'placeholder':'Email',
    #            'type': 'email',
    #        }
    #    )
    #)

    #project_type = forms.CharField(
    #    widget=forms.TextInput(
    #        attrs = {
    #            'class':"form-control",
    #            'id':'project_type',
    #            'name':'project_type',
    #            'placeholder':'Project Type',
    #            'type': 'text',
    #        }
    #    )
    #)

    #description = forms.CharField(
    #    widget=forms.Textarea(
    #        attrs = {
    #            'class':"form-control",
    #            'id':'description',
    #            'name':'description',
    #            'placeholder':'Description',
    #            'rows':'5',
    #        }
    #    )
    #)

    class Meta:
        model = StartProjectRequest
        fields = [
            'email',
            'project_type',
            'description',
        ]

