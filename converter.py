import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Convert temperature between Celsius and Fahrenheit"
    )

    parser.add_argument("value", type=float, help="Temperature value to convert")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--to-celsius", action="store_true", help="Convert to Celsius")
    group.add_argument("--to-fahrenheit", action="store_true", help="Convert to Fahrenheit")

    parser.add_argument(
        "--precision",
        type=int,
        default=2,
        help="Decimal precision (default: 2)"
    )

    args = parser.parse_args()

    precision = args.precision

    if args.to_celsius:
        result = fahrenheit_to_celsius(args.value)
        print(f"{args.value}°F is {round(result, precision)}°C")
    elif args.to_fahrenheit:
        result = celsius_to_fahrenheit(args.value)
        print(f"{args.value}°C is {round(result, precision)}°F")

if __name__ == "__main__":
    main()
