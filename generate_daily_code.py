"""
generate_daily_code.py

This script automatically generates a new Python file each day with
unique, human-like code examples. The generated file includes functions
that demonstrate different programming concepts, and its name includes
the current date.

You can run this script manually or schedule it (e.g. via GitHub Actions)
to keep your repository active.

"""

import datetime
import random
import textwrap


def generate_code_content(date_str: str) -> str:
    """Return a Python module string containing unique content for the given date."""
    tasks = [
        (
            "fibonacci",
            "Compute the nth Fibonacci number iteratively.",
            textwrap.dedent(
                """\
                def fibonacci(n: int) -> int:
                    """Return the nth Fibonacci number using an iterative method."""
                    a, b = 0, 1
                    for _ in range(n):
                        a, b = b, a + b
                    return a
                """
            ),
        ),
        (
            "factorial",
            "Compute the factorial of a non-negative integer recursively.",
            textwrap.dedent(
                """\
                def factorial(n: int) -> int:
                    """Return the factorial of n using recursion."""
                    if n < 0:
                        raise ValueError("n must be non-negative")
                    return 1 if n <= 1 else n * factorial(n - 1)
                """
            ),
        ),
        (
            "is_palindrome",
            "Check if a given string is a palindrome.",
            textwrap.dedent(
                """\
                def is_palindrome(s: str) -> bool:
                    """Check if a given string is a palindrome ignoring non-alphanumeric characters."""
                    cleaned = ''.join(c.lower() for c in s if c.isalnum())
                    return cleaned == cleaned[::-1]
                """
            ),
        ),
        (
            "sum_of_squares",
            "Calculate the sum of squares of numbers up to n.",
            textwrap.dedent(
                """\
                def sum_of_squares(n: int) -> int:
                    """Return the sum of squares from 1 to n."""
                    return sum(i * i for i in range(1, n + 1))
                """
            ),
        ),
        (
            "quick_sort",
            "Sort a list of integers using the Quick Sort algorithm.",
            textwrap.dedent(
                """\
                def quick_sort(arr: list[int]) -> list[int]:
                    """Return a new sorted list using the Quick Sort algorithm."""
                    if len(arr) <= 1:
                        return arr
                    pivot = arr[len(arr) // 2]
                    left = [x for x in arr if x < pivot]
                    middle = [x for x in arr if x == pivot]
                    right = [x for x in arr if x > pivot]
                    return quick_sort(left) + middle + quick_sort(right)
                """
            ),
        ),
    ]

    # Randomly select 2 tasks to include
    chosen_tasks = random.sample(tasks, k=2)
    doc_lines = [f"- {desc}" for (_, desc, _) in chosen_tasks]
    code_blocks = [code.strip() for (_, _, code) in chosen_tasks]

    header = textwrap.dedent(
        f"""\
        """daily_code_{date_str}.py

        This module was auto-generated on {date_str}.
        It includes several example functions for demonstration purposes:

        {'\n'.join(doc_lines)}

        Feel free to modify or expand upon this code.
        """
        """
    )
    return header + "\n\n" + "\n\n".join(code_blocks)


def main() -> None:
    today = datetime.datetime.now().strftime("%Y_%m_%d")
    filename = f"daily_code_{today}.py"
    content = generate_code_content(today)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Generated {filename}")


if __name__ == "__main__":
    main()
