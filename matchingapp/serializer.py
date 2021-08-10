from rest_framework import serializers
from django.conf import settings
import ssl
import smtplib
from .models import Club,Player,Membership,Country
from django.core.mail import send_mail
class CountrySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Country
        fields = ("id","name","code")


class ClubSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Club
        fields = ("id","name","country")
        extra_kwargs = {'country': {'required': False}}

class MembershipSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Membership
        fields = ("id",'club','signed_on','contract_img')
        extra_kwargs = {'club': {'required': False},'player': {'required': False},}

class PlayerSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name is too short')
        return value

    def validate_age(self, value):
        if value <20 or value > 60:
            raise serializers.ValidationError('You are not eligible by age')
        return value

    def validate(self, attrs):
        msg = 'Hi, thank you for registering in our membership site '
        usr = attrs.get('name')
        port = settings.EMAIL_PORT
        smtp_server = settings.EMAIL_HOST
        sender_email = settings.EMAIL_HOST_USER
        password = settings.EMAIL_HOST_PASSWORD
        receiver_email = 'fongohmartin@gmail.com'
        subject = 'welcome to world Club'
        body = msg + str(usr) + "More information will be forwarded to you concerning this registrations " + "https://digitalrenter.com"
        message = 'Subject: {}\n\n{}'.format(subject, body)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        
        return super().validate(attrs)

    # members = MembershipSerializer(source='membership', many=True)
    
    class Meta:
        model=Player
        # depth=2
        fields = '__all__'

        

    
