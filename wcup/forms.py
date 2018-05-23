# =============================
# Added by developer after this
# =============================

from django import forms

class PlayerForm(forms.Form):
    player_first_name = forms.CharField(label='Player first name', max_length=100)
    player_last_name = forms.CharField(label='Player last name', max_length=100)

