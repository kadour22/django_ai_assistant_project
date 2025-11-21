from assistant.models import Bug
from django.contrib.auth.models import User

def assign_bug_to_user(bug_id:int, user_name:str):
    try:
        bug = Bug.objects.get(id=bug_id)
        user = User.objects.get(username=user_name)
        bug.assigned_to = user
        bug.save()
        return f"Bug '{bug.id}' has been assigned to user '{user_name}'."
    except Bug.DoesNotExist:
        return "Bug not found."
    except User.DoesNotExist:
        return "User not found."