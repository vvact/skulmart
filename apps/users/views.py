from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    try:
        data = request.data
        if not data:
            return Response({'error': 'No data provided'}, status=400)

        # Check if the email already exists
        if User.objects.filter(email=data.get('email')).exists():
            return Response({'error': 'User with this email already exists'}, status=400)

        user = User.objects.create(
            first_name=data.get('fname', ''),
            last_name=data.get('lname', ''),
            username=data.get('email', ''),
            email=data.get('email', ''),
            password=make_password(data.get('password'))
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data, status=201)
    except KeyError as e:
        return Response({'error': f'Missing field: {str(e)}'}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
