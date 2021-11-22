from flask import Flask, request, render_template, jsonify, json 
app = Flask(__name__)

import os
import jinja2
import argparse


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/updatetext', methods=['POST'])
def updatetext(title):
    title =title
    return render_template(   
        'index.html', title=title )

#   server.updatetext("heyho")

#@app.route('/', methods=['POST'])
#def noreturn():
  #print("yes, ich werde ausgeführt")
  #return render_template('index.html',gifstoff="generate.gif")
#print("log")

@app.route('/', methods=['POST'])
def my_form_post():
    in_text = request.form['text']

    with open("data/out.csv", "r+") as himmel:
      top = himmel.read()

    if (str(in_text) not in str(top)):
      return render_template('index.html',data="Missing Data - 'Menschen' Eike hat darüber noch keinen Witz geschrieben.")  

    else:

      out_result=('')
      
      for x in range(3):
        print (x)
        x=x+1
        import train 
        from train import dataset, model, predict 
        #train.predict(dataset,model,text)
        #besult= train.train(dataset,model,args)
        text_result= train.predict(dataset, model, in_text, next_words=9)
        print(text_result)
        out_result=out_result+text_result +" \n"
        

      #holy = open("end.txt", "r+")
      #bdata = holy.read()
      #holy.truncate(0)
      #holy.close()

      #hell = open("input.txt","r+")
      #hell.truncate(0)
      #hell.close()
      #render_template('index.html',data=out_result)
    return render_template('index.html',data=out_result)


if __name__ == '__main__':
  app.run(debug=True)
  import argparse
