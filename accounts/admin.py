from django.contrib import admin

# Register your models here.
from django.contrib import admin
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
    pass

