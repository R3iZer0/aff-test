from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'last_name', 'email', 'phone', 'country']

    def save(self, commit=True):
        lead = super(LeadForm, self).save(commit=False)
        lead.name = self.cleaned_data['name']
        lead.last_name = self.cleaned_data['last_name']
        lead.email = self.cleaned_data['email']
        lead.phone = self.cleaned_data['phone']
        lead.country = self.cleaned_data['country']
        if commit:
            lead.save()
        return lead
