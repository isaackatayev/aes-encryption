from flask import Flask,request,redirect,Response, render_template,render_template_string, send_file
import requests
from bs4 import BeautifulSoup

import aes

config = {
    "DEBUG": True,          
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__, template_folder = "templates")
@app.route("/")
def index():
    return redirect("/encrypt", code=301)
 

@app.route("/encrypt")
def encrypt():
    return render_template("encrypt.html")
@app.route("/decrypt")
def decrypt():
    return render_template("decrypt.html")
@app.route('/encrypt', methods=['POST'])
def enc():
  try:
    
    plaintext = request.form['plaintext']
    iv = request.form['iv']
    key = request.form['key']
    encrypted = aes.encrypt(key,iv,plaintext)
    
    html0 = str(render_template("encrypt.html"))
    soup = BeautifulSoup(html0, 'html.parser')
    div1 = soup.find(class_='div1')
    a1 = soup.new_tag("a")
    a2 = soup.new_tag("a")
    desc1 = soup.find(class_='description')
    a1.attrs['href'] = "/returntoencrypt"
    a2.attrs['href'] = "/returntodecrypt"
    a1.attrs['style'] = "color:black;"
    a2.attrs['style'] = "color:black;"
    break0 = soup.new_tag("br")
    par = soup.new_tag("p")
    a1.append("Return to AES Encryption page")
    a2.append("Return to AES Decryption page")
    div1.clear()
    desc1.decompose()
    div1.append("AES Ciphertext (Encoded with Base64): \n ")
    div1.append(break0)
    div1.append(break0)
    div1.append(break0)
    par.append(encrypted)
    
    div1.append(par)
    
    div1.append(soup.new_tag("br"))
    div1.append(a1)
    div1.append(soup.new_tag("br"))
    div1.append(a2)
    
    soup.find("p")['class'] = "result"
    
    
    
    return str(soup)
  except ValueError as err:
    return "<script>window.alert('Error: " + str(err) + "'); window.location.replace('/');</script>"
  except:
    "<script>window.alert('An unknown error has occured. Please make sure your AES key and IV are the correct sizes.'); window.location.replace('/');</script>"
    
    #return text
    #return text
@app.route('/decrypt', methods=['POST'])
def dec():
  try:
    
    ciphertext = request.form['ciphertext']
    iv = request.form['iv']
    key = request.form['key']
    encrypted = aes.decrypt(key,iv,ciphertext)
    html0 = str(render_template("decrypt.html"))
    soup = BeautifulSoup(html0, 'html.parser')
    div1 = soup.find(class_='div1')
    
    a1 = soup.new_tag("a")
    a2 = soup.new_tag("a")
    par = soup.new_tag("p")
    a1.attrs['href'] = "/returntoencrypt"
    a2.attrs['href'] = "/returntodecrypt"
    a1.attrs['style'] = "color:black;"
    a2.attrs['style'] = "color:black;"
    
    a1.append("Return to AES Encryption page")
    a2.append("Return to AES Decryption page")
    div1.clear()
    div1.append("Decrypted message: \n")
    div1.append(soup.new_tag("br"))
    
    par.append(encrypted)
    
    
    div1.append(par)
    div1.append(soup.new_tag("br"))
    div1.append(a1)
    div1.append(soup.new_tag("br"))
    div1.append(a2)
    
    
    soup.find("p")['class'] = "result"
    
    
    
    
    return str(soup)
  except ValueError as err:
    return "<script>window.alert('Error: " + str(err) + "'); window.location.replace('/returntodecrypt');</script>"
  except:
    "<script>window.alert('An unknown error has occured. Please make sure your AES key and IV are the correct sizes.'); window.location.replace('/');</script>"
    
    
@app.route("/returntoencrypt")
def reutntoencrypt():
    return redirect("/encrypt", code=301)
@app.route("/returntodecrypt")
def reutntodecrypt():
    return redirect("/decrypt", code=301)
if __name__ == "__main__":
    app.run(debug = False, host="0.0.0.0",port=8080)

  