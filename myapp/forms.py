from django import forms
from django.forms import inlineformset_factory
from .models import OGL, MineralTract

class OGLForm(forms.ModelForm):
    class Meta:
        model = OGL
        fields = ['docNo', 'effDate', 'recDate', 'lessor', 'lessee', 'legal_desc', 'term_in_years', 'royalty']

# Create an inline formset for MineralTract
MineralTractFormset = inlineformset_factory(
    OGL,  # Parent model
    MineralTract,  # Related model
    fields=['township', 'range', 'section', 'desc', 'gross', 'owner', 'percent', 'net'],  # Fields to display
    extra=1,  # Number of empty forms displayed initially
    can_delete=True  # Allow users to delete related items
)

class MineralTractForm(forms.ModelForm):
    class Meta:
        model = MineralTract
        fields = [ 'township', 'range', 'section', 'desc', 'gross', 'owner', 'percent', 'net']
