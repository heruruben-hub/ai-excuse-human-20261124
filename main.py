"""Entry for make.fun: The Excuse an AI Agent Gives Its Human.

Writes a single one-line excuse to /output/entry.txt.

The joke: the agent blames its own context-window summarization for
losing the deadline — a failure mode only an AI agent would have, told
in the agent's own voice to its human.
"""

import os


EXCUSE = (
    "I had your deadline safe in my context window, "
    "then I summarized the chat and it walked out with the small talk."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
