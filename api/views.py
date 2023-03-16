from django.http import JsonResponse,HttpRequest
from .models import Tasks
# Create your views here.

def get_tasks(request: HttpRequest):
    if request.method == 'GET':
        tasks = Tasks.objects.all()


        result = {
            'result':[]
        }

        for task in tasks:
            model = task.task
            result.setdefault(model,[])
            result[model].append({
                'id':task.id,
                'task':task.task,
                'description':task.description,
                'complited':task.complited
            })
        return JsonResponse(result)