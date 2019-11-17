from django import forms

from .models import Pet


class PetRegistrationForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = (
            'image', 'name', 'pet_type', 'breed', 'gender', 'son', 'weight', 'coat','birthday', 'allergies_notes',
            'notes', 'vaccine', 'allergies', 'anal_gland', 'arthirits', 'blind', 'trachea','deaf', 'diabetic', 'standing',
            'epileptic', 'heart', 'hip', 'hot', 'incontinence', 'kidney', 'moles','pancreatitis', 'ear', 'skin', 'tooth', 'tumors',
            'anxiety', 'cage', 'clippers', 'dryer', 'nail', 'water', 'shedding', 'hernia','energy', 'biting', 'leash', 'soiler', 'prefumes',
            'photo', 'animal', 'people', 'clipper_burn', 'senior', 'table', 'team', 'chew','timid', 'barker'
            )
class PetUpdateForm(forms.ModelForm):

    class Meta:

        model = Pet
        fields = (
        'image', 'name', 'pet_type', 'breed', 'gender', 'son', 'weight', 'coat','birthday', 'allergies_notes',
        'notes', 'vaccine', 'allergies', 'anal_gland', 'arthirits', 'blind', 'trachea','deaf', 'diabetic', 'standing',
        'epileptic', 'heart', 'hip', 'hot', 'incontinence', 'kidney', 'moles','pancreatitis', 'ear', 'skin', 'tooth', 'tumors',
        'anxiety', 'cage', 'clippers', 'dryer', 'nail', 'water', 'shedding', 'hernia','energy', 'biting', 'leash', 'soiler', 'prefumes',
        'photo', 'animal', 'people', 'clipper_burn', 'senior', 'table', 'team', 'chew','timid', 'barker'
    )
