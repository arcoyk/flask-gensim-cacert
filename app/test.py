from flask import Flask, jsonify
from gensim.models import word2vec
from gensim.models import KeyedVectors
import numpy as np

path = "./word2vec.gensim.model"
model = word2vec.Word2Vec.load("word2vec.gensim.model")

app = Flask(__name__)
@app.route("/")
def index():
	v = model.wv.similar_by_word("dog")
	return jsonify(v)

if __name__=='__main__':
	app.run(host='0.0.0.0', port=80)
