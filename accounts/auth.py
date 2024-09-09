from rest_framework.exceptions import AuthenticationFailed,APIException
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:

    def signin(self, email=None, password=None) -> User:       
        execption_auth =  AuthenticationFailed("Houve um erro no email ou senha")

        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            raise execption_auth
        
        user = User.objects.filter(email=email).first()
        
        if not check_password(password, user.password):
            raise execption_auth
        
        return user 

         
    def  signup(self, name, email, password, type_account="owner", company_id=False):

        if not name or name == "": 
            raise APIException("O nome não pode ser null")  

        if not email or email == "": 
            raise APIException("O email não pode ser null")  

        if not password or password == "": 
            raise APIException("A senha não pode ser null")    

        if type_account == "employee" and not company_id:
            raise APIException("O id da empresa não pode ser vazio") 
        
        user = User
        if user.objects.filter(email=email).exists():
            raise APIException("Esse email já existe no DB")
        
        password_hashed = make_password(password)

        create_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account =="employee" else 1
        )

        if type_account == "owner":
            create_enterprise = Enterprise.objects.create(
                name='Nome da empresa',
                user_id=create_user.id 
            )

        if type_account == "employee":
            Employee.objects.create(
                enterprise_id=company_id or create_enterprise.id,
               user_id=create_user.id
            )   

        return create_user    

            
