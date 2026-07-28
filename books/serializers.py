from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    is_in_stock = serializers.SerializerMethodField()

    class Meta:
        model = Book

        fields = [
            "id",
            "title",
            "author",
            "description",
            "isbn",
            "price",
            "stock",
            "status",
            "published_date",
            "is_in_stock",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "is_in_stock",
            "created_at",
            "updated_at",
        ]

    def get_is_in_stock(self, obj):
        return (obj.stock > 0
                and obj.stock == Book.Status.AVAILABLE)


    def validate_isbn(self, value):
        normalized_value = value.replace("-", "").replace(" ", "")

        if not normalized_value.isdigit():
            raise serializers.ValidationError("ISBN must contain only numbers.")

        if len(normalized_value) not in [10, 13]:
            raise serializers.ValidationError("ISBN must contain 10 or 13 digits.")
        return normalized_value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

