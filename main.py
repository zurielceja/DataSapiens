#########################

# Este es el código principal para correr 
# El usuario es zuriel y la contraseña es zuriel

#########################


# Call functions to process data

from helper import helper_function
from login import login_function


exec(open("login.py").read())
exec(open("helper.py").read())

# call functions
login_function()
helper_function()
