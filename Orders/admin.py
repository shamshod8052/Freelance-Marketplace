from django.contrib import admin
from .models import Order, Order_Requirements, DeliveryDetails


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'seller', 'service', 'status', 'created_at', 'delivery_date')
    list_filter = ('status', 'created_at', 'delivery_date')
    search_fields = ('buyer__username', 'seller__username', 'service__title')
    autocomplete_fields = ('buyer', 'seller', 'service', 'transaction')
    readonly_fields = ('created_at',)


@admin.register(Order_Requirements)
class OrderRequirementsAdmin(admin.ModelAdmin):
    list_display = ('order', 'short_description', 'has_example_image')
    search_fields = ('order__id', 'description')

    def short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    def has_example_image(self, obj):
        return bool(obj.example_image)

    has_example_image.boolean = True  # ✔/✘ icon


@admin.register(DeliveryDetails)
class DeliveryDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_status', 'order_delivered_date')
    list_filter = ('delivery_status', 'order_delivered_date')
    search_fields = ('order__id', 'delivery_notes')
