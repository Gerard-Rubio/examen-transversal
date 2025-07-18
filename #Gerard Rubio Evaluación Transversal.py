#Gerard Rubio Evaluación Transversal
productos={
"8475HD": ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
inventario={
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1]
}
while True:
    print("\n****MENU PRINCIPAL****")
    print("1) Busqueda por marca.")
    print("2) Busqueda por precio.")
    print("3) Actualizar precio")
    print("4) Salir del progama.")
    opcion=input("Ingrese una opción (1-4): ")

    if opcion=="1":
        marca=input("Ingrese la marca que busca: ")

        encontrado=False
        for codigo, datos in productos.items():

            if datos[0].lower()==marca.lower():
                precio, stock=inventario[codigo]
                print(f"El Stock es de: {stock} ")
                encontrado=True
                if not encontrado:
                    print("No se encontró producto con esa marca")
    elif opcion=="2":
        try:
            max_precio=int(input("Ingrese un precio como máximo: "))
            min_precio=int(input("Ingrese un precio como mínimo: "))
            for codigo,(precio,stock) in inventario.items():
                if precio<max_precio and precio>min_precio:
                   tipo=productos[codigo][1]
                   print(f"Código: {codigo}")
                   encontrado=True
                   if not encontrado:
                    print("No hay productos con ese precio disponible")
        except ValueError:
            print("Debe ingresar valores enteros!!!")
    elif opcion=="3":
        try:
         codigo=input("Ingrese modelo a actualizar: ")
         if codigo in inventario:
            precio_nuevo=input("Ingrese precio nuevo: ")
            inventario[codigo][1]=precio_nuevo
            print("Precio actualizado")
         sub_opcion=input("Desea actualizar otro precio? (s/n): ")  
         if sub_opcion=="s":
            codigo=input("Ingrese modelo a actualizar: ")
            if codigo in inventario:
             precio_nuevo=input("Ingrese precio nuevo: ")
             inventario[codigo][1]=precio_nuevo
             print("Precio actualizado")
         elif sub_opcion=="n":
            print("Cambio de precios terminado....")
        except ValueError:
            print("Modelo no encontrado")
    elif opcion=="4":
        print("Saliendo del programa....")
        break
    else:
        print("Favor de ingresar una opción valida.")