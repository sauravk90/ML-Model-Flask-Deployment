import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/api',methods=['POST'])
def hello():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
    # dic = {'experience':10, 'test_score':5, 'interview_score':6}
    # x = np.array(list(dic.values()))
    # print(x)
    # print(type(x))