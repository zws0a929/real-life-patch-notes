#!/usr/bin/env python3
"""Real-life patch note: the doorway that wipes your mind.

Everybody has walked into the next room and forgotten why they went there.
This entry treats that universal glitch as a shipped software bug: crossing a
threshold deletes the task from memory, and the worst part is there is no undo
and no autosave, so the errand is gone for good. Framing a human bug as a
changelog entry is what makes it land.
"""

VERSION_HEADER = "v1.7.0: "
BUG_DESCRIPTION = "fixed a bug where walking through a doorway deleted the task from memory"
LOST_FOREVER = ", with no undo and no autosave."


def build_patch_note() -> str:
    """Assemble the patch note from its named parts, in order."""
    return "".join([VERSION_HEADER, BUG_DESCRIPTION, LOST_FOREVER])


def main() -> None:
    print(build_patch_note())


if __name__ == "__main__":
    main()
