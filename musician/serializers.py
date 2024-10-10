from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )

# class MusicianListSerializer(MusicianSerializer):
#     is_adult = serializers.BooleanField(
#         source="musician.is_adult",
#         read_only=True
#     )
