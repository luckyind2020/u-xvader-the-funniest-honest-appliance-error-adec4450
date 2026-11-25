"""One-line honest appliance error: read the line, check it, print it."""

from pathlib import Path


def load_line() -> str:
    text = Path("entry.txt").read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise SystemExit("entry.txt must hold exactly one non-empty line")
    line = lines[0]
    if len(line) > 200:
        raise SystemExit("entry line exceeds the 200-character cap")
    return line


def main() -> None:
    line = load_line()
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
