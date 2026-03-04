from typing import Any
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.forms import inlineformset_factory

from .models import Clue, Machine, Order, WorkingShift, ImageShiftAct
from .forms import WorkingShiftForm, WorkingShiftEditForm, ImageShiftActForm


ImageFormSet = inlineformset_factory(
    WorkingShift,
    ImageShiftAct,
    form=ImageShiftActForm,
    extra=3,
    can_delete=True,
)


class ProductionMainView(TemplateView):
    """Отображает главную страницу приложения 'production'."""
    template_name = 'production/about.html'
    form_class = WorkingShiftEditForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Производство'
        return context


class MachineListView(ListView):
    model = Machine
    template_name = 'production/machine.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['machines'] = Machine.objects.all()
        return context


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'production/machine_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context


class OrderListView(ListView):
    model = Order
    template_name = 'production/order.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all().order_by('-name')
        return context


class OrderDetailView(DetailView):
    model = Order
    template_name = 'production/order_detail.html'


class ClueListView(ListView):
    model = Clue
    template_name = 'production/clue.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['clues'] = Clue.objects.all()
        return context


class ClueDetailView(DetailView):
    model = Clue


class WorkingShiftListView(ListView):
    model = WorkingShift
    template_name = 'production/working_shift.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['working_shifts'] = WorkingShift.objects.all()
        context['images'] = ImageShiftAct.objects.all()
        return context

# ******************


def working_shift_create(request):
    """Представление для создания новой рабочей смены."""
    if request.method == 'POST':
        form = WorkingShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('production:working_shift')
    else:
        form = WorkingShiftForm()

    context = {
        'form': form,
        'title': 'Добавление новой смены'
    }
    return render(request, 'production/working_shift_form.html', context)


# Вы также можете создать view для редактирования
def working_shift_edit(request, pk):
    """Представление для редактирования существующей смены."""
    shift = get_object_or_404(WorkingShift, pk=pk)
    if request.method == 'POST':
        form = WorkingShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect('production:working_shift')
    else:
        form = WorkingShiftForm(instance=shift)

    context = {
        'form': form,
        'title': f'Редактирование смены от {shift.date}',
        'is_edit': True
    }
    return render(request, 'production/working_shift_form.html', context)


def create_object(request):
    if request.method == 'POST':
        form = WorkingShiftForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            obj = form.save()
            formset.instance = obj
            formset.save()
            return redirect('object_detail', pk=obj.pk)
    else:
        form = WorkingShiftForm()
        formset = ImageFormSet()

    return render(
        request,
        'production/create_object.html',
        {'form': form, 'formset': formset}
    )


def object_detail(request, pk):
    obj = get_object_or_404(WorkingShift, pk=pk)
    return render(request, 'production/detail_object.html', {'object': obj})
