def self():
    codigo = 'def self():\n    codigo = {0!r}\n    print(codigo.format(codigo))'
    print(codigo.format(codigo))

# Self guarda en codigo un string que es una plantilla de su propia definición.
# lo que hace {0!r} cuando hace codigo.format(codigo) reemplaza {0!r} por el propio string codigo, 
# pero escrito como representación de Python, con comillas y \n. 
