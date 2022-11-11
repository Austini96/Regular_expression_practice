# return match object if S matches the date format, and if not, False
#   mm-dd-yy or mm/dd/yy
#   mm-dd-yyyy or mm/dd/yyyy

import re

# my code
# def matchDate(S):
#   m = re.match('^(?:[0]{0,1}[0-9]{1}|[1]{1}[0-2]{1})(?:-[0-3]{0,1}[0-9]{1}-|/[0-3]{0,1}[0-9]{1}/)([0-9]{2,4})$', S)
#   if type(m) == re.Match:
#     return m
#   else:
#     return False

# more concise code
def matchDate(S):
  return(re.match("^[01]?\d([-/])[0123]?\d\\1([12]\d)?\d\d$", S) or False)
  
# The use of predefined code can make the code for the regular expression more concise
