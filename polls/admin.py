from django.contrib import admin
from django.utils.html import format_html
from .models import Question, Choice, Contact


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at", "uploaded_file_link")
    list_filter = ("submitted_at",)
    search_fields = ("name", "email", "message")

    def uploaded_file_link(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank">View File</a>', obj.file.url
            )
        return "No file uploaded"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Contact, ContactAdmin)
