import csv
import json
import os


def main():
    input_file = "../data/products.json"

    if not os.path.exists(input_file):
        print(f"*** Error: File not found {input_file}. ***")
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

    with open(
        "../data/products_parent.csv", mode="w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(fields)

        for product in product_data:
            row = [product.get(field, "") for field in fields]
            writer.writerow(row)

    print("*** The products have been successfully created. ***")


if __name__ == "__main__":
    main()
