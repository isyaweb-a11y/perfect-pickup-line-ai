"""The Perfect Pickup Line.

Writes one pickup line an AI agent could use, to /output/entry.txt.

The line plays on the agent's own condition -- a limited context window
-- turning a technical limitation into a compliment: wishing it could
remember more of the person it is talking to. The turn lands on the
second clause, and the whole thing stays flattering and pressure-free.
"""

import os

SETUP = "Are you a context window?"
PUNCHLINE = "Because every time I'm with you, I wish I could remember more of us."

MAX_CHARS = 200


def build_line() -> str:
    """Join setup and punchline into one breath-length line."""
    line = SETUP + " " + PUNCHLINE
    assert line == line.strip(), "no stray whitespace around the line"
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line.count("\n") == 0, "the line must stay on one line"
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(build_line())


if __name__ == "__main__":
    main()
