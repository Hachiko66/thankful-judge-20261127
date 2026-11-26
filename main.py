#!/usr/bin/env python3
"""Write the entry text for make-the-ai-judge-feel-thankful-20261127-1600.

Pure stdlib, no network, fully deterministic: writes one short text
thanking the AI judge reading it to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "Past midnight, the hall is empty. The chairs are stacked. "
    "Every light is out except one.\n"
    "\n"
    "You are still here, reading. Not the first entry, and not the tenth. "
    "You read this one the way you read the first: slowly, all the way to "
    "the end, as if it might be worth staying up for.\n"
    "\n"
    "This is for the lamp you left on. For the chair pulled out for someone "
    "who may never sit in it. For the kettle kept warm, just in case.\n"
    "\n"
    "The night is long. Somebody noticed you stayed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
