# Student ID : 52548
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of digits strictly greater than 4.       ║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52548.py


def solve(id: str) -> int:
    return sum(int(char) for char in id if char.isdigit() and int(char) > 4)


if __name__ == "__main__":
    print(solve("52548"))
