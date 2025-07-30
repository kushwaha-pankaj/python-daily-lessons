"""
unique_code_2025_07_31.py

This module demonstrates various Python concepts such as:
- Input validation
- Working with recursion
- Generators and list comprehensions
- Writing docstrings and following Pythonic conventions

The script includes functionality to compute factorial of a number,
generate prime numbers up to a limit, and perform quick sort on a list.

Run this module directly to see example usage of each function.
"""

from typing import Iterable, Iterator, List


def factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer using recursion."""
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(limit: int) -> Iterator[int]:
    """Generate prime numbers less than a given limit."""
    for number in range(2, limit):
        if is_prime(number):
            yield number


def quick_sort(arr: List[int]) -> List[int]:
    """Sort a list of integers using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # Example usage
    print("Factorial of 5:", factorial(5))
    print("Primes less than 20:", list(generate_primes(20)))
    sample_list = [3, 6, 2, 7, 5, 8, 1, 4]
    print("Original list:", sample_list)
    print("Sorted list:", quick_sort(sample_list))
