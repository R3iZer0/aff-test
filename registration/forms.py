from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'last_name', 'email', 'phone','lost_amount','company']

    def save(self, commit=True):
        lead = super(LeadForm, self).save(commit=False)
        lead.name = self.cleaned_data['name']
        lead.last_name = self.cleaned_data['last_name']
        lead.email = self.cleaned_data['email']
        lead.phone = self.cleaned_data['phone']
        lead.lost_amount = self.cleaned_data['lost_amount']
        lead.company=self.cleaned_data['company']
        if commit:
            lead.save()
        return lead
