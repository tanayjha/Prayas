from django import forms
from main.models import *

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = students
        exclude = []

    def __init__(self, *args, **kwargs):
                    self.user_cache = None
                    super(CreateStudentForm, self).__init__(*args, **kwargs)
    def clean(self):
        name = self.cleaned_data.get('name')
       
        rollNo = self.cleaned_data.get('rollNo')
       
        address = self.cleaned_data.get('address')

        isActive = self.cleaned_data.get('isActive')

        guardianName = self.cleaned_data.get('guardianName')

        guardianPhone = self.cleaned_data.get('guardianPhone')
        if len(str(guardianPhone)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter a valid 10 digit phone number')

        guardiansRelationWithChild = self.cleaned_data.get('guardiansRelationWithChild')

        referenceName = self.cleaned_data.get('referenceName')
        
        referencePhone = self.cleaned_data.get('referencePhone')
        if len(str(referencePhone)) == 10:
            pass
        else:
            raise forms.ValidationError('Enter a valid 10 digit phone number')        

        referenceAddress = self.cleaned_data.get('referenceAddress')
        
        joiningDate = self.cleaned_data.get('joiningDate')
        return self.cleaned_data
    def get_user(self):
        return self.user_cache
    