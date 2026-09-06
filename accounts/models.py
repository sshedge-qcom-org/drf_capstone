from django.db import models
from django.db.models import QuerySet

# Create your models here.

class Organization(models.Model):
    org_name = models.CharField(max_length=256, unique=True)
    party_id = models.PositiveIntegerField(unique=True,
                                           blank=True,
                                           null=True)
    def __str__(self):
        return f"{self.org_name} (Party ID: {self.party_id})"

class CLUser(models.Model):
    class Meta:
        verbose_name = "CLO User"
        verbose_name_plural = "CLO Users"

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    class InactiveStatusReason(models.TextChoices):
        CURRENTLY_ACTIVE = "account-currently-active", "Account currently active"
        NO_ENTITLED_PROJECTS = "no-entitled-projects", "No entitled projects"
        LOST_ENTITLED_PROJECTS = "lost-training-not-completed" "LOST training not completed", "Lost training not completed"
        TERMINATED = "employment terminated", "Employment terminated"

    email = models.CharField(max_length=256, unique=True)

    org = models.CharField(max_length=512)
    username = models.CharField(max_length=256, unique=True)

    qcusername = models.CharField(max_length=256, unique=True,
                                  blank=True, null=True)

    qcquid = models.CharField(max_length=1000, unique=True,
                              blank=True, null=True)

    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.ACTIVE)
    inactive_status_reason = models.CharField(
        max_length=256,
        choices=InactiveStatusReason.choices,
        default=InactiveStatusReason.CURRENTLY_ACTIVE)

    @classmethod
    def get_active_qc_users(cls) -> QuerySet["CLUser"]:
        return (cls.objects.filter(
            status=cls.Status.ACTIVE,
            qcusername__isnull=False).exclude(qcusername="")
        )

    @classmethod
    def get_inactive_qc_users(cls) -> QuerySet["CLUser"]:
        return (
            cls.objects.filter(
                status=cls.Status.INACTIVE,
                qcusername__isnull=False,
            ).exclude(qcusername="")
        )

    def is_qc_user(self) -> bool:
        return bool(self.qcusername)

    def __str__(self) -> str:
        return f"{self.username} - {self.org}"


