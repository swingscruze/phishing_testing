from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import user
from .serializers import ItemSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.






def attackareal(request):

    return render(request, "attack_template.html")






class UserView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of all users",
        responses={
            200: openapi.Response(
                description="List of users returned successfully",
                schema=ItemSerializer(many=True)
            ),
            404: "Users not found"
        }
    )
    def get(self, request):
        """
        Get all users
        
        Returns a list of all user instances in the system.
        """
        items = user.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=ItemSerializer,
        responses={
            201: openapi.Response(
                description="User created successfully",
                schema=ItemSerializer()
            ),
            400: "Invalid user data"
        }
    )
    def post(self, request):
        """
        Create a user
        
        Creates a new user instance with the provided data.
        """
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

  

class RemoveUser(APIView):


    @swagger_auto_schema(operation_description="Remove user from that data base",
                         responses={201: openapi.Response( description="Return 201 message once user has been deleted"), 
                                    400:"user is not available on the database"})
    def get(self, request, id):
        """
        Retrieve a user by ID.
        """
        try:
            user_instance = user.objects.get(id=id)
            serializer = ItemSerializer(user_instance)
            return Response(serializer.data)
        except user.DoesNotExist:
            raise AttributeError


class FetchUser(APIView):

    def get(self, request, id):
        userinfor = user.objects.get(id=id)

        serializedata = ItemSerializer(userinfor)

        return Response(serializedata.data, status= status.HTTP_200_OK)




