from flask import Flask, request, jsonify
from transformers import pipeline
pipe = pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-cased")

app = Flask(__name__)

@app.route('/api_endpoint', methods=['POST'])
def api_endpoint():
    data = list(request.get_json().values())

    # Burada alınan veriyi işleyin ve sonucu hazırlayın
    
    result = {'response': your_classification_function(data[0]), 'received_data': data[0]}

    return jsonify(result)

def your_classification_function(input_data):
    # Burada sınıflandırma işlemlerini gerçekleştirin, örneğin:
    
    label = pipe(input_data)[0]["label"]
    return label

if __name__ == '__main__':
    app.run(debug=True)