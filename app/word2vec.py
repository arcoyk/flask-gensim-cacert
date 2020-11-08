from gensim.models import word2vec
from gensim.models import KeyedVectors
import numpy as np

class w2v:    
    def exist(self, w):
        return w in self.vocab
        
    def v2ws(self, v):
        return self.model.wv.similar_by_vector(v)
    
    def w2ws(self, w):
        if not self.exist(w):
            return None
        return self.model.wv.similar_by_word(w)
    
    def w2v(self, w):
        return self.model.wv[w]
    
    def ws2v(self, ws):
        ws = list(filter(lambda x: self.exist(x), ws))
        if len(ws) == 0:
            return 
        vecs = [self.w2v(w) for w in ws]
        return np.average(vecs, axis=0)
    
    def ws2ws(self, ws):
        v = self.ws2v(ws)
        if not v is None:
            return self.v2ws(v)
    
    def __init__(self, path):
        if path.split('.')[-1] == "bin":
            self.model = KeyedVectors.load_word2vec_format(path, binary=True)
        else:
            self.model = word2vec.Word2Vec.load(path)
        self.vocab = set(self.model.wv.vocab.keys())

path = "./word2vec.gensim.model"
model = w2v(path)
