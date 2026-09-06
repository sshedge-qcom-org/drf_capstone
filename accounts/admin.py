from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

# Register your models here.

from .models import CLUser, Organization

# admin.site.register(Organization)
# admin.site.register(CLUser)

# Customize OrganizationAdmin
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "org_name",
        "party_id",
        "cluser_count",
    )

    search_fields = (
        "org_name",
        "party_id",
    )

    ordering = ("org_name",)

    @admin.display(description="CLO users")
    def cluser_count(self,obj:Organization):
        return obj.clusers.count()

@admin.register(CLUser)
class CLUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "organization",
        "qcusername",
        "status",
        "is_qc_user_display",
    )
    list_filter = (
        "status",
        "organization",
        "inactive_status_reason",
    )
    search_fields = (
        "username",
        "email",
        "qcusername",
        "qcquid",
        "organization__org_name",
    )
    ordering = ("username",)
    list_select_related = ("organization",)
    readonly_fields = (
        "is_qc_user_display",
    )
    actions = (
        "mark_as_active",
        "mark_as_inactive",
    )

    @admin.display(boolean=True, description="QC user")
    def is_qc_user_display(self, obj:CLUser):
        return obj.is_qc_user()

    @admin.action(description="Mark selected users as active")
    def mark_as_active(self,
                       request:HttpRequest,
                       queryset: QuerySet[CLUser]) -> None:
        queryset.update(status=CLUser.Status.ACTIVE,
                        inactive_status_reason=(
                            CLUser.InactiveStatusReason.CURRENTLY_ACTIVE
                        ),)
    @admin.action(description="Mark selected users as inactive")
    def mark_as_inactive(self,
                         request:HttpRequest,
                         queryset: QuerySet[CLUser]) -> None:
        queryset.update(status=CLUser.Status.INACTIVE,
                        inactive_status_reason=(
                            CLUser.InactiveStatusReason.NO_ENTITLED_PROJECTS
                        ),
                        )
