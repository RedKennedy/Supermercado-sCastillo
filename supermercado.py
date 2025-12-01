def productoMasCaro(productos):

  # En esta variable se guardanda el precio mas alto que encuentre
  productoMC = 0
  # En esta se va guardando el nombre del producto mas caro
  nombrePMC = 0

 # abro el archivo productos.csv para leerlo
  with open('productos.csv', 'r') as productos:

# Se lee cada linea del archivo
   for linea in productos:

# Se separa los datos por coma
    id = linea.split(',')[0]
    nombre = linea.split(',')[1]
    precio = int (linea.split(',')[2]) # Se convierte el precio a numero
    cantidad = linea.split(',')[3]

 # Si el precio de este producto es mayor al que tenia guardado...
    if precio > productoMC:
      # Se actualiza el nuevo precio mas caro
      productoMC = precio
      # y se guarda el nombre del producto mas caro
      nombrePMC = nombre

  # Se muestra el nombre del producto
   print(nombrePMC)
  # Y se devuelve el nombre del producto mas caro
   return(nombrePMC)
  
# Se abre el archivo y se llama a la función que crearon
with open('productos.csv', 'r') as productos:
  productoMasCaro(productos)

def valorTotalBodega(productos):

# En esta variable se va sumando el valor total de toda la bodega
 valortotal = 0

 # Se abre el archivo productos.csv para leerlo
 with open('productos.csv', 'r') as productos:

# Se lee cada linea del archivo
   for linea in productos:

 # Se separan los datos por coma
    id = linea.split(',')[0]
    nombre = linea.split(',')[1]
    precio = int (linea.split(',')[2])  # Se convierte el precio a numero
    cantidad =int (linea.split(',')[3]) # Se convierte la cantidad a numero

 # Se multiplica el precio por la cantidad y se agrega al total
    valortotal += precio * cantidad

# Se muestra el valor total de la bodega
 print(valortotal)
 # Se muestra el valor total de la bodega
 return(valortotal)

# Se abre el archivo y se llama a la función que crearon
with open('productos.csv', 'r') as productos:
  valorTotalBodega(productos)

def productoConMasIngresos(items, productos):

# En esta variable se guarda el mayor ingreso encontrado
  productoCMI = 0
# En esta se guarda el nombre del producto con mas ingresos
  nombreCMI = 0
# Esta variable guarda el ingreso calculado para cada producto
  ingreso = 0

# Se abre el archivo items.csv
  with open('items.csv', 'r') as items:
  # Se abre el archivo productos.csv
    with open('productos.csv', 'r') as productos:

# Se lee cada linea del archivo items
      for linea in items:

        # Se separan los datos por punto y coma
        boleta = linea.split(';')[0]
        id = int (linea.split(';')[1]) # Se convierte el id a numero
        cantidad = int (linea.split(';')[2]) # Se convierte la cantidad a numero

      # Se lee cada linea del archivo productos
        for linea in productos:

          # Se separan los datos del producto por coma
           id_p = int (linea.split(',')[0]) # Se convierte el id_p a numero
           nombre = linea.split(',')[1]
           precio = int (linea.split(',')[2]) # Se convierte el precio a numero
           cantidad_p = linea.split(',')[3]

 # Si los dos ID son iguales, significa que es el mismo producto
           if id == id_p:
            # Se calcula el ingreso: precio por cantidad vendida
            ingreso = precio * cantidad
            # Si este ingreso es mayor al que estaba guardado...
            if ingreso > productoCMI:
              # Se guarda el nuevo ingreso mas alto
              productoCMI = ingreso
              # Y se guarda el nombre del producto
              nombreCMI = nombre

      # Se muestra el nombre del producto con mas ingresos
      print(nombreCMI)
      # Y se devuelve ese nombre
      return(nombreCMI)

with open('productos.csv', 'r') as productos:
  with open('items.csv', 'r') as items:
    productoConMasIngresos(items, productos)

def totalVentasDelMes(año, mes, items, productos, ventas):

  # En esta variable se va sumando el total de ventas del mes pedido
  totalVentas = 0

# Se abre el archivo items.csv
  with open('items.csv', 'r') as items:
    # Se lee cada linea del archivo items
    for linea in items:

# Se separan los datos por punto y coma
      boleta = linea.split(';')[0]
      id_item = int(linea.split(';')[1]) # Se convierte el id_item a numero
      cantidad = int(linea.split(';')[2]) # Se convierte la cantidad a numero

# Se abre el archivo productos.csv
      with open('productos.csv', 'r') as productos:

       # Se lee cada linea del archivo productos
        for linea_p in productos:
          # Se separan los datos por coma
          id_p = int(linea_p.split(',')[0]) # Se convierte el id_p a numero
          precio = int(linea_p.split(',')[2]) # Se convierte el precio a numero

        # Si los dos ID son iguales, significa que es el mismo producto
          if id_item == id_p:

            # Se abre el archivo ventas.csv
            with open('ventas.csv', 'r') as ventas:

              # Se lee cada linea del archivo ventas
              for linea_v in ventas:

                # Se separan los datos por punto y coma
                boleta_v = linea_v.split(';')[0]
                fecha = linea_v.split(';')[1]

               # Si las dos boletas son iguales, es la misma venta
                if boleta == boleta_v:

                 # Se separa la fecha por guiones
                  partes_fecha = fecha.split('-')
                  dia_v = int(partes_fecha[0]) # Se convierte el dia_v a numero
                  mes_v = int(partes_fecha[1]) # Se convierte el mes_v a numero
                  año_v = int(partes_fecha[2]) # Se convierte el año_v a numero

                  # Si la fecha coincide con el mes y año pedidos...
                  if mes_v == mes and año_v == año:
                    # Se suma al total el precio multiplicado por la cantidad
                    totalVentas += precio * cantidad

    # Se muestra el total de ventas del mes
    print(totalVentas)
    # Y se devuelve ese total
    return(totalVentas)

with open('productos.csv', 'r') as productos:
  with open('items.csv', 'r') as items:
    with open('ventas.csv', 'r') as ventas:
      totalVentasDelMes(2010, 10, items, productos, ventas)

def informe():

    # Se llama a la funcion que busca el producto mas caro del archivo productos.csv
    nombre_mas_caro = productoMasCaro("productos.csv")

    # Se llama a la funcion que calcula el valor total de todos los productos en bodega
    total_bodega = valorTotalBodega("productos.csv")

    # Se llama a la funcion que encuentra el producto con mas ingresos
    producto_mas_ingresos = productoConMasIngresos("items.csv", "productos.csv")

    # Se llama a la funcion que calcula las ventas de un mes y año especifico
    ventas_periodo = totalVentasDelMes(2010, 10, "items.csv", "productos.csv", "ventas.csv")

    # Se crea el archivo informe.txt en modo escritura
    with open("informe.txt", "w") as salida:

        # Se escribe el producto mas caro encontrado
        salida.write(f"El producto mas caro es {nombre_mas_caro}\n")

        # Se escribe el valor total de la bodega
        salida.write(f"El valor total de la bodega es de ${total_bodega}\n")

        # Se escribe el nombre del producto que genero mas ingresos
        salida.write(f"El producto con mas ingresos es {producto_mas_ingresos}\n")

        # Se escribe el total de ventas del mes y año pedido
        salida.write(f"En el periodo de 10/2010, el total de ventas es de ${ventas_periodo}\n")


# Se llama a la funcion informe para que se ejecute todo
informe()

