from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer, UserModelSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User

class UserAPI(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:
            serializer.error_messages = {
                'message':'El usuario ya ha sido creado'
            }
            return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.GenericViewSet):
    
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            id1= UserModelSerializer(user).data.get('id')
            username= UserModelSerializer(user).data.get('username')
            firsname= UserModelSerializer(user).data.get('first_name')
            last_name= UserModelSerializer(user).data.get('last_name')
            email= UserModelSerializer(user).data.get('email')
            data = {
                'id':id1,
                'username':username,
                'first_name':firsname,
                'last_name':last_name,
                'email':email,
                'token': token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
            serializer.error_messages = {
                'message':'Las credenciales no son validas'
            }
            return Response(data = serializer.error_messages, exception=True , status=status.HTTP_400_BAD_REQUEST)
        