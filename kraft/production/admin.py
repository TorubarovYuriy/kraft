from django.contrib import admin
from .models import (
    Machine, Order, Roll, Clue, Work, Marriage, Box, WorkingShift,
    MarriageCount,
)

admin.site.empty_value_display = 'Не задано'


class OrderAdmin(admin.ModelAdmin):
    """
    Docstring для OrderAdmin
    Вспомогательные настройки для модели Order
    """
    list_display = ('name', 'count')


class RollAdmin(admin.ModelAdmin):
    """
    Docstring для RollAdmin
    Вспомогательные настройки для модели Roll
    """
    list_display = (
        'number', 'weight', 'order'
    )
    list_editable = ('weight',)


class MarriageInline(admin.TabularInline):
    """
    Docstring для MarriageInline
    Модель для отображения в WorkingShiftAdmin
    """
    model = MarriageCount
    extra = 0


class WorkingShiftAdmin(admin.ModelAdmin):
    """
    Docstring для WorkingShiftAdmin
    Вспомогательные настройки для модели WorkingShift
    """
    inlines = (MarriageInline,)
    list_display = (
        'date', 'machine', 'plan', 'done',
    )
    list_editable = (
        'done',
    )
    filter_horizontal = ('users', 'rolls', 'work')


class MarriageCountAdmin(admin.ModelAdmin):
    """
    Docstring для MarriageCountAdmin
    Вспомогательные настройки для модели MarriageCount
    """
    list_display = (
        'working_shift', 'marriage', 'count_pieces', 'count_weight'
    )


admin.site.register(
    [Machine, Clue, Work, Marriage, Box]
)

admin.site.register(Order, OrderAdmin)
admin.site.register(Roll, RollAdmin)
admin.site.register(WorkingShift, WorkingShiftAdmin)
admin.site.register(MarriageCount, MarriageCountAdmin)
admin.site.site_header = 'Администрирование сайта'
admin.site.site_title = 'Администрирование'
