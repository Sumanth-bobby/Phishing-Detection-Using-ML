from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the model
phish_model_ls = joblib.load('C:/Users/91798/Desktop/link/link/phishing.pkl')

# Render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# ML Aspect
@app.route('/predict', methods=['GET'])
def predict():
    feature = request.args.get('feature')
    X_predict = [str(feature)]

    try:
        prediction = phish_model_ls.predict(X_predict)[0]
        if prediction == 'bad':
            result = "This is a Phishing Site"
        else:
            result = "This is not a Phishing Site"
    except Exception as e:
        result = str(e)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
