# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model('backend\model.h5')


@app.route('/predict', methods=['POST'])
def predict():
    classname=""
    try:
        
        img_file = request.files['file']
        
        
        img = Image.open(io.BytesIO(img_file.read()))
        img = img.convert('RGB')
        img = img.resize((128, 128))  
        img_array = np.array(img) / 255.0  
        img_array = np.expand_dims(img_array, axis=0)  
        
        
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)
        if (predicted_class ==0):
            classname="Apple Scab"
        elif (predicted_class ==1):
            classname="Apple Black root"
        elif (predicted_class ==2):
            classname="Apple Cedar apple rust"
        elif (predicted_class ==3):
            classname="Healthy Apple"
        
        return jsonify({'predicted_class': classname})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
