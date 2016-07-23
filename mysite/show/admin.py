from django.contrib import admin
from .models import Artist, Works, MyUser


class WorksInline(admin.TabularInline):
	model = Works
	extra = 0


class ArtistAdmin(admin.ModelAdmin):
	fieldsets = [
		('艺术家', {'fields': ['name']}),
	]
	inlines = [WorksInline]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(MyUser)
