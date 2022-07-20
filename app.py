import requests
from flask import Flask,render_template,url_for
from flask import request as req
from sentence_splitter import SentenceSplitter
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/grammarCorrector",methods=["GET","POST"])
def grammarCorrector():

    
        
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction"
        headers = {"Authorization": f"Bearer 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"}


        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        data=req.form["data"]
        if len(data)>26:
            splitter = SentenceSplitter(language='en')
            sentence_list = splitter.split(data)
            output2 = []
            for sentence in sentence_list:
                output1 = query({"inputs": sentence})
                output2.append(output1)
            output = ' '.join([str(elem) for elem in output2])
            return render_template("index.html",result=output)  
        else: 
            output = query({"inputs": data})
            return render_template("index.html",result=output)
        
        
    else:
        return render_template("index.html")