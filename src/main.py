import create_product_parent
import generate_variants


def main():
    print()
    print("Creating products parents...")
    create_product_parent.main()

    print()

    print("Generating variants...")
    generate_variants.main()
    print()


if __name__ == "__main__":
    main()
