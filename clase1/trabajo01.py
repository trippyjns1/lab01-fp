

precios = [120 , 40 , 80]
total_cliente = 0

for precio in precios:
    if precio > 50:
        descuento = precio * 0.9
        print(f"Obtuvo un descuento de: ${descuento}")
    elif precio <= 50:
        descuento = 0
        print("No obtuvo ningun descuento")


    total_cliente += descuento