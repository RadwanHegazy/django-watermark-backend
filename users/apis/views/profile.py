"""
    This endpoint must get the profile details like : 
        - full_name, email, is_gold
        - is user gold must return days of expired
"""

from rest_framework import status, decorators, permissions
from rest_framework.response import Response

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def ProfileView (request) :
    try :
        current_user = request.user

        data = {
            'full_name' : current_user.full_name,
            'email' : current_user.email,
        }

        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)