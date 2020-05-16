from django.contrib import admin

# Register your models here.
from api.models import ServiceRequirements, Services, Arrangement, DetailRequirements, FileRequirement, User


class UserAdmin(admin.ModelAdmin):
    list_display = ["telegram_id", "name", "url_ktp_photo", "url_self_photo"]
    list_filter = ()
    search_fields = ["telegram_id", "name", "url_ktp_photo", "url_self_photo"]
    list_per_page = 25


class ServiceRequirementsAdmin(admin.ModelAdmin):
    list_display = ["name_requirement"]
    list_filter = ()
    search_fields = ["name_requirement"]
    list_per_page = 25


class ServicesAdmin(admin.ModelAdmin):
    list_display = ["type_service"]
    list_filter = ()
    search_fields = ["type_service"]
    list_per_page = 25


class DetailRequirementsAdmin(admin.ModelAdmin):
    list_display = ["service_id", "requirement_id"]
    list_filter = ()
    search_fields = ["service_id", "requirement_id"]
    list_per_page = 25


class ArrangementAdmin(admin.ModelAdmin):
    list_display = ["user_id", "service_id", "date", "status"]
    list_filter = ()
    search_fields = ["user_id", "service_id", "date", "status"]
    list_per_page = 25


class FileRequirementAdmin(admin.ModelAdmin):
    list_display = ["arrangement_id", "requirement_id", "url_file"]
    list_filter = ()
    search_fields = ["arrangement_id", "requirement_id", "url_file"]
    list_per_page = 25


admin.site.register(User, UserAdmin)
admin.site.register(ServiceRequirements, ServiceRequirementsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(DetailRequirements, DetailRequirementsAdmin)
admin.site.register(Arrangement, ArrangementAdmin)
admin.site.register(FileRequirement, FileRequirementAdmin)
