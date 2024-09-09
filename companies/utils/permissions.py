from rest_framework import permissions
from accounts.models import User_Group, Group_Permission
from django.contrib.auth.models import Permission

def Check_permissions(user, method, permission_to) -> bool | None:

    if not user.is_authenticated:
        return False
    
    if user.is_owner:
        return True
    
    required_permission = 'view_' +permission_to
    if method =='POST':
        required_permission ='add_' +permission_to

    if method == 'PUT':
        required_permission = 'chang_' +permission_to

    if  method == 'DELETE':
        required_permission = 'delete_' +permission_to

    groups =  User_Group.objects.values('group_id').filter(user_id=user.id).all()

    for group in groups:
        permissions = Group_Permission.objects.values('permission_id').filter(group_id=group['group_id']).all()  

        for permission in permissions:

            if Permission.objects.filter(id=permission['permission_id'], codename=required_permission).exists():
                return True
            

class EmployeePermission(permissions.BasePermission):
    message = 'O funcionário não têm permisão para gerenciar funcionários'

    def has_permission(self, request, _view) -> bool | None:
        return Check_permissions(request.user, request.method, permission_to='employee')
    
class GroupsPermission(permissions.BasePermission):
    message = 'O funcionário não têm permisão para gerenciar grupos'
      
    def has_permission(self, request, _view) -> bool | None:
        return Check_permissions(request.user, request.method, permission_to='group')
    

class GorpusPermissionPermissions(permissions.BasePermission):
    message = 'O funcionário não têm permisão para gerenciar permissões'

    def has_permission(self, request, _view) -> bool | None:
        return Check_permissions(request.user, request.method, permission_to='permission')
    
class TaskPermission(permissions.BasePermission):
    message = 'O funcionário não têm permisão para gerenciar as tarefas de todos os funcionários'
    
    def has_permission(self, request, _view) -> bool | None:
        return Check_permissions(request.user, request.method, permission_to='task')
    


    


    





    

