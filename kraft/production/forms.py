from django import forms
from .models import WorkingShift


class WorkingShiftForm(forms.ModelForm):
    """Форма для создания и редактирования рабочей смены."""

    class Meta:
        model = WorkingShift
        # Указываем поля, которые будут в форме
        fields = [
            'date', 'machine', 'order', 'users', 'work', 'rolls',
            'plan', 'done', 'box', 'count_box', 'clue', 'count_clue',
            'time_start', 'time_end'
        ]
        # Используем виджеты для более удобного ввода данных
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
            # Для полей ManyToMany используем CheckboxSelectMultiple
            # для наглядного выбора нескольких вариантов
            'users': forms.CheckboxSelectMultiple(),
            'work': forms.CheckboxSelectMultiple(),
            'rolls': forms.CheckboxSelectMultiple(),
            # Для остальных полей можно оставить виджеты по умолчанию
            # или добавить им класс для стилизации
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
        # Поле 'rolls' может содержать много записей,
        # сделаем его необязательным
        # для более удобного начального создания смены.
        # Рулоны можно будет добавить позже на странице редактирования.
        self.fields['rolls'].required = False


class WorkingShiftEditForm(forms.ModelForm):
    """Форма для редактирования рабочей смены."""

    class Meta:
        model = WorkingShift
        # Указываем поля, которые будут в форме
        fields = [
            'date', 'machine', 'order', 'users', 'work', 'rolls',
            'plan', 'done', 'box', 'count_box', 'clue', 'count_clue',
            'time_start', 'time_end'
        ]
        # Используем виджеты для более удобного ввода данных
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
            # Для полей ManyToMany используем CheckboxSelectMultiple
            # для наглядного выбора нескольких вариантов
            'users': forms.CheckboxSelectMultiple(),
            'work': forms.CheckboxSelectMultiple(),
            'rolls': forms.CheckboxSelectMultiple(),
            # Для остальных полей можно оставить виджеты по умолчанию
            # или добавить им класс для стилизации
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'plan': forms.NumberInput(attrs={'class': 'form-control'}),
            'done': forms.NumberInput(attrs={'class': 'form-control'}),
            'box': forms.Select(attrs={'class': 'form-control'}),
            'count_box': forms.NumberInput(attrs={'class': 'form-control'}),
            'clue': forms.Select(attrs={'class': 'form-control'}),
            'count_clue': forms.NumberInput(attrs={'class': 'form-control'}),
        }
