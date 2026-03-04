from django.contrib import admin
from .models import (
    Machine, Order, Roll, Clue, Work, Marriage, Box, WorkingShift,
    MarriageCount, ImageShiftAct
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
        'date', 'order', 'done',
    )
    list_editable = (
        'done',
    )
    filter_horizontal = ('users', 'rolls', 'work',)


class MarriageCountAdmin(admin.ModelAdmin):
    """
    Docstring для MarriageCountAdmin
    Вспомогательные настройки для модели MarriageCount
    """
    list_display = (
        'working_shift', 'marriage', 'count_pieces', 'count_weight'
    )


class ImageShiftActInline(admin.ModelAdmin):
    """
    Docstring для ImageShiftActInline
    Модель для отображения в WorkingShiftAdmin
    """
    list_display = (
        'image', 'working_shift'
    )
    search_fields = ('working_shift',)


admin.site.register(
    [Machine, Clue, Work, Marriage, Box]
)

admin.site.register(Order, OrderAdmin)
admin.site.register(Roll, RollAdmin)
admin.site.register(WorkingShift, WorkingShiftAdmin)
admin.site.register(MarriageCount, MarriageCountAdmin)
admin.site.register(ImageShiftAct, ImageShiftActInline)
admin.site.site_header = 'Администрирование сайта'
admin.site.site_title = 'Администрирование'
