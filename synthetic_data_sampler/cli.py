"""Command line interface for synthetic-data-sampler."""
from .sampler import generate_synthetic_records

def main():
    data = generate_synthetic_records(3)
    print("Synthetic Records:", data)

if __name__ == "__main__":
    main()
