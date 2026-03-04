from django import forms
from .models import WorkingShift, ImageShiftAct


class WorkingShiftForm(forms.ModelForm):
    """Форма для создания и редактирования рабочей смены."""

    class Meta:
        model = WorkingShift
        fields = [
            'date', 'machine', 'order', 'users', 'work', 'rolls',
            'plan', 'done', 'box', 'count_box', 'clue', 'count_clue',
            'time_start', 'time_end'
        ]
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'time_start': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'time_end': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'users': forms.CheckboxSelectMultiple(),
            'work': forms.CheckboxSelectMultiple(),
            'rolls': forms.CheckboxSelectMultiple(),
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'plan': forms.NumberInput(attrs={'class': 'form-control'}),
            'done': forms.NumberInput(attrs={'class': 'form-control'}),
            'box': forms.Select(attrs={'class': 'form-control'}),
            'count_box': forms.NumberInput(attrs={'class': 'form-control'}),
            'clue': forms.Select(attrs={'class': 'form-control'}),
            'count_clue': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rolls'].required = False


class WorkingShiftEditForm(forms.ModelForm):
    """Форма для редактирования рабочей смены."""

    class Meta:
        model = WorkingShift
        fields = [
            'date', 'machine', 'order', 'users', 'work', 'rolls',
            'plan', 'done', 'box', 'count_box', 'clue', 'count_clue',
            'time_start', 'time_end'
        ]
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'time_start': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'time_end': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'users': forms.CheckboxSelectMultiple(),
            'work': forms.CheckboxSelectMultiple(),
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'plan': forms.NumberInput(attrs={'class': 'form-control'}),
            'done': forms.NumberInput(attrs={'class': 'form-control'}),
            'box': forms.Select(attrs={'class': 'form-control'}),
            'count_box': forms.NumberInput(attrs={'class': 'form-control'}),
            'clue': forms.Select(attrs={'class': 'form-control'}),
            'count_clue': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ImageShiftActForm(forms.ModelForm):
    """Форма для загрузки изображений для акта смены."""

    class Meta:
        model = ImageShiftAct
        fields = ('image', 'title')


class ImageShiftActFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        images_count = sum(
            1 for form in self.forms if not form.cleaned_data.get('DELETE')
        )
        if images_count < 2:
            raise forms.ValidationError('Добавьте минимум 2 изображения.')
