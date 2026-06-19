# Deepfake Detection using RetinaFace, Xception-LSTM and Ethereum Blockchain

## Project Overview

This project presents a Deepfake Video Detection System integrated with Ethereum Blockchain for secure, transparent, and tamper-proof verification of prediction results.

The system uses RetinaFace for face detection, Xception CNN for spatial feature extraction, and LSTM for temporal sequence analysis. After classification, a SHA256 hash of the video along with the prediction result is stored on the Ethereum Sepolia Blockchain using a Solidity Smart Contract.

The objective of this project is to combine Deep Learning and Blockchain Technology to improve trust, security, and authenticity verification of digital media.

---

## Features

* Deepfake Video Detection
* Face Detection using RetinaFace
* Feature Extraction using Xception CNN
* Temporal Learning using LSTM
* SHA256 Video Hash Generation
* Ethereum Blockchain Integration
* Smart Contract Based Verification
* Tamper-Proof Record Storage
* Secure Prediction Logging
* Blockchain-Based Evidence Tracking

---

## System Architecture

Input Video

↓

RetinaFace Face Detection

↓

Face Extraction & Preprocessing

↓

Xception CNN Feature Extraction

↓

LSTM Temporal Analysis

↓

REAL / FAKE Classification

↓

SHA256 Video Hash Generation

↓

Ethereum Smart Contract

↓

Blockchain Storage

---

## Technology Stack

### Programming Language

* Python 3.10

### Deep Learning Frameworks

* TensorFlow
* Keras

### Computer Vision

* OpenCV
* RetinaFace

### Deep Learning Architecture

* Xception CNN
* LSTM Network

### Blockchain

* Ethereum Sepolia Testnet
* Solidity
* Web3.py

### Development Tools

* Visual Studio Code
* MetaMask
* Alchemy RPC
* GitHub

---

## Why RetinaFace?

RetinaFace is a state-of-the-art deep learning-based face detector capable of accurately detecting faces under challenging conditions.

Advantages:

* High face detection accuracy
* Facial landmark detection
* Robust under varying lighting conditions
* Effective face localization
* Improved preprocessing for deepfake detection

The model extracts the most prominent face from each frame before classification.

---

## Why Xception?

Xception is one of the most widely used architectures in deepfake detection research.

Advantages:

* Excellent feature extraction capability
* Strong performance on manipulated images
* Efficient transfer learning
* Reduced overfitting

The network learns deepfake-specific visual artifacts from facial regions.

---

## Why LSTM?

Deepfake videos often contain temporal inconsistencies that cannot be detected from a single frame.

LSTM helps:

* Capture temporal dependencies
* Learn frame-to-frame relationships
* Improve video-level classification accuracy
* Detect manipulation patterns across sequences

---

## Dataset

The model was trained using face sequences extracted from real and deepfake videos.

### Preprocessing Steps

* Face Detection using RetinaFace
* Face Cropping
* Frame Resizing to 224×224
* Pixel Normalization
* Sequence Generation
* Temporal Sampling

### Sequence Configuration

* Image Size: 224 × 224
* Sequence Length: 20 Frames

---

## Model Performance

### Final Evaluation Results

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 92.46% |
| Precision | 94.43% |
| Recall    | 90.24% |
| F1 Score  | 92.29% |
| ROC-AUC   | 97.48% |

### Classification Report

| Class | Precision | Recall | F1 Score |
| ----- | --------- | ------ | -------- |
| Real  | 0.91      | 0.95   | 0.93     |
| Fake  | 0.94      | 0.90   | 0.92     |

### Confusion Matrix

| Actual / Predicted | Real | Fake |
| ------------------ | ---- | ---- |
| Real               | 427  | 24   |
| Fake               | 44   | 407  |

---

## Blockchain Integration

### Smart Contract

A Solidity Smart Contract was developed to securely store prediction results on the Ethereum Blockchain.

### Stored Information

* Video Hash
* Prediction Result
* Timestamp
* Wallet Address

### Smart Contract Functions

#### storeRecord()

Stores a prediction result on Ethereum.

#### getRecord()

Retrieves a stored prediction record.

#### getTotalRecords()

Returns the total number of stored records.

---

## Ethereum Deployment

### Network

Ethereum Sepolia Testnet

### Wallet

MetaMask

### RPC Provider

Alchemy

### Python Library

Web3.py

---

## Example Blockchain Record

Video Hash:

6e83d0e0c51a0f7cdf2db48f796617db43148b3390011555dfa758f2b7ab811b

Prediction:

FAKE

Wallet Address:

0xc2aE2f50736d9C9986C68EA332A04502A21E7A9B

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/deepfake-detection-blockchain.git
cd deepfake-detection-blockchain
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Predict and Verify a Video

Edit:

```python
VIDEO_PATH = r"path_to_video.mp4"
```

Run:

```bash
python predict_video_direct.py
```

Output:

```text
Prediction: REAL/FAKE
Confidence: XX%
Video Hash: XXXXX
Transaction Hash: XXXXX
```

---

## Blockchain Verification

Retrieve all blockchain records:

```bash
python read_blockchain.py
```

---

## Project Structure

```text
deepfake-detection-blockchain
│
├── blockchain
│   ├── DeepfakeStorage.sol
│   ├── blockchain_interface.py
│   ├── deploy_contract.py
│   ├── contract_abi.json
│   └── contract_bytecode.txt
│
├── face_dataset_generator.py
├── face_extractor.py
├── model.py
├── train_face_model.py
├── fine_tune_model.py
├── evaluate_model.py
├── predict_video_direct.py
├── read_blockchain.py
│
├── requirements.txt
├── README.md
```

---

## Future Scope

* Real-Time Deepfake Detection
* Web Application Deployment
* Mobile Application Integration
* IPFS Storage Support
* Multi-Blockchain Compatibility
* Explainable AI Integration
* Cloud Deployment

---

## Conclusion

This project successfully combines Deep Learning and Blockchain Technology to create a secure Deepfake Detection Framework. The proposed system achieved **92.46% accuracy**, **94.43% precision**, **92.29% F1 Score**, and **97.48% ROC-AUC** while providing tamper-proof verification through Ethereum Blockchain integration.

---

## Author

**Vishruth H R**

B.Tech Information Science and Engineering

NMAM Institute of Technology (NMAMIT), Nitte
