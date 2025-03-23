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
│   ├── balanced shuffled traffic.csv
│── notebooks/                 # Jupyter Notebooks for EDA & model training
│   ├── main.ipynb
│   ├── gui.py
│── docs/
│   │── requirements.txt            # Dependencies
│   │── README.md                   # Documentation
│── models/
│   │── k8s_failure_model.pkl       #saved model
│── presentation/
│   │──Demo Video
│   │──Presentation PPT
│
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
git clone https://github.com/pragatishpragatish/kubernetes_guidewire/k8s_failure_prediction.git
cd k8s_failure_prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model
```bash
python notebooks/main.ipynb
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
- **Pragatish A M** ([@pragatishpragatish](https://github.com/pragatishpragatish))
- **Koushik Babu A S** ([@koushikkb12](https://github.com/koushikkb12))

## 📜 License
This project is licensed under the MIT License.

---

🚀 **Stay ahead of Kubernetes failures with AI-powered prediction!**
