from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import User


class LoginSerializer (serializers.Serializer) : 
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'message' : "invalid email"
            },code=400)
        
        if not self.user.check_password(password) :
            raise serializers.ValidationError({
                'message' : "invalid password"
            },code=400)

        return attrs
    
    @property
    def tokens (self) :
        t = RefreshToken.for_user(self.user)
        return {
            'refresh' : str(t),
            'access' : str(t.access_token),
        }

class RegisterSerializer (serializers.ModelSerializer) : 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email','password','full_name',)

    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        self.user.save()
        return self.user
    

    @property
    def tokens (self) :
        t = RefreshToken.for_user(self.user)
        return {
            'refresh' : str(t),
            'access' : str(t.access_token),
        }
    