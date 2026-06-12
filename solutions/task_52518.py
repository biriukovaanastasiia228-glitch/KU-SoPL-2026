# Student ID : 52518
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of all EVEN digits in your ID.           ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52518.py


def solve(id: str) -> int:
    total = 0

    for digit in id:
        if int(digit) % 2 == 0:
            total += int(digit)

    return total


if __name__ == "__main__":
    print(solve("52518"))
