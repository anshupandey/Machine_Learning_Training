# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:05:07 2018

@author: Anshu Pandey
"""

from flask import Flask,request,jsonify
from textblob import TextBlob
app=Flask(__name__)
@app.route('/demo',methods=['GET','POST'])
def newfun2():
    data=request.get_json(force=True)
    q=data['qus']
    ln=data['lang']
    q=TextBlob(q)
    ans=q.translate(to=ln)
    return jsonify(str(ans))

if __name__=='__main__':
    app.run(port=9000)
