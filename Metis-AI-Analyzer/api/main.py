from fastapi import FastAPI, File, UploadFile
import numpy as np, os, tempfile
import scipy.sparse as sp
from ember.features import PEFeatureExtractor
from analyzer.ai_model import predict_from_vector

app = FastAPI(
    title="AI Malware Analyzer",
    description="Upload an EXE to detect if it's malware or benign using EMBER + LightGBM",
    version="1.0.0"
)

extractor = PEFeatureExtractor(2)  # feature extractor stays loaded in memory

@app.post("/analyze")
async def analyze(uploaded_file: UploadFile = File(...)):
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await uploaded_file.read())
        tmp_path = tmp.name

    with open(tmp_path, "rb") as f:
        bytez = f.read()
    os.remove(tmp_path)

    # Extract features and predict
    features = np.array(extractor.feature_vector(bytez), dtype=np.float32).reshape(1, -1)
    label, prob = predict_from_vector(sp.csr_matrix(features))

    return {
        "filename": uploaded_file.filename,
        "prediction": "Malware" if label == 1 else "Benign",
        "probability": float(prob)
    }

@app.get("/")
def root():
    return {"status": "API running", "message": "Upload files at /analyze"}
