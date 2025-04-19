print ("This code is to check password strength")
user_password = input ("please enter a password:") 
special_characters = "~!@#$%^&*_-+=`|){}[]:;'<>,.?/"

def check_password_strength():
    global special_characters
    check_length(user_password)
    check_uppercase(user_password)
    check_lowercase(user_password)
    check_isnumeric(user_password)
    check_isspecial(user_password)
                  
def check_length(user_password):
    if not len(user_password) >= 8:
       print ("Password must be atleast 8 Character long") 

def check_uppercase(user_password):
    if not any(char.isupper() for char in user_password):
       print ("Password must have atleast 1 Upper Case Character")
 
def check_lowercase(user_password):
    if not any(char.islower() for char in user_password):
       print ("Password must have atleast 1 Lower Case Character")


def check_isnumeric(user_password):
    if not any(char.isdigit() for char in user_password):
       print ("Password must have atleast 1 Number")

def check_isspecial(user_password):
    Flag = True
    for ch in user_password:
        if ch in special_characters:
           Flag = True
           print ("Password is Strong")       
           break;
        else:
           Flag = False
           
    if Flag == False: 
       print ("Password must have atleast 1 Special Character")       
       return "False"
    else:
       return "True"
    
if __name__ == "__main__":
     check_password_strength()