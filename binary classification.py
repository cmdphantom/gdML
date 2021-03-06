#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_classification 
from sklearn.linear_model import SGDClassifier


# In[4]:


# Génération de données aléatoires: 100 exemples, 2 classes, 2 features x0 et x1
np.random.seed(1)
x, y = make_classification(n_samples=100,n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)


# In[5]:


# Visualisation des données
plt.figure(num=None, figsize=(8, 6)) 
plt.scatter(x[:,0], x[:, 1], marker = 'o', c=y, edgecolors='k') 
plt.xlabel('X0') 
plt.ylabel('X1') 
x.shape


# In[6]:


# Génération d'un modele en utilisant la fonction cout 'log' pour Logistic Regression 
model = SGDClassifier(max_iter=1000, eta0=0.001, loss='log')


# In[7]:


model.fit(X, y) 
print('score:', model.score(x, y))


# In[8]:


# Visualisation des données
h = .02
colors = "bry" 
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1 
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


# In[9]:


Z = model.predict(np.c_[xx.ravel(), yy.ravel()]) 
Z = Z.reshape(xx.shape) 
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired) 
plt.axis('tight')


# In[10]:


for i, color in zip(model.classes_, colors):
    idx = np.where(y == i) 
    plt.scatter(X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor='black', s=20)


# In[ ]:




