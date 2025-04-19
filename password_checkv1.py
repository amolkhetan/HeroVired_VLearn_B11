print ("This code is to check password strength")
user_password = input ("please enter a password:") 
special_characters = "~!@#$%^&*_-+=`|){}[]:;'<>,.?/"

def check_password_strength(user_password):
   global special_characters
   if not len(user_password) >= 8:
      print ("Password must be atleast 8 Character long")
      return False
   elif not any(char.isupper() for char in user_password):
      print ("Password must have atleast 1 Upper Case Character")
      return False
   elif not any(char.islower() for char in user_password):
      print ("Password must have atleast 1 Lower Case Character") 
      return False
   elif not any(char.isdigit() for char in user_password):
      print ("Password must have atleast 1 Number")
      return False  
   for ch in user_password:
      if ch in special_characters:
         print ("Password is Strong")
         return True
         break;
   else:
      print ("Password must have atleast 1 Special Character")
      return False   
  
                    
if __name__ == "__main__":
   check_password_strength(user_password)
   