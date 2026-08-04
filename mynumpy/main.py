import random
from random import randrange

import numpy as np
import sentence_transformers
from sentence_transformers import util, SentenceTransformer
import matplotlib.pyplot as plt
time = np.linspace(0,100,101)

altitude = np.zeros(101)

# To check if two vectors are close that how its checked under the hood of RAG:

model = SentenceTransformer("all-MiniLM-L6-v2")


x=model.encode("Car is Honda",normalize_embeddings=True)

y=model.encode("Car is Hyundai",normalize_embeddings=True)
plt.plot(x, label="Honda")
plt.plot(y, label="Hyundai")
#plt.legend()
plt.show()

score = util.cos_sim(x,y).item()

#print(type(set(x)))
print(score)



















def main():
    pass




if __name__ == "__main__":
    main()
