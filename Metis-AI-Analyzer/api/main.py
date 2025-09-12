from fastapi import FastAPI, File, UploadFile, HTTPException
import scipy.sparse as sp
from ember.features import PEFeatureExtractor
from analyzer.ai_model import predict_from_vector
import traceback
import numpy as np

if not hasattr(np, "int"):
    np.int = int


app = FastAPI(
    title="AI Malware Analyzer",
    description="Upload an EXE to detect if it's malware or benign using EMBER + LightGBM",
    version="1.0.0"
)

# Keep extractor in memory
extractor = PEFeatureExtractor(2)

def safe_feature_vector(bytez):
    try:
        # This directly gives you a NumPy array (no .get() needed)
        return extractor.feature_vector(bytez)
    except Exception as e:
        raise RuntimeError(f"Feature extraction failed: {str(e)}")


@app.post("/analyze")
async def analyze(uploaded_file: UploadFile = File(...)):
    try:
        # Read raw bytes directly
        bytez = await uploaded_file.read()

        # Extract EMBER features
        features = np.array(safe_feature_vector(bytez), dtype=np.float32).reshape(1, -1)

        # Predict using your model wrapper
        label, prob = predict_from_vector(sp.csr_matrix(features))

        return {
            "filename": uploaded_file.filename,
            "prediction": "Malware" if label == 1 else "Benign",
            "probability": float(prob)
        }

    except Exception as e:
        print(traceback.format_exc())  # Debugging in server logs
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/")
def root():
    return {"status": "API running", "message": "Upload files at /analyze"}
