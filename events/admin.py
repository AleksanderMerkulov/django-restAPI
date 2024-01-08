from django.contrib import admin

from events.models import Events, Category


# Register your models here.
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

