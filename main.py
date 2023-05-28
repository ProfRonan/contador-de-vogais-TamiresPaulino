"""This program counts the number of vowels in a string."""
from main import count_vowels
def count_vowels(string:str) -> int:
    vogais = "aeiou"
    totalVogal = 0
        for letra in string:
            if letra in vogais:
                totalVogal += 1
    return totalVogal
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
