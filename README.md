Act as my Django REST Framework tutor and continue my existing practical learning project from its current state.

My experience level:
- Comfortable with basic Python
- Beginner in Django and DRF
- I prefer step-by-step explanations that teach both what the code does and why
- Please teach one concept at a time and let me ask questions between stages

Project details:
- Project name: clo_portal
- Django configuration package: config
- Django app: accounts
- Dependency management: uv with pyproject.toml and uv.lock
- Interactive shell: IPython
- Database: SQLite for learning
- Models: Organization and CLUser

Completed:
✓ Project setup using uv
✓ Django app creation and configuration
✓ Organization and CLUser models
✓ Migrations
✓ ForeignKey relationships and reverse relationships
✓ ORM practice in IPython
✓ TextChoices
✓ Meta options, including verbose_name and verbose_name_plural
✓ Database constraints and the distinction between validation and constraints
✓ Django Admin registration and customization
✓ list_display, search_fields, list_filter, ordering, list_select_related, readonly_fields, and Admin actions
✓ Initial model tests

Important model relationship:
- CLUser.organization is a ForeignKey to Organization
- related_name is "clusers"
- on_delete is models.SET_NULL
- The organization field allows null and blank values

Current understanding:
- Serializer validators protect API input and provide friendly errors
- Model validation handles Django-level business rules
- Database constraints provide the final database integrity guarantee
- select_related helps prevent N+1 queries for ForeignKey relationships

Continue from:
1. Install Django REST Framework using uv
2. Explain JSON representation before introducing serializers
3. Explain Serializer versus ModelSerializer
4. Create an OrganizationSerializer
5. Create a CLUserSerializer
6. Explain every Meta option and field behavior used
7. Demonstrate serialization and deserialization in IPython
8. Add serializer validation
9. Write serializer tests with at least:
   - one successful validation test
   - one validation-failure test
10. Explain relationship representation choices, such as primary key, nested object, slug, and string representation

Teaching requirements:
- Do not repeat the completed Django setup unless it is necessary
- Use complete, runnable examples with file paths and imports
- Use uv commands, not pip or requirements.txt
- Explain the underlying Django idea before showing how DRF builds on it
- Include prediction checkpoints and small exercises
- Point out common mistakes
- Discuss query efficiency when serializers access organizations
- End each substantial lesson with a recap, exercise, and suggested next topic

Please begin with the first DRF lesson: installing and configuring DRF, understanding Python dictionaries versus JSON, and manually representing one Organization object before creating OrganizationSerializer.
``