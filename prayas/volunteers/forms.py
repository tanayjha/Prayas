from django import forms
from main.models import *
import re

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
        if re.match("[0-9]*-[A-Z]*-[0-9]*",str(collegeRollNo)) == None:
            raise forms.ValidationError('Incorrect format of roll no.(Correct format: 111-CO-15)')

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


class SearchVolunteerForm(forms.Form):
    name = forms.CharField(help_text='Search Volunteer by Name')

    def __init__(self, *args, **kwargs):
                    self.user_cache = None
                    super(SearchVolunteerForm, self).__init__(*args, **kwargs)

    def clean(self):
        name = self.cleaned_data.get('name')

        return self.cleaned_data


class EditVolunteerForm(forms.ModelForm):
    class Meta:
        model = volunteers
        exclude = []

    def __init__(self, *args, **kwargs):
                    self.collegeRollNo = kwargs.pop('rollNo', None)
                    self.user = kwargs.pop('user',None)
                    self.user_cache = None
                    super(EditVolunteerForm, self).__init__(*args, **kwargs)

    def clean(self):
        name = self.cleaned_data.get('name')

        
        collegeRollNo = self.cleaned_data.get('collegeRollNo')

        if re.match("[0-9]*-[A-Z]*-[0-9]*",str(collegeRollNo)) == None:
            raise forms.ValidationError('Incorrect format of roll no.(Correct format: 111-CO-15)')
        joiningDate = self.cleaned_data.get('joiningDate')
        email = self.cleaned_data.get('email')
        contactNo = self.cleaned_data.get('contactNo')

        if len(str(contactNo)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter a valid 10 digit phone number')

        return self.cleaned_data