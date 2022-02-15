#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask


# In[8]:


app = Flask(__name__)


# In[9]:


#dir(app)


# In[10]:


from flask import request, render_template
from keras.models import load_model

@app.route("/", methods = ["GET","POST"])
#the / is the 120.0.0.1:5000
def index():
    if request.method=="POST": #press submit come here
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model = load_model("BKRNN")
        pred = model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        print(pred)
        s = "The predicted bankruptancy score is:" + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__ == "__main__": #when name =/= main, sk.learn create error. u must run in main.
    app.run()


# In[ ]:




