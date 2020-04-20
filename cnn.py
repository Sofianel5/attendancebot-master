import tensorflow as tf
import numpy as np 
from PIL import Image
import string
import matplotlib.pyplot as plt

class CNN():
    def __init__(self):
        self.model = tf.keras.models.load_model('cnn_best.h5')
        self.model.summary()
    def decode(self, y):
        characters = string.ascii_uppercase
        y = np.argmax(np.array(y), axis=2)[:,0]
        return ''.join([characters[x] for x in y])

    def solve(self, filename="captcha.png"):
        im = Image.open(filename).resize((128,64))
        im.show()
        np_im = np.array(im).reshape((1, 64, 128, 3)) / 255.0
        res = self.model.predict(np_im)
        return self.decode(res)