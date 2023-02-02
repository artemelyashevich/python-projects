from rest_framework import serializers
from .models import Men


class MenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Men
        fields = ("__all__")
