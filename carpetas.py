import os

ruta_absoluta = os.path.abspath('1.3-Seccion3_Mod_Paq')
print(f"Ruta absoluta a la carpeta del módulo: {ruta_absoluta}")

# Verificar que el archivo existe en la ruta especificada
ruta_modulo = os.path.join(ruta_absoluta, 'module.py')
if os.path.isfile(ruta_modulo):
    print("El archivo module.py existe en la ruta especificada.")
else:
    print("El archivo module.py NO existe en la ruta especificada.")
    
try:
    import module
    print("¡El módulo se ha importado correctamente!")
except ImportError as e:
    print(f"Error al importar el módulo: {e}")
    
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))