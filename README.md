# End-to-End-Machine-Learning-Project-with-ML-Flow
# Workflows

1. Update congig.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

---

# How to run?

## STEPS

Clone the repository

```bash
https://github.com/PrajnaShe/End-to-End-Machine-Learning-Project-with-ML-Flow
```

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

Activate the environment

```bash
conda activate mlproj
```

### STEP 02 - Install the requirements

```bash
pip install -r requirements.txt
```

Finally run the application

```bash
python app.py
```

Open your localhost and port in the browser.

---

# MLflow

[Documentation:](https://mlflow.org/docs/latest/index.html)

Run the MLflow UI

```bash
mlflow ui
```

---

# DagsHub

https://dagshub.com/

Run directly:

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/PrajnaShe/End-to-End-Machine-Learning-Project-with-ML-Flow.mlflow \
MLFLOW_TRACKING_USERNAME=PrajnaShe \
MLFLOW_TRACKING_PASSWORD=3618e24fb2b028c441d90ae5b079ff8a2ce94970 \
python script.py
```

Or export the variables permanently for the current terminal session:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/PrajnaShe/End-to-End-Machine-Learning-Project-with-ML-Flow.mlflow

export MLFLOW_TRACKING_USERNAME=PrajnaShe

export MLFLOW_TRACKING_PASSWORD=3618e24fb2b028c441d90ae5b079ff8a2ce94970
```