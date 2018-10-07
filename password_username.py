#--------------------------------------------------------------------------------
# Random Password Generator
#--------------------------------------------------------------------------------
import string
import random

# List of usable characters, ignoring commonly confused ones
CHARS = [x for x in string.ascii_letters+string.digits \
         if x not in ['i','I','l','L','o','O','0','1']]

def gen_password(size=8, chars=CHARS):
  # By default creates a random 8 character password
    return ''.join(random.choice(chars) for i in range(size))

#--------------------------------------------------------------------------------
# Basic Username generator
#--------------------------------------------------------------------------------
def gen_username(in_data):
  # Takes a regular name (first & last) and creates a lowercase username
  # IE: 'John Doe' becomes jdoe
    first, last = in_data.lower().split(' ')
    return first[0]+last

#--------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------
