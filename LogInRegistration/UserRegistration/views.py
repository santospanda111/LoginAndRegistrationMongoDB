from rest_framework.views import APIView,Response,status
from .coordinator import Coordinator
from rest_framework.exceptions import ValidationError



class Index(APIView):

    def get(self,request):
        """
        This method is used to return a welcome message.
        :return: It returns the welcome message when homepage is get called.
        """
        return Response({'message':'Welcome to LogIn & Registration App'})

class Register(APIView):
    
    def post(self,request):
        """
            This method is used to register new user.
            :param request: It accepts first_name, last_name, email, username and password as parameter with datatypes.
            :return: It returns the message if successfully registered.
        """
        try:
            data=request.data
            get_data=Coordinator().check_username_present(data)
            if get_data[0]>0:
                return Response({'message': 'Username is already registered with another user.'}, status=status.HTTP_400_BAD_REQUEST)
            insert_data=Coordinator().insert_data(data)
            if insert_data is True:
                return Response({"message":"Registration Successfull"})
            return Response({'message':'Try Again'})
        except ValueError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:
            return Response({"message1": str(e)}, status=status.HTTP_400_BAD_REQUEST)