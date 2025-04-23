# Text Summarizer Project

## Overview
This project implements an advanced text summarization system using the PEGASUS model. It features a complete ML pipeline from data ingestion to API deployment, capable of generating concise summaries from longer texts.

## Features
- End-to-end ML pipeline implementation
- FastAPI-based REST API
- PEGASUS model fine-tuning
- ROUGE metric evaluation
- Modular and maintainable codebase


## Project Structure
```
textSummarizer/
├── .github/workflows/
├── src/textSummarizer/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   ├── utils/
│   ├── logging/
│   ├── config/
│   ├── pipeline/
│   │   ├── stage1_data_ingestion_pipeline.py
│   │   ├── stage2_data_transformation_pipeline.py
│   │   ├── stage3_model_trainer_pipeline.py
│   │   ├── stage4_model_evaluation_pipeline.py
│   │   └── stage5_prediction_pipeline.py
│   ├── entity/
│   └── constants/
├── config/
│   └── config.yaml
├── params.yaml
├── app.py
├── main.py
├── Dockerfile
└── requirements.txt
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone https://github.com/MelvinAnnasse/TextSummarizer.git
cd textSummarizer
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Training Pipeline
To run the complete training pipeline:
```bash
python app.py
```

This executes:
1. Data Ingestion
2. Data Transformation
3. Model Training
4. Model Evaluation

### API Service
Start the FastAPI server:
```bash
python app.py
```

The API will be available at: http://localhost:5000

### API Endpoints

1. Root endpoint:
```
GET /
Response: Redirects to API documentation
```

2. Training endpoint:
```
GET /train
Response: Initiates model training
```

3. Prediction endpoint:
```
POST /predict
Body: {
    "text": "Your text to summarize"
}
Response: {
    "summary": "Generated summary"
}
```

## Model Details

### Architecture
- Base Model: PEGASUS (google/pegasus-cnn_dailymail)
- Fine-tuned on: SAMSum dialogue dataset
- Training Parameters:
  - Length Penalty: 0.8
  - Number of Beams: 8
  - Max Length: 128

### Performance Metrics
Evaluated using ROUGE scores:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- ROUGE-Lsum

## Configuration

### config.yaml
Contains configuration for:
- Data paths
- Model parameters
- Training settings
- Evaluation metrics

### params.yaml
Contains hyperparameters for:
- Model training
- Text generation
- Evaluation metrics

## Development Workflow

#### 1. Data Ingestion
- Downloads dataset from configured source
- Extracts and validates data
- Creates organized directory structure
- Maintains operation logs

#### 2. Data Transformation
- Text preprocessing
- Tokenization
- Dataset splitting
- Feature generation

#### 3. Model Training
- Hyperparameter configuration
- Training execution
- Model checkpointing
- Performance monitoring

#### 4. Model Evaluation
- ROUGE metrics calculation
- Performance analysis
- Quality validation
- Results documentation

#### 5. Prediction 
- Model serving
- Request processing
- Response generation
- Performance logging

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
GPL-3.0 license

## Acknowledgments
- HuggingFace Transformers library
- PEGASUS model team
- SAMSum dataset creators
