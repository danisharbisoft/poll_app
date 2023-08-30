from django.contrib import admin
from .models import Question, Choice


class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 3


class FormatAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions', {'fields': ['question_text']}),
        ('Date', {'fields': ['pub_date']})
    ]
    search_fields = ["question_text"]
    list_display = ['question_text', 'pub_date', 'check_recency']
    list_filter = ['pub_date']
    inlines = [ChoiceAdmin]


admin.site.register(Question, FormatAdmin)
# Register your models here.
