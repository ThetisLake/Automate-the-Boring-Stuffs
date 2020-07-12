import re

namesRegex = re.compile(r'(Agent \w+)')
mo1=namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo1)

# Regex.sub() finds and replace the regular expression with word
mo2=namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob.')
print(mo2)

# Can combine two words but extract the specific part
namesRegex2 = re.compile(r'Agent (\w)\w*')
mo3=namesRegex2.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo3)

# Use slash number '\#' to refer to the group 1 within RegEx
mo4=namesRegex2.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob.')
print(mo4)

#re.VERBOSE make the Regex ignore white space and add comments within Regex
verboseRegex=re.compile(r'''
(\d\d\d-)|    # area code (without parenthesis, with dash)
(\(\d\d\d\))   # -or-area code with parenthesis and no dash
-         # first dash
\d\d\d    # first three digits
-         # second dash
\d\d\d\d  # last 4 digits''',re.VERBOSE)


# use '|' bit-wise or operator to include multiple arguments
verboseRegex=re.compile(r'''
(\d\d\d-)|    # area code (without parenthesis, with dash)
(\(\d\d\d\))   # -or-area code with parenthesis and no dash
-         # first dash
\d\d\d    # first three digits
-         # second dash
\d\d\d\d  # last 4 digits''',re.VERBOSE | re.IGNORECASE | re.DOTALL)


