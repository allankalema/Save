class User:
   
    _ROLE_PERMISSIONS = {
        'admin': {'can_access_sensitive_data': True},
        'user': {'can_access_sensitive_data': False},
        'guest': {'can_access_sensitive_data': False},
    }
    
    def __init__(self, username, role):
     self._username = username
     self._role= role if role in self._ROLE_PERMISSIONS else 'guest'

    def can_access_sensitive_data(self):
     
     return self._ROLE_PERMISSIONS[self.role].get('can_access_sensitive_data', False)
    
    @property
    def username(self):
      return self._username
    
    @property
    def role(self):
      return self._role
    


# Usage
user1 = User('Alice', 'admin')
user2 = User('Bob', 'user')
user3 = User('Eve', 'unknown')  # Example of invalid role

print(user1.can_access_sensitive_data())  # Output: True
# print(user1.username)
print(user2.can_access_sensitive_data())  # Output: False
print(user3.can_access_sensitive_data())  # Output: False
   
      
