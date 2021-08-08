from rest_framework import serializers

from .models import Club,Player,Membership,Country
class CountrySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Country
        fields = ("id","name","code")


class ClubSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Club
        fields = ("id","name","country")
        extra_kwargs = {'country': {'required': False}}

class PlayerSerializer(serializers.ModelSerializer):
    
    def validate_name(self, value):
        if len(value) <=6:
            raise serializers.ValidationError('Name is too short')
        return value

    def validate_age(self, value):
        if value <20 or value > 60:
            raise serializers.ValidationError('You are not eligible by age')
        return value

    class Meta:
        model=Player
        fields = ("id","name","age",'club','country')
        extra_kwargs = {'country': {'required': False},'club': {'required': False}}

class MembershipSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Membership
        fields = ("id",'club','player','signed_on','contract_img')
        extra_kwargs = {'club': {'required': False},'player': {'required': False},}

    
