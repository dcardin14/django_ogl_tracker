from django import forms
from django.forms import inlineformset_factory
from .models import OGL, MineralTract

class OGLForm(forms.ModelForm):
    class Meta:
        model = OGL
        fields = ['docNo', 'effDate', 'recDate', 'lessor', 'lessee', 'legal_desc', 'term_in_years', 'royalty']

from django.forms.models import BaseInlineFormSet, inlineformset_factory
from .models import OGL, MineralTract

class MineralTractBaseFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not any(form.cleaned_data.values()):  # Skip entirely blank forms
                continue
            if form.cleaned_data.get('DELETE', False):  # Skip forms marked for deletion
                continue
            # Add additional validation as needed
            if not form.cleaned_data.get('township') or not form.cleaned_data.get('range'):
                raise forms.ValidationError("All required fields must be filled out.")

MineralTractFormset = inlineformset_factory(
    OGL,
    MineralTract,
    fields=['township', 'range', 'section', 'desc', 'gross', 'owner', 'percent', 'net'],
    extra=0,  # No extra blank forms by default
    can_delete=True,
    formset=MineralTractBaseFormset,  # Use the custom formset class
)


class MineralTractForm(forms.ModelForm):
    class Meta:
        model = MineralTract
        fields = [ 'township', 'range', 'section', 'desc', 'gross', 'owner', 'percent', 'net']
