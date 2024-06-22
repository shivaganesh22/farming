from django import forms
from .models import FarmingDetails

class FarmingDetailsForm(forms.ModelForm):
    class Meta:
        model = FarmingDetails
        fields = [
            'farmer_name', 'pincode', 'aadhar_number', 'contact_number', 'acres_ploughed', 
            'season', 'crop_grown', 'seeds_used', 'date_seed_sown', 'transplanting', 
            'irrigation_method', 'fertilizers_used', 'date_harvesting', 'subfield', 
            'variety_used', 'quantity_used', 'irrigation_type', 'fertilizers_type'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
