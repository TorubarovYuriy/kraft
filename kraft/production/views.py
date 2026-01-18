from django.views.generic import DetailView, ListView, TemplateView

from .models import Clue, Machine, Order, WorkingShift


class ProductionMainView(TemplateView):
    """Отображает главную страницу приложения 'production'."""
    template_name = 'production/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = Machine.objects.all()
        context['orders'] = Order.objects.all()
        context['clues'] = Clue.objects.all()
        return context


class MachineListView(ListView):
    model = Machine
    template_name = 'production/machine.html'

    def get_context_data(self, **kwargs):
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


class OrderDetailView(DetailView):
    model = Order


class ClueListView(ListView):
    model = Clue


class ClueDetailView(DetailView):
    model = Clue


class WorkingShiftListView(ListView):
    model = WorkingShift
    template_name = 'production/working_shift.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['working_shifts'] = WorkingShift.objects.all()
        return context
