# Fase 5 - Evaluación Final POA
# Curso: Fundamentos de Programación
# Problema 2: Aplicación de promociones a productos de un menú

# Matriz del menú: [Nombre del producto, Categoría, Precio base]
menu = [
    ["Bandeja paisa", "Platos principales", 38000],
    ["Hamburguesa artesanal", "Platos principales", 32000],
    ["Lomo de res", "Platos principales", 45000],
    ["Arepa de queso", "Entradas", 12000],
    ["Ensalada de frutas", "Postres", 16000],
    ["Limonada natural", "Bebidas", 9000],
    ["Cheesecake", "Postres", 18000],
    ["Pasta Alfredo", "Platos principales", 30000]
]

# Constantes de la promoción
CATEGORIA_OBJETIVO = "Platos principales"
UMBRAL_PRECIO = 30000
PORCENTAJE_DESCUENTO = 0.15


def calcular_precio_final(producto, categoria_objetivo, umbral, descuento):
    """
    Calcula el precio final de un producto.
    Aplica el descuento únicamente si pertenece a la categoría objetivo
    y su precio base es mayor que el umbral establecido.
    """
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * (1 - descuento)
    else:
        precio_final = precio_base

    return precio_final


def mostrar_informe(productos):
    """Muestra el precio base y el precio final de cada producto."""
    print("\n========== PROMOCIÓN DEL RESTAURANTE ==========")
    print(f"Categoría objetivo: {CATEGORIA_OBJETIVO}")
    print(f"Condición de precio: mayor a ${UMBRAL_PRECIO:,.0f}")
    print(f"Descuento: {PORCENTAJE_DESCUENTO * 100:.0f}%")
    print("-" * 78)
    print(f"{'PRODUCTO':25} {'PRECIO BASE':15} {'PRECIO FINAL':15} {'RESULTADO'}")
    print("-" * 78)

    for producto in productos:
        precio_final = calcular_precio_final(
            producto,
            CATEGORIA_OBJETIVO,
            UMBRAL_PRECIO,
            PORCENTAJE_DESCUENTO
        )

        if precio_final < producto[2]:
            resultado = "Descuento aplicado"
        else:
            resultado = "Sin descuento"

        print(
            f"{producto[0]:25} "
            f"${producto[2]:>12,.0f} "
            f"${precio_final:>12,.0f} "
            f"{resultado}"
        )

    print("-" * 78)


# Programa principal
mostrar_informe(menu)
