from lib2to3.pgen2 import token
from itsdangerous import Serializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from app1.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
import jwt,datetime

class Loginview(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email)
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,'secret',algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt': token
        }
        return response
    
class Userview(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user = User.objects.get(id=payload['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
class Logoutview(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message":"success"
        }
        return response



