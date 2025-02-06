import csv
import json
import os


def main():
    input_file = "../data/products.json"

    if not os.path.exists(input_file):
        print(f"Error: No se encontró el archivo {input_file}.")
        return

    with open(input_file, "r", encoding="utf-8") as file:
        product_data = json.load(file)

    fields = [
        "Identificador de URL",
        "Nombre",
        "Categorías",
        "Nombre de propiedad 1",
        "Valor de propiedad 1",
        "Nombre de propiedad 2",
        "Valor de propiedad 2",
        "Nombre de propiedad 3",
        "Valor de propiedad 3",
        "Precio",
        "Precio promocional",
        "Peso (kg)",
        "Alto (cm)",
        "Ancho (cm)",
        "Profundidad (cm)",
        "Stock",
        "SKU",
        "Código de barras",
        "Mostrar en tienda",
        "Envío sin cargo",
        "Descripción",
        "Tags",
        "Título para SEO",
        "Descripción para SEO",
        "Marca",
        "Producto Físico",
        "MPN (Número de pieza del fabricante)",
        "Sexo",
        "Rango de edad",
        "Costo",
    ]

    product = [product_data.get(field, "") for field in fields]

    with open(
        "../data/parent_products.csv", mode="w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(fields)
        writer.writerow(product)

    print("El producto ha sido creado con éxito.")


if __name__ == "__main__":
    main()
