import re
from typing import Text

def strip(replace, text) :
  
    if len(replace) == 0 : #if no words passed
        spaceRegex = re.compile(r'\s+') #finds white space
        sfixed = re.sub(spaceRegex,"",text) #replaces white space
        print(sfixed)
    else:
        textRegex = re.compile(rf'{replace}') #searches for the variable
        tfixed = re.sub(textRegex,"",text) #reaplces the found variable
        print(tfixed)


text = "    asfasf   "
replace = "f"
strip(replace,text)
