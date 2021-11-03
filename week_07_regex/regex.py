import re

# This was an interesting task. While I had challenges running the program as a whole, I did use https://pythex.org/, plug in lines 8, 12, and 17 (after5 the "=" sign) and the codes worked. I am most interested in exploring gen regex on a deeper level. Quite intriguing. 

# Additionally, I have attached two samples of what the code on https://pythex.org/ displayed.


def find_names(line):
  # Find Mr. Mrs. Ms. or Dr. and last name (Smith)
  pattern = r"(Mr|Mrs|Ms.|Dr)\.?( [A-Z][a-z]*)( [A-Z][A-Za-z]*)*"
  result = re.findall(pattern,line)

# Find main character: UK teacher name
  pattern = r"Marjorie Smith"
  result = result + re.findall(pattern,line)
  return result

# Find other names, First and last name without Mr. Mrs. Ms. Dr.
  pattern = r"([A-Z][a-z]* [A-Z][a-z]*)"
  result = result + re.findall(pattern,line)
  return result