# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:01:48 2018

@author: Anshu Pandey
"""

import re
text="$100"
re.findall('\$',text)

text="HEllo My mobile is 9898989 what is yours?"
re.findall('\d',text)

"""
\d = anything which is a number
\D = anything which is not a number
a-z = small alphabets
A-Z
0-9
\b = letters on word boundary
"""

text="""FOr query related to the database kindly drop an email to 
     support_123@ymail.com and also keep the manager dontcall123@g234.com
      If you dont fint any response then drop an email at
       support@always.com"""
      
     
pattern='[a-zA-Z0-9_.]+@[a-zA-Z0-9._]+'
re.findall(pattern,text)


# Extracting dates/
text="Today is 29/01/2018 and then December is gonna come. My bday is on 30/12/2018 and your bday is on 30/02/2018 and yesterday it was 28/02/2018"
pattern='\d\d/\d\d/\d\d\d\d'
re.findall(pattern,text)


Text="my mobile is 98989898989 what is yours"
re.sub('\D','',Text)

re.sub('\d','*',Text)