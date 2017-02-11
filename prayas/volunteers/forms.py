from django import forms
from main.models import *

class CreateVolunteerForm(forms.ModelForm):
    class Meta:
        model = volunteers
        exclude = []

    def __init__(self, *args, **kwargs):
                    self.user_cache = None
                    super(CreateVolunteerForm, self).__init__(*args, **kwargs)
    def clean(self):
        name = self.cleaned_data.get('name')
        collegeRollNo = self.cleaned_data.get('collegeRollNo')
        joiningDate = self.cleaned_data.get('joiningDate')
        email = self.cleaned_data.get('email')
        contactNo = self.cleaned_data.get('contactNo')

        if len(str(contactNo)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter a valid 10 digit phone number')

        return self.cleaned_data
    def get_user(self):
        return self.user_cache