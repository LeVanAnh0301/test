import os
from flask import Flask, redirect, render_template, request, url_for
from PIL import Image
import torchvision.transforms.functional as TF
import cnn
import numpy as np
import torch
import pandas as pd


# disease_info = pd.read_csv('disease_info.csv' , encoding='cp1252')
# supplement_info = pd.read_csv('supplement_info.csv',encoding='cp1252')

# model = CNN.CNN(39)    
# model.load_state_dict(torch.load("plant_disease_model_1_latest.pt"))
# model.eval()

# def prediction(image_path):
#     image = Image.open(image_path)
#     image = image.resize((224, 224))
#     input_data = TF.to_tensor(image)
#     input_data = input_data.view((-1, 3, 224, 224))
#     output = model(input_data)
#     output = output.detach().numpy()
#     index = np.argmax(output)
#     return index


app = Flask(__name__)
app.debug = True 

#màn hình start
@app.route('/')
def welcome():
    return redirect('/login')
 
# màn hình chính
@app.route('/home')
def home():
    return render_template('index.html')

# đăng ký
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            return redirect(url_for('home'))
        else:
            # return redirect(url_for('home'))
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

#màn hình đề xuất giải pháp và suggest sản phẩm
@app.route('/chatbox')
def chatbox_page():
    return render_template('chatbox.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         image = request.files['image']
#         filename = image.filename
#         file_path = os.path.join('static/uploads', filename)
#         image.save(file_path)
#         print(file_path)
#         pred = prediction(file_path)
#         title = disease_info['disease_name'][pred]
#         description =disease_info['description'][pred]
#         prevent = disease_info['Possible Steps'][pred]
#         image_url = disease_info['image_url'][pred]
#         supplement_name = supplement_info['supplement name'][pred]
#         supplement_image_url = supplement_info['supplement image'][pred]
#         supplement_buy_link = supplement_info['buy link'][pred]
#         return render_template('submit.html' , title = title , desc = description , prevent = prevent , 
#                                image_url = image_url , pred = pred ,sname = supplement_name , simage = supplement_image_url , buy_link = supplement_buy_link)

# @app.route('/market', methods=['GET', 'POST'])
# def market():
#     return render_template('market.html', supplement_image = list(supplement_info['supplement image']),
#                            supplement_name = list(supplement_info['supplement name']), disease = list(disease_info['disease_name']), buy = list(supplement_info['buy link']))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
