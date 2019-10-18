from django.contrib import admin
from .models import Question
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
	fields=['quest_title']
admin.site.register(Question)