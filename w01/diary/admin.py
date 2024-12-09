from django.contrib import admin
from diary.models import Letter

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
  list_display = ['lno','ltitle','lcontent','ldate']

