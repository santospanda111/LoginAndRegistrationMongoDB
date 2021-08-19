from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .coordinator import Note_Coordinator
from rest_framework.exceptions import ValidationError
from log import get_logger

# Logger configuration
logger= get_logger()

class Notes(APIView):
    

    def get(self, request):
        """
            This method is used to read the notes according to user.
            :param request: It accepts user_id as parameter.
            :return: It returns the note data.
        """
        try:
            data= request.data
            user_note = Note_Coordinator().read_notes(data)
            return Response({"data":user_note}, status=status.HTTP_200_OK)    
        except AssertionError as e:
            logger.exception(e)
            return Response({"message":"Put user id to get notes"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            This method is used to create new notes according to user.
            :param request: It accepts user_id,title and description as parameter.
            :return: It returns response that notes successfully created or not.
        """
        try:
            data=request.data
            id= Note_Coordinator().insert_notes(data)
            if id is True:
                return Response({'message': 'Notes created successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            logger.exception(e)
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            logger.exception(e)
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

 
    def put(self,request):
        """
            This method is used to update notes using note_id.
            :param request: It accepts note_id,user_id,title and description as parameter.
            :return: It returns response that notes successfully updated or not.
        """
        try:
            data=request.data
            updated_data=Note_Coordinator().update_note(data)
            if updated_data is True:
                return Response({'msg':'Complete Data Updated'}, status=status.HTTP_200_OK)
        except ValueError as e:
            logger.exception(e)
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            logger.exception(e)
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        """
            This method is used to delete notes using user_id.
            :param request: It accepts user_id as parameter.
            :return: It returns response that notes successfully deleted or not.
        """
        try:
            data=request.data
            deleted_data=Note_Coordinator().delete_note(data)
            if deleted_data is True:
                return Response({'msg':'Data Deleted'}, status=status.HTTP_200_OK) 
        except ValueError as e:
            logger.exception(e)
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)