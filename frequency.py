def char_frequency(str):
    freq = {}
    for char in str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
