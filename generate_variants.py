import csv

producto_padre = [
    {"id": "remera-baki-hanma-pose", "outfit": "remera"},
    {"id": "buzo-baki-hanma-pose", "outfit": "buzo"},
]

# Define the variants for remeras and buzos
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


# Function to generate variants
def generate_variants(product, base_name, base_price, base_row):
    variants = []
    if "remera" in product:
        for color in remera_variants["color"]:
            for estilo in remera_variants["estilo"]:
                for talle in remera_variants["talle"]:
                    if (
                        color == remera_variants["color"][0]
                        and estilo == remera_variants["estilo"][0]
                        and talle == remera_variants["talle"][0]
                    ):
                        variant_row = base_row.copy()
                    else:
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
                        ]
                    variants.append(variant_row)
    elif "buzo" in product:
        for color in buzo_variants["color"]:
            for estilo in buzo_variants["estilo"]:
                for talle in buzo_variants["talle"]:
                    if (
                        color == buzo_variants["color"][0]
                        and estilo == buzo_variants["estilo"][0]
                        and talle == buzo_variants["talle"][0]
                    ):
                        variant_row = base_row.copy()
                    else:
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
                        ]
                    variants.append(variant_row)
    return variants


# File paths
input_file = "c:/Users/nikoo/Downloads/tiendanube-20250130.csv"
output_file = "c:/Users/nikoo/Downloads/tiendanube-20250130 - copia.csv"

# Read the original CSV and generate variants
with open(input_file, "r", encoding="utf-8") as infile, open(
    output_file, "w", newline="", encoding="utf-8"
) as outfile:
    reader = csv.reader(infile, delimiter=";")
    writer = csv.writer(outfile, delimiter=";")

    for row in reader:
        if len(row) > 0:
            for producto in producto_padre:
                if row[0] == producto["id"]:
                    variants = generate_variants(
                        producto["outfit"], row[0], row[8], row
                    )
                    writer.writerows(variants)
                    print(f"Variantes creadas para {producto['id']}")
                    break
            else:
                writer.writerow(row)
