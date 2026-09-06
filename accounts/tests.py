from django.db import IntegrityError, transaction
from django.test import TestCase

from .models import CLUser, Organization


class OrganizationModelTests(TestCase):
    def test_string_representation(self):
        organization = Organization.objects.create(
            org_name="Microsoft",
            party_id=1001,
        )

        self.assertEqual(
            str(organization),
            "Microsoft (Party ID: 1001)",
        )

    def test_org_name_must_be_unique(self):
        Organization.objects.create(
            org_name="Microsoft",
            party_id=1001,
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Organization.objects.create(
                    org_name="Microsoft",
                    party_id=1002,
                )


class CLUserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.microsoft = Organization.objects.create(
            org_name="Microsoft",
            party_id=1001,
        )

    def test_user_string_representation(self):
        user = CLUser.objects.create(
            email="suraj@example.com",
            org="Microsoft",
            username="sshedge",
            organization=self.microsoft,
        )

        self.assertEqual(
            str(user),
            "sshedge - Microsoft",
        )

    def test_user_with_qcusername_is_qc_user(self):
        user = CLUser.objects.create(
            email="suraj@example.com",
            org="Microsoft",
            username="sshedge",
            qcusername="suraj.qc",
            organization=self.microsoft,
        )

        self.assertTrue(user.is_qc_user())

    def test_user_without_qcusername_is_not_qc_user(self):
        user = CLUser.objects.create(
            email="regular@example.com",
            org="Microsoft",
            username="regular.user",
            organization=self.microsoft,
        )

        self.assertFalse(user.is_qc_user())

    def test_active_qc_users_returns_only_active_qc_users(self):
        active_qc_user = CLUser.objects.create(
            email="active.qc@example.com",
            org="Microsoft",
            username="active.qc",
            qcusername="active.qc",
            organization=self.microsoft,
            status=CLUser.Status.ACTIVE,
        )

        CLUser.objects.create(
            email="inactive.qc@example.com",
            org="Microsoft",
            username="inactive.qc",
            qcusername="inactive.qc",
            organization=self.microsoft,
            status=CLUser.Status.INACTIVE,
            inactive_status_reason=(
                CLUser.InactiveStatusReason.TERMINATED
            ),
        )

        CLUser.objects.create(
            email="regular@example.com",
            org="Microsoft",
            username="regular.user",
            organization=self.microsoft,
            status=CLUser.Status.ACTIVE,
        )

        result = CLUser.get_active_qc_users()

        self.assertQuerySetEqual(
            result,
            [active_qc_user],
            ordered=False,
        )

    def test_inactive_qc_users_returns_only_inactive_qc_users(self):
        inactive_qc_user = CLUser.objects.create(
            email="inactive@example.com",
            org="Microsoft",
            username="inactive.user",
            qcusername="inactive.qc",
            organization=self.microsoft,
            status=CLUser.Status.INACTIVE,
            inactive_status_reason=(
                CLUser.InactiveStatusReason.TERMINATED
            ),
        )

        CLUser.objects.create(
            email="active@example.com",
            org="Microsoft",
            username="active.user",
            qcusername="active.qc",
            organization=self.microsoft,
            status=CLUser.Status.ACTIVE,
        )

        result = CLUser.get_inactive_qc_users()

        self.assertQuerySetEqual(
            result,
            [inactive_qc_user],
            ordered=False,
        )

