from django.http import response
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def job_list_api(request):
    job_list = Job.objects.all()
    data = JobSerializer(job_list, many=True).data
    return Response({'data': data})
