from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def collect_files(pattern: str) -> list[Path]:
    return list(DATA_DIR.glob(pattern))


def pipeline() -> None:
    files = collect_files("*.txt")


if __name__ == "__main__":
    pipeline()
