from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ..serializers import Watermark, CreateWatermarkSerializer

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def CreateWatermark (request) : 
    try :
        data = request.data
        serializer = CreateWatermarkSerializer(data=data,context={'user':request.user})
        if serializer.is_valid() : 
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)