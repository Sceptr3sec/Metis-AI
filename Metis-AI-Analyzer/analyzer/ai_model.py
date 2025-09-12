import lightgbm as lgb
import scipy.sparse as sp

model = lgb.Booster(model_file="models/ember_model.txt")

def predict_from_vector(vector):
    """vector = sparse feature vector for one file"""
    proba = model.predict(vector.toarray())
    return int(proba[0] > 0.5), proba[0]  # (label, probability)
