import create_parent_product
import generate_variants


def main():
    print()
    print("Creating parent products...")
    create_parent_product.main()

    print()

    print("Generating variants...")
    generate_variants.main()
    print()


if __name__ == "__main__":
    main()
