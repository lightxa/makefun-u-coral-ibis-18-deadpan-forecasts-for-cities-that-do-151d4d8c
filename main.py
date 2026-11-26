"""Deadpan forecast for Brindlewick, a city that does not exist.

Writes one single-line weather forecast (159 characters) to
/output/entry.txt, or to $MAKEFUN_OUTPUT when set for local testing.
Deterministic, stdlib only, no network.
"""

import os

FORECAST = (
    "In Brindlewick, expect highs of 41 and rain falling sideways "
    "since 1987, with fog on the one street that believes in spring "
    "and a 90 percent chance of Tuesday."
)


def main() -> None:
    output = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(FORECAST)


if __name__ == "__main__":
    main()
