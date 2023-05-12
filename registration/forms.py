from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    EXPERIENCE_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No')
    )


    class Meta:
        model = Lead
        fields = ['name', 'last_name', 'email', 'phone','experience', 'country']

    def save(self, commit=True):
        lead = super(LeadForm, self).save(commit=False)
        lead.name = self.cleaned_data['name']
        lead.last_name = self.cleaned_data['last_name']
        lead.email = self.cleaned_data['email']
        lead.phone = self.cleaned_data['phone']
        lead.country = self.cleaned_data['country']
        lead.experience = self.cleaned_data['experience']
        if commit:
            lead.save()
        return lead
