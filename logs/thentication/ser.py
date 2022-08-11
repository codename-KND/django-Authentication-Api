
from django.contrib.auth.models import User
from rest_framework import serializers,validators

class RegSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')

        extra_kwargs = { 'password' : {'write_only': True}, 'email': {'required':True,'allow_blank': False ,'validators':[validators.UniqueValidator(User.objects.all(),'Email already used')]}}


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

