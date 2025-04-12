import re
from collections import Counter

def calculate_readability_score(text: str) -> float:
    # Simple Flesch Reading Ease formula (rough estimate)
    sentence_count = max(text.count("."), 1)
    word_list = text.split()
    word_count = len(word_list)
    syllable_count = sum(count_syllables(word) for word in word_list)

    ASL = word_count / sentence_count  # Average Sentence Length
    ASW = syllable_count / word_count  # Average Syllables per Word
    score = 206.835 - (1.015 * ASL) - (84.6 * ASW)
    return round(score, 2)

def count_syllables(word: str) -> int:
    return len(re.findall(r"[aeiouy]+", word.lower()))

def keyword_density(text: str, keyword: str) -> float:
    words = re.findall(r'\w+', text.lower())
    keyword_count = words.count(keyword.lower())
    return round((keyword_count / len(words)) * 100, 2)
