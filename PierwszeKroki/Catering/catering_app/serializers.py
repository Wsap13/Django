from rest_framework import serializers

class PracownicySerializer(serializers.Serializer):
    imie = serializers.CharField()
    nazwisko = serializers.CharField()
    pesel = serializers.IntField()
    pensja = serializers.DecimalField()

    def validate_pensja(self,value):
        if value <= 0:
            raise serializers.ValidationError('Pensja nie może być mniejsza lub równa zero.')
        else:
            return value