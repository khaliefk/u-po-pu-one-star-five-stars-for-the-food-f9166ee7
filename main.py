#!/usr/bin/env python3
"""Write a one-star alien review of Earth to /output/entry.txt.

Stdlib only. The review is a single sentence, at most 200 characters:
an alien tourist's one-star review of Earth that still compliments the food.
"""

import os

ENTRY = (
    "One star: my rental saucer got towed, the locals worship glowing "
    "rectangles, and gravity keeps stealing my socks, but the tacos are "
    "so good I almost forgave this planet."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
