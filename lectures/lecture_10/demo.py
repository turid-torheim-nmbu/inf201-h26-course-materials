import argparse


def main():
    parser = argparse.ArgumentParser(description="Argparse demo with an optional flag.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("-n", "--n_greet", type=int, default=1, help="Number of greetings wanted")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode is ON.")

    for _ in range(args.n_greet):
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
