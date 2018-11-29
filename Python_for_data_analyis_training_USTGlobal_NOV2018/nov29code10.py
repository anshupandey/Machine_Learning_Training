# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:52:49 2018

@author: Anshu Pandey
"""

from flask import Flask
app=Flask(__name__)
@app.route('/demo',methods=["GET","POST"])
def mainfunction():
    data="""
    <html>
<body><center><h1>welcome to Data Science Dashboard
</h1><br><br><br><br><br><br><hr><hr></body></html>
    """
    return data

if __name__=='__main__':
    app.run(port=9000)
