import os
import joblib

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

MODEL_FILE = "modele_ia.joblib"

if os.path.exists(MODEL_FILE):
    
    print("==> MODEL ALREADY TRAINED")
    model = joblib.load(MODEL_FILE)
    
else:
    
    print("==> DOWNLOADING MNIST DATASET")
    X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False, parser="liac-arff")
    print("==> DOWNLOAD COMPLETED")
    
    X = X / 255
    y = y.astype(int)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2,stratify=y)
    
    model = MLPClassifier(hidden_layer_sizes=(128, 64),max_iter=60,random_state=2)
    
    print("==> TRAINING THE MODEL")
    model.fit(X_train,y_train)
    joblib.dump(model,MODEL_FILE)
    print("==> MODEL TRAINED ")
    
    print(f"  - Accuracy: {model.score(X_test, y_test) * 100:.2f}%")