from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_datetime
from .models import Robot
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class RobotCreateView(View):
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request, *args, **kwargs):
        try:
            import json
            data = json.loads(request.body)
            
            
            model = data.get('model')
            version = data.get('version')
            created = data.get('created')
            
            if not model or not version or not created:
                return JsonResponse({"error": "Missing required fields."}, status=400)
            
            
            created_date = parse_datetime(created)
            if not created_date:
                return JsonResponse({"error": "Invalid date format. Use ISO 8601."}, status=400)
            
            
            robot = Robot.objects.create(
                model=model,
                version=version,
                created=created_date,
                serial=f"{model}-{version}"
            )
            
            return JsonResponse({"message": "Robot created successfully.", "robot_id": robot.id}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred.", "details": str(e)}, status=500)



