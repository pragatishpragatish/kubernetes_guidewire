# Kubernetes Failure Prediction Using Machine Learning

## 📌 Project Overview
This project aims to predict failures in Kubernetes clusters using machine learning models based on network traffic and system resource metrics. The goal is to detect potential issues such as pod crashes, resource bottlenecks, and network failures before they occur, enabling proactive mitigation.

## 📊 Dataset Information
The dataset contains network traffic features such as:
- **Flow Information**: Flow ID, Flow Duration, Flow Bytes/s, Flow Packets/s
- **Network Metrics**: Source/Destination IP & Port, Protocol, Timestamp
- **Traffic Features**: Packet Lengths, Forward/Backward Packets, IAT (Inter-Arrival Time)
- **Flags & Indicators**: TCP Flags, PSH Flags, ACK Flags
- **Resource Utilization**: CPU, Memory, Disk IO, Network IO

The dataset is preprocessed to handle missing values, normalize numerical features, and extract relevant insights for model training.

## 📁 Project Structure
```
k8s_failure_prediction/
│── data/                     # Store datasets
│   ├── train_data.csv
│   ├── test_data.csv
│── notebooks/                 # Jupyter Notebooks for EDA & model training
│   ├── data_exploration.ipynb
│   ├── model_training.ipynb
│── src/
│   ├── data_preprocessing.py   # Data loading & preprocessing
│   ├── model.py                # ML model training & evaluation
│   ├── prediction.py           # Prediction script
│── app.py                      # Flask API for predictions
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```

## 🛠️ Technologies Used
- **Programming Language**: Python 3.9
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Framework**: Flask (for API)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (K8s)
- **Cloud Deployment**: Minikube / AWS EKS

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/k8s_failure_prediction.git
cd k8s_failure_prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model
```bash
python src/model.py
```

### 4️⃣ Start the Flask API
```bash
python app.py
```

### 5️⃣ Test the API
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{
    "cpu_usage": 80,
    "memory_usage": 90,
    "disk_io": 400,
    "network_io": 700,
    "pod_status": 0,
    "service_errors": 1
}'
```

## 📈 Model Performance
- **Accuracy**: 87%
- **Improvements**:
  - Experiment with time-series models (LSTMs)
  - Use real-time Kubernetes logs for better prediction

## 📌 Future Improvements
✅ Integrate real-time monitoring using Prometheus & Grafana  
✅ Enhance model accuracy with deep learning (LSTMs, Transformers)  
✅ Automate Kubernetes failure mitigation  

---

## ✨ Contributors
- **Your Name** ([@pragatishpragatish](https://github.com/pragatishpragatish))

## 📜 License
This project is licensed under the MIT License.

---

🚀 **Stay ahead of Kubernetes failures with AI-powered prediction!**
