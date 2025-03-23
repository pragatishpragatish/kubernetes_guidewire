import tkinter as tk
from tkinter import messagebox, ttk
import requests

# Flask API URL
API_URL = "http://127.0.0.1:5000/predict"

# List of all 55 features
FEATURES = [
    "Src Port", "Dst Port", "Protocol", "Flow Duration", "Total Fwd Packet", "Total Bwd packets",
    "Total Length of Fwd Packet", "Total Length of Bwd Packet", "Fwd Packet Length Max",
    "Fwd Packet Length Mean", "Fwd Packet Length Std", "Bwd Packet Length Max", "Bwd Packet Length Mean",
    "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s", "Flow IAT Mean", "Flow IAT Std",
    "Flow IAT Max", "Flow IAT Min", "Fwd IAT Total", "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max",
    "Fwd IAT Min", "Bwd IAT Total", "Bwd IAT Mean", "Bwd IAT Std", "Bwd IAT Max", "Bwd IAT Min",
    "Fwd PSH Flags", "Bwd PSH Flags", "Fwd Header Length", "Bwd Header Length", "Fwd Packets/s",
    "Bwd Packets/s", "Packet Length Max", "Packet Length Mean", "Packet Length Std", "Packet Length Variance",
    "FIN Flag Count", "SYN Flag Count", "PSH Flag Count", "ACK Flag Count", "Down/Up Ratio",
    "Average Packet Size", "Fwd Segment Size Avg", "Bwd Segment Size Avg", "Subflow Fwd Bytes",
    "Subflow Bwd Bytes", "FWD Init Win Bytes", "Bwd Init Win Bytes", "Fwd Act Data Pkts",
    "Fwd Seg Size Min", "Total TCP Flow Time"
]

# Function to get prediction
def get_prediction():
    try:
        # Read values from entry fields
        features = [float(entries[i].get()) if entries[i].get() else 0 for i in range(len(FEATURES))]

        # Prepare JSON payload
        data = {"features": features}

        # Send request to Flask API
        response = requests.post(API_URL, json=data)

        # Handle response
        if response.status_code == 200:
            result = response.json()
            messagebox.showinfo("Prediction", f"Predicted Output: {result['prediction']}")
        else:
            messagebox.showerror("Error", f"Server Error: {response.text}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI
root = tk.Tk()
root.title("Kubernetes Failure Prediction")
root.geometry("600x700")

# Create a scrollable frame
frame_canvas = tk.Frame(root)
frame_canvas.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame_canvas)
scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Input fields
entries = []
for feature in FEATURES:
    frame = ttk.Frame(scrollable_frame)
    frame.pack(pady=2, padx=10, fill=tk.X)

    label = ttk.Label(frame, text=feature, width=30)
    label.pack(side=tk.LEFT)

    entry = ttk.Entry(frame, width=20)
    entry.pack(side=tk.LEFT)
    
    entries.append(entry)

# Predict Button
predict_btn = tk.Button(scrollable_frame, text="Predict", command=get_prediction, font=("Arial", 12), bg="green", fg="white")
predict_btn.pack(pady=10)

# Run GUI
root.mainloop()
