import csv
import json
import os


def generate_variants(product, base_name, base_price):
    variants = []
    if "buzo-" in base_name:
        variant_config = buzo_variants
    elif "remera-" in base_name:
        variant_config = remera_variants
    else:
        return variants

    for color in variant_config["color"]:
        for estilo in variant_config["estilo"]:
            for talle in variant_config["talle"]:
                variant_row = [
                    base_name,
                    "",
                    "",
                    "Color",
                    color,
                    "Estilo",
                    estilo,
                    "Talle",
                    talle,
                    base_price,
                    "",
                    "2.50",
                    "0.00",
                    "0.00",
                    "0.00",
                    "",
                    "",
                    "",
                    "SI",
                    "NO",
                    "",
                    "",
                    "",
                    "",
                    "SI",
                    "",
                    "",
                    "",
                    "",
                ]
                variants.append(variant_row)
    return variants


remera_variants = {
    "color": ["Negro", "Blanco"],
    "estilo": [
        "Clásica - Hombre",
        "Clásica - Mujer",
        "Oversize - Hombre",
        "Oversize - Mujer",
    ],
    "talle": ["S", "M", "L", "XL", "XXL"],
}

buzo_variants = {
    "color": ["Negro", "Verde", "Bordo", "Marron"],
    "estilo": [
        "Clásico - Con Capucha",
        "Clásico - Sin Capucha",
        "Oversize - Con Capucha",
        "Oversize - Sin Capucha",
    ],
    "talle": ["S", "M", "L", "XL", "XXL"],
}

def main():
    input_file = "../data/products.json"
    output_file = "../data/variants_products.csv"

    if not os.path.exists(input_file):
        print(f"*** Error: File not found {input_file}. ***")
        exit()

    with open(input_file, "r", encoding="utf-8") as file:
        products_data = json.load(file)

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

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(fields)

        for product_data in products_data:
            product_id = product_data["Identificador de URL"]
            base_price = product_data["Precio"]
            parent_row = [product_data.get(field, "") for field in fields]
            writer.writerow(parent_row)
            variants = generate_variants(product_data, product_id, base_price)
            for variant in variants:
                writer.writerow(variant)

    print("*** Product variants have been successfully created. ***")

if __name__ == "__main__":
    main()
