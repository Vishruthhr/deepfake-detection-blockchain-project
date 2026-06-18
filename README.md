# Deepfake Detection using RetinaFace, Xception-LSTM and Ethereum Blockchain

## Project Overview

This project presents a Deepfake Video Detection System integrated with Ethereum Blockchain for secure and tamper-proof verification of prediction results.

The system detects whether a video is REAL or FAKE using Deep Learning techniques and stores the verification results on the Ethereum Sepolia Blockchain.

The main objective is to combine Artificial Intelligence and Blockchain Technology to improve trust, transparency, and security in deepfake detection systems.

---

## Features

* Deepfake Video Detection
* Face Detection using RetinaFace
* Feature Extraction using Xception Network
* Temporal Analysis using LSTM
* SHA256 Video Hash Generation
* Ethereum Blockchain Integration
* Tamper-Proof Verification Records
* Secure Storage of Prediction Results
* Automatic Prediction Logging

---

## System Architecture

Input Video

↓

RetinaFace Face Detection

↓

Face Extraction

↓

Xception CNN

↓

Feature Extraction

↓

LSTM Network

↓

REAL / FAKE Classification

↓

SHA256 Hash Generation

↓

Ethereum Smart Contract

↓

Blockchain Storage

---

## Technology Stack

### Programming Language

* Python 3.10

### Deep Learning

* TensorFlow
* Keras

### Computer Vision

* OpenCV
* RetinaFace

### Deep Learning Architecture

* Xception CNN
* LSTM

### Blockchain

* Ethereum Sepolia Testnet
* Solidity Smart Contracts
* Web3.py

### Development Tools

* Visual Studio Code
* MetaMask
* Alchemy RPC
* GitHub

---

## Why RetinaFace?

RetinaFace is a state-of-the-art deep learning based facial detector.

Advantages:

* High face detection accuracy
* Facial landmark detection
* Robust under varying lighting conditions
* Effective for deepfake preprocessing

The model extracts the most prominent face from each video frame before classification.

---

## Why Xception?

Xception is a powerful convolutional neural network architecture widely used in deepfake detection research.

Advantages:

* Efficient feature extraction
* Strong generalization capability
* Excellent performance on manipulated facial images

---

## Why LSTM?

Deepfake videos contain temporal inconsistencies across frames.

LSTM helps:

* Capture temporal dependencies
* Analyze frame sequences
* Improve video-level prediction accuracy

---

## Dataset

The system was trained on face sequences extracted from deepfake and real videos.

Preprocessing:

* Face extraction using RetinaFace
* Frame resizing to 224×224
* Normalization
* Sequence length: 20 frames

---

## Model Performance

### Final Evaluation Results

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 90.02% |
| Precision | 88.00% |
| Recall    | 92.68% |
| F1 Score  | 90.28% |
| ROC-AUC   | 96.45% |

### Classification Report

| Class | Precision | Recall | F1 Score |
| ----- | --------- | ------ | -------- |
| Real  | 0.92      | 0.87   | 0.90     |
| Fake  | 0.88      | 0.93   | 0.90     |

---

## Blockchain Integration

### Smart Contract

A Solidity smart contract was developed to store verification records.

Stored Information:

* Video Hash
* Prediction Result
* Timestamp
* Uploader Wallet Address

### Smart Contract Functions

#### storeRecord()

Stores a prediction result on Ethereum.

#### getRecord()

Retrieves a stored record.

#### getTotalRecords()

Returns total records stored.

---

## Ethereum Deployment

### Network

Ethereum Sepolia Testnet

### Wallet

MetaMask

### Communication

Alchemy RPC

### Python Library

Web3.py

---

## Example Blockchain Record

Video Hash:

6e83d0e0c51a0f7cdf2db48f796617db43148b3390011555dfa758f2b7ab811b

Prediction:

FAKE

Uploader:

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

### Activate Environment

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

### Predict a Video

Edit:

```python
VIDEO_PATH = r"path_to_video.mp4"
```

Then run:

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

Read all stored blockchain records:

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
│
├── face_dataset_generator.py
├── face_extractor.py
├── model.py
├── train_face_model.py
├── evaluate_model.py
├── predict_video_direct.py
│
├── requirements.txt
├── README.md
```

---

## Future Scope

* Web Application Integration
* Real-Time Video Detection
* IPFS Storage Integration
* Multi-Blockchain Support
* Explainable AI for Deepfake Detection
* Mobile Application Deployment

---

## Conclusion

This project successfully combines Deep Learning and Blockchain Technology to create a secure Deepfake Detection Framework. The system detects manipulated videos with 90.02% accuracy and stores prediction records on the Ethereum Blockchain, ensuring transparency, traceability, and tamper-proof verification.

## Author

Vishruth H R

B.Tech Information Science and Engineering

NMAM Institute of Technology (NMAMIT), Nitte
