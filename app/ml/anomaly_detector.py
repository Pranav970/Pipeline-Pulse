from sklearn.ensemble import IsolationForest
import numpy as np
model=IsolationForest(random_state=42,contamination=0.1)
X=np.array([[10],[20],[30],[1000]])
model.fit(X)

def predict_anomaly(log_text:str):
    return bool(model.predict([[len(log_text)]])[0]==-1)
