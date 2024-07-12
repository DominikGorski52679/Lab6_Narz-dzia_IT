# args_parser.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="Argument parser")
    parser.add_argument('--example', type=str, help="Example argument")
    args = parser.parse_args()
    print(f"Argument: {args.example}")

if __name__ == "__main__":
    main()