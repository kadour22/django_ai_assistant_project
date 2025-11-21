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

def update_bug_status(bug_id:int, status:str):
    try:
        bug = Bug.objects.get(id=bug_id)
        bug.status = status
        bug.save()
        return f"Bug '{bug.id}' status has been updated to '{status}'."
    except Bug.DoesNotExist:
        return "Bug not found."

def create_bug(title:str, description:str, assigned_to:str=None):
    user = None
    if assigned_to:
        try:
            user = User.objects.get(username=assigned_to)
        except User.DoesNotExist:
            return "Assigned user not found."
    bug = Bug.objects.create(title=title, description=description, assigned_to=user)
    return f"Bug '{bug.title}' has been created with ID '{bug.id}'."

def delete_bug(bug_id:int):
    try:
        bug = Bug.objects.get(id=bug_id)
        bug.delete()
        return f"Bug '{bug.id}' has been deleted."
    except Bug.DoesNotExist:
        return "Bug not found."