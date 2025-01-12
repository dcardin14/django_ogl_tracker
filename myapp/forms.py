from django import forms
from django.forms import inlineformset_factory
from .models import OGL, MineralTract

class OGLForm(forms.ModelForm):
    class Meta:
        model = OGL
        fields = ['docNo', 'effDate', 'recDate', 'lessor', 'lessee', 'legal_desc', 'term_in_years', 'royalty']

    def clean_docNo(self):
        docNo = self.cleaned_data.get('docNo')
        if not docNo.isdigit() or len(docNo) != 10:
            raise forms.ValidationError("Document Number must be a 10-digit number.")
        return docNo

class MineralTractForm(forms.ModelForm):
    class Meta:
        model = MineralTract
        fields = '__all__'

class MineralTractBaseFormset(forms.BaseInlineFormSet):
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

MineralTractFormset = inlineformset_factory(OGL, MineralTract, form=MineralTractForm, formset=MineralTractBaseFormset, extra=1)
