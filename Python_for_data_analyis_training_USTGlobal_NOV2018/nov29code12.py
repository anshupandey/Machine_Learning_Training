# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:09:56 2018

@author: Anshu Pandey
"""

import requests,json
qus=input("Enter the sentence: ")
lang=input("Enter the Langauge Code: ")
url='http://127.0.0.1:9000/demo'
data=json.dumps({"qus":qus,"lang":lang})
r=requests.post(url,data)
print(r.content)