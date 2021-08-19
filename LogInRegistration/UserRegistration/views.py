from rest_framework.views import APIView,Response,status
from .coordinator import Coordinator
from rest_framework.exceptions import ValidationError,AuthenticationFailed



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

class LogIn(APIView):
        
    def post(self,request):
        """[This method will take the required input and do login]
        Returns:
            [returns the message if successfully loggedin]
        """
        try:
            data=request.data
            username=data.get('username')
            password=data.get('password')
            user_auth=Coordinator().authenticate_data(username)
            if username==user_auth['username'] and password==user_auth['password']:
                return Response({"msg": "Loggedin Successfully", 'data' : {'username': data.get('username')}}, status=status.HTTP_200_OK)
            return Response({"msg": 'Wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'message': "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST) 
        except AuthenticationFailed:
            return Response({'message': 'Authentication Failed'}, status=status.HTTP_400_BAD_REQUEST) 
        except Exception:
            return Response({"msg1": "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)