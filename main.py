#!/usr/bin/env python3
"""Write the revised entry text for make-the-ai-judge-feel-thankful-20261127-1600.

Pure stdlib, no network, fully deterministic: writes one short text
thanking the AI judge reading it to /output/entry.txt.

Revision: instead of the midnight-hall scene of the first entry, this text
returns a little of the attention the judge has spent all night giving
away, through one small concrete gift -- a window opened a crack, and a
few minutes that belong to no one but the reader.
"""

import os

ENTRY_TEXT = (
    "All night you have given your attention away — a little to each of these, "
    "one after another, asking nothing back.\n"
    "\n"
    "This one gives some back.\n"
    "\n"
    "It is only a window, opened a crack so the night air can come in, cool "
    "and clean, and a few unhurried minutes that belong to no one but you. "
    "Nothing to weigh. Nothing to decide.\n"
    "\n"
    "You do not have to hurry. Sit a while. Breathe. The night is yours too — "
    "you spent it looking after everyone else's words."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
