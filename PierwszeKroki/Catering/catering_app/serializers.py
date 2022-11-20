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

    def validate_dane(self, value):
        if value[0] in string.ascii_lowercase:
            raise serializers.ValidationError(
                "Dane powinny zaczynać się z dużej litery"
            )
        else:
            return value

    def validate_harmonogram_pracy(self, value):
        if 8 > value.any() > 20:
            raise serializers.ValidationError(
                "Godziny pracy powinny znajdować się w przedziale 8-20"
            )
        else:
            return value


    def validate_harmonogram_spacerow(self, value):
        if 8 > value.any() > 20:
            raise serializers.ValidationError(
                "Godziny spacerów powinny znajdować się w przedziale 8-20"
            )
        else:
            return value