from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # token = Token.objects.create(user=user)
        token = Token.objects.get(user=user)
        data = serializer.data
        data['token'] = token.key # ? kayıtla birlikte token'ı user infosuna ekledik
        data['message'] = 'user created successfully' 
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)