from flask import Flask, render_template
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator defines the   
def home():  
    return render_template('index.html')
  
if __name__ =='__main__':  
    app.run(debug = True,port=8080) #if any errors occur they will pop up on the webpage 