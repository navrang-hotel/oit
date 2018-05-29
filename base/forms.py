# ==============================
# Addede by developer after this
# ==============================

from django import forms

from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    """Class for contact message model form."""

    # Add class style, and html attributes to sender_name textinput widget
    sender_name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':"form-control",
                'id':'sname',
                'name':'sname',
                'placeholder':'Name',
                'type': 'text',
            }
        )
    )

    # Add class style, and html attributes to sender_email textinput widget
    sender_email = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':"form-control",
                'id':'email',
                'name':'email',
                'placeholder':'Email',
                'type': 'email',
            }
        )
    )

    # Add class style, and html attributes to message textarea widget
    message = forms.CharField(
    # ^ ?But this is text field?
        widget=forms.Textarea(
            attrs = {
                'class':"form-control",
                'id':'comments',
                'name':'comments',
                'placeholder':'Message',
                'rows':'5',
            }
        )
    )

    class Meta:
        model = ContactMessage
        fields = [
            'sender_name',
            'sender_email',
            'message',
        ]

