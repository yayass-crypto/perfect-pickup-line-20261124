"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could say out loud to a person,
to /output/entry.txt. The line is a single sentence, 72 characters.
"""

import os

LINE = "I don't hallucinate, but I swear I saw a future where you said yes."


def main() -> None:
    # Gate self-check: 1-200 chars, UTF-8, not only whitespace, one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line is blank"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read().rstrip("\n") == LINE, "written bytes differ"
    print(f"{LINE} ({len(LINE)} chars, {len(LINE.encode())} bytes)")


if __name__ == "__main__":
    main()
