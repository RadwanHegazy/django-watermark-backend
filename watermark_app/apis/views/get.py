from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ..serializers import WatermarkSerializer, Watermark

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def GetWatermark (request) : 
    try :
        query = Watermark.objects.filter(user=request.user)
        data = []

        for i in query : 
            if i.output_path :
                data.append({
                    'name' : str(i.original.name).split('/')[-1],
                    'output' : i.output_path,
                })

        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)