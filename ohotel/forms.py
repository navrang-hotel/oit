# =============================
# Added by developer after this
# =============================

from django import forms

class BookingFormStaff(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    customer = forms.CharField(max_length=100)
    number_of_people = forms.IntegerField()

class BlogCommentForm(forms.Form):
    comment_body = forms.CharField(label='Comment', widget=forms.Textarea) 

