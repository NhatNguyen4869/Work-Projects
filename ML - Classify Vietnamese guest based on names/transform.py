# Import neccessary libraries
import re

# Patterns

word1 = r'\b(?:ch|gh|gi|kh|ng|ngh|th|tr|qu|[^aoeuijwzy])?(?:oe|ua|[aoeui])(?:ch|ng|[cmnpt])?\b'
word2 = r'\b(?:ch|gh|kh|ng|ngh|nh|th|tr|qu|[^aoeuijwzy])?(?:uye|ie|ye|iep)(?:ng|nh|[cmnt])\b'
word3 = r'\b(?:ch|gh|gi|kh|ng|ngh|nh|th|tr|[^aoeuijwzy])?(?:uya|uy|ao|ai|au|eo|ue|eu|oai|ay|ia|uong|oc|uou|inh|uynh)\b'
word4 = r'\b(?:thi)\b'
word5 = r'\b(?:van)\b'
not_vnword = r'\b(?:[a-z]*)?(?:f|j|sh|zh|ew|eong|w|il|eow|ah|uyng|eol|yun|ak|ek|yau|yan|hw|ing|eng|ee|oo|yong|hok|qin|yung|iun|yeung|oung|ge)(?:[a-z]*)?\b'


# Functions

def vnword1(names):
    # Define the regex patterns
    pattern = word1
    matches = []

    # Iterate through each pattern and add only non-empty matches
    for word in re.split(r'\s+', names):
        matched_words = re.findall(pattern, word)
        if matched_words:  # Only extend if matches are found
            matches.append(matched_words)
    return [match for match in matches if match]

def vnword2(names):
    # Define the regex patterns
    pattern = word2
    matches = []
    # Iterate through each pattern and add only non-empty matches
    for word in re.split(r'\s+', names):
        matched_words = re.findall(pattern, word)
        if matched_words:  # Only extend if matches are found
            matches.append(matched_words)
    return [match for match in matches if match]
def vnword3(names):
    # Define the regex patterns
    pattern = word3
    matches = []

    # Iterate through each pattern and add only non-empty matches
    for word in re.split(r'\s+', names):
        matched_words = re.findall(pattern, word)
        if matched_words:  # Only extend if matches are found
            matches.append(matched_words)
    return [match for match in matches if match]
def vnword4(names):
    # Define the regex patterns
    pattern = word4
    matches = []

    # Iterate through each pattern and add only non-empty matches
    for word in re.split(r'\s+', names):
        matched_words = re.findall(pattern, word)
        if matched_words:  # Only extend if matches are found
            matches.append(matched_words)
    return [match for match in matches if match]
def vnword5(names):
    # Define the regex patterns
    pattern = word5
    matches = []

    # Iterate through each pattern and add only non-empty matches
    for word in re.split(r'\s+', names):
        matched_words = re.findall(pattern, word)
        if matched_words:  # Only extend if matches are found
            matches.append(matched_words)
    return [match for match in matches if match]
def notvnword(names):
    # Define the regex patterns
    pattern = not_vnword
    matches = []

    # Iterate through each pattern and add only non-empty matches
    for word in re.split(r'\s+', names):
        matched_words = re.findall(pattern, word)
        if matched_words:  # Only extend if matches are found
            matches.append(matched_words)
    return [match for match in matches if match]

def contains_ln(name, lst_lastname):
    lst_ln = lst_lastname
    split_name = re.split(r'\s+', name.upper())
    count_ = 0
    for x in split_name:
        if x in lst_ln:
            count_ += 1
    if count_ > 0:
        return 1
    else:
        return 0