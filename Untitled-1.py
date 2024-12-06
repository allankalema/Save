class SecureLoginSystem:
    def __init__(self, username, password):
         self._username = username
         self._password = password


    def _is_password_strong(self):
         if len(self._password) <8:
              return "Password must be atleast 8 characters long "
         
         has_upper = any(char.isupper() for char in self._password)
         has_lower = any(char.islower() for char in self._password)
         has_digit = any(char.isdigit()for char in self._password)
         has_special = any(char in ".;!@#$%^&*()_+[]" for char in self._password)

         if not has_upper:
               return "Password must contain at least one uppercase letter."
         if not has_lower:
               return "Password must contain at least one lowercase letter."
         if not has_digit:
               return "Password must contain at least one digit."
         if not has_special:
               return "Password must contain at least one special character (e.g., !, @, #, $, %, etc.)."

         return True 
    
    def validate_credentials(self):
         if  not  self._username or not self._password:
              return "Username and password cannot be empty "
          
         password_validation_result = self._is_password_strong()

         if password_validation_result != True:  # we r doing a whotelisting so the  function must return  true 
          return password_validation_result
         
         return "Login successful"
         

    
    @property
    def username(self):
         return self._username
    
    @username.setter
    def username(self, new_username):
         if new_username:
              self._username = new_username
         else:
            raise ValueError("Username cannot be empty")


while True:
     # Example usage
     us3rname = input("Username: -> ")
     Pa55word= input("Password: -> ")

     user = SecureLoginSystem(us3rname, Pa55word)

     validation_result = user.validate_credentials()
     if validation_result == "Login successful":
      print(f"Login successful for user: {user.username}")
     else:
      print(f"Invalid credentials: {validation_result}")

     print ('-------------------------------------------------')