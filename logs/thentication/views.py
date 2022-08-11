from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from knox.auth import AuthToken
from .ser import RegSer


# Create your views here.
@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    userinfo = {
        "id" : user.id,
        'username': user.username,
        'email': user.email     
    }


    return Response({'user_info': userinfo,'token': token})

@api_view(['GET'])
def get_user_data(request):

    user = request.user

    if  user.is_authenticated:

        userinfo = {
            "id" : user.id,
            'username': user.username,
            'email': user.email}
        
        return Response({'user_info' : userinfo,})

    return Response({'error': "You are not authenticated"}, status=400)

@api_view(['POST'])
def register(request):
    serializer = RegSer(data= request.data)
    serializer.is_valid(raise_exception= True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    userinfo = {
    "id" : user.id,
    'username': user.username,
    'email': user.email}

    return Response({'user_info': userinfo,'token': token})

    #user : userserializer(user, contet = self.get_serializercontext()).data


 
