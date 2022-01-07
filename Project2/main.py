# Este archivo manda llamar a el archivo helper y la función
# helper_function donde se procesa la información y se obtienen
# los resultados impresos en la consola 

from helper import helper_function

exec(open("helper.py").read())


helper_function()
