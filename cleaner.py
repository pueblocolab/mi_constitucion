import re

uni_pattern = r"\\u.{4}"
nl_pattern_space_after = r"\\n\s"
nl_pattern_space_before = r"\s\\n"


# Converts csv to dictionary
def csv_to_dict(file):
    csv_reader = csv.reader(open(file))
    d = {}
    for row in csv_reader:
        d[row[0]] = row[1]
    return d

# Replaces character with another character
def replace_uni(text, pattern): 
    matches = re.finditer(pattern, text, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1): 
        word = match.group()
        replacement = code_dict[word]
        text = text.replace(word, replacement)
    return text

# Load unicode dictionary
code_dict = csv_to_dict('/Users/cathyr/GitHub/pueblo_colab/mi_constitucion/unicodetable.csv')



