# Metis-AI
AI-powered malware analyzer built with EMBER, LightGBM, and FastAPI. Upload an executable file and get an instant prediction (malware or benign) with probability score. Extensible with YARA scanning, entropy checks, and static feature reporting.

# 🦠 AI Malware Analyzer  

An **AI-powered malware detection tool** built with:  
- **EMBER 2018 dataset** (1.1M PE files, engineered features)  
- **LightGBM classifier** (AUC ~0.9830 on test set)  
- **FastAPI backend** for file uploads & predictions  
- **Extensible design** for YARA scanning, entropy checks, and static analysis  

⚡ Upload an EXE file → get a JSON verdict:  
- Malware or Benign  
- Probability score  
- (Future: Hashes, entropy, YARA hits, report export)  

---

## 🚀 Features
- ✅ EMBER-trained LightGBM model (`ember_model.txt`)  
- ✅ REST API via FastAPI  
- ✅ Upload `.exe` → get instant malware verdict  
- ✅ Dockerized for easy deployment  
- 🔜 YARA rule integration (signature-based detection)  
- 🔜 Entropy & static feature reporting  
- 🔜 Streamlit UI frontend  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [LightGBM](https://github.com/microsoft/LightGBM)  
- [EMBER Dataset](https://github.com/elastic/ember)  
- [LIEF](https://lief.quarkslab.com/) (PE parsing)  
- [YARA](https://virustotal.github.io/yara/) (future integration)  

---

## 📂 Project Structure
ai-malware-analyzer/
├── analyzer/ # Core ML + analysis logic
│ ├── ai_model.py
│ ├── analyzer.py
│ ├── static.py
│ └── yara_scan.py
├── api/ # FastAPI service
│ └── main.py
├── models/ # Trained models (not committed to GitHub)
│ └── ember_model.txt
├── rules/ # YARA rules (future)
├── tests/ # Unit tests (WIP)
├── ui/ # Streamlit frontend (future)
├── requirements.txt
├── Dockerfile
└── README.md

yaml
Copy code

---

## ⚙️ Installation

Clone repo:
```bash
git clone https://github.com/YOUR_USERNAME/ai-malware-analyzer.git
cd ai-malware-analyzer
Create virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
⚠️ You need a trained ember_model.txt inside models/.
Train it separately with EMBER (instructions in repo wiki) or download from releases.

▶️ Usage
Run FastAPI locally:

bash
Copy code
uvicorn api.main:app --reload
Swagger UI: http://127.0.0.1:8000/docs

Upload EXE file → get prediction:

Example request (curl):

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'uploaded_file=@notepad.exe;type=application/x-msdownload'
Example response:

json
Copy code
{
  "filename": "notepad.exe",
  "prediction": "Benign",
  "probability": 0.0342
}
📊 Model Performance
Dataset: EMBER 2018

Classifier: LightGBM

Test Accuracy: 98.3%

AUC: 0.9830

🐳 Docker Support
Build image:

bash
Copy code
docker build -t ai-malware-analyzer .
Run container:

bash
Copy code
docker run -p 8000:8000 ai-malware-analyzer
📌 Roadmap
 Add YARA scanning support

 Add entropy + static analysis report

 Streamlit web UI

 Database logging of scans

 DockerHub image release

📜 License
MIT License © 2025 Sceptr3sec

🙌 Acknowledgements
EMBER Dataset by Elastic Security

LightGBM by Microsoft

LIEF for PE parsing

FastAPI for the API framework
