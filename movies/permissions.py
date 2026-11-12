from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #questo eseguito quando c'è oggetto
        if request.method in permissions.SAFE_METHODS:
                    return True
                
        return request.user.is_staff or request.user.is_superuser
        
    def has_permission(self, request, view): #permesso viene controllato x lista create
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff or request.user.is_superuser 
    #la lista è consentita a tutti ma dobbiamo controllare se la creazione è x admin?
    #metodo eseguito x list e create; altro x object x put, update e delete
    #cambia in base a operazione specifica o associata a oggetto, che nel ns caso è id, possiamo fare chiamata a endpoint 