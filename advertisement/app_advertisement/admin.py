from django.contrib import admin
from django.utils.html import format_html

from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'price', 'trades', 'date_now', "created_date", 'image', 'user']
    list_filter = ['date_now', 'descriptions', "trades"]
    fieldsets = (
        (
            "Первый блок",
            {
                "fields": ("title", "descriptions", 'image', 'user'),
            },
        ),
        (
            "Второй блок",
            {
                'classes': ('collapse',),
                "fields": ('price', 'trades'),
            },
        ),
    )

    actions = ['make_true', 'make_False', 'created_date']

    def image(self, obj):
        if obj.image:
            return format_html('<img src="%s" width="100" height="100">' % obj.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" width="100" height="100">')

    image.short_description = 'Image'

    @admin.action(description="Обновить торг на True")
    def make_true(self, request, queryset):
        queryset.update(trades=True)

    @admin.action(description="Обновить торг на False")
    def make_False(self, request, queryset):
        queryset.update(trades=False)


