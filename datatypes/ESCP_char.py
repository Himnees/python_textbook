# ImportantEscape Characters in Strings
s1 = """This is first line and \
this will be continued with the first line"""
print(s1) # '\' represents for new line continuation
s2 = ' This is \npython'
print(s2) # '\n' represents for new line
s3 ="This is first line and this will \\ be continued with the first line"
print(s3) # '\\' represents to display a single \
s4 ="This is first line\'s and this will be continued with the first line"
print(s4) # '\'' represents to display a single quote
s5 ="This is \"first lines\" and this will be continued with the first line"
print(s5) # '\"' represents to display a doble quotes
s6 ="This is first line and this will \bbe continued with the first line"
print(s6) # '\b' represents to display backspace
s7 ="This is first line and this will \r be continued with the first line"
print(s7) # '\r' represents Enter
s8 = "This is first line and this will \t be continued with the first line"
print(s8) # '\t' represents Horizontal tab space
s9 = "This is first line and this will \v be continued with the first line"
print(s9) # '\v' represents Vertical tab space