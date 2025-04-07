# Pipol Challenge
Technical Challenge Resolution Repository for Data Engineer position.

Project Details: [Python Code Challenge](https://mia-platform.notion.site/Python-Code-Challenge-Scraping-and-Ingest-Advanced-1add2fa22f91806b8eb9d3d52981161e)

## Requirements

- Python 3.12
- Google Chrome
- Google Cloud Platform (GCP) project

## Instructions

To get started, clone the GitHub repository locally:

```bash
git clone git@github.com:nvoviedo-code/pipol_challenge.git
```

This project requires access to a Google Cloud Project with a properly configured BigQuery instance. Authentication is managed using a service account key.

### Configuration Steps

1. **Set up Google Cloud credentials**  
    Follow the [Google Cloud documentation](https://console.cloud.google.com/apis/credentials/serviceaccountkey) to create and download a service account key. Save the credentials file in the root of this project as `pipolchallenge.json`.

2. **Set the BigQuery Dataset ID**  
    Define the dataset ID as an environment variable. Replace `bq-dataset-id` with your BigQuery dataset ID:

    ```bash
    export DATASET_ID="bq-dataset-id"
    ```

Ensure these steps are completed before running the project.

### Run, Test, and Deploy

#### Run Locally

1. Create a virtual environment:

    ```bash
    python -m venv <venv>
    source <venv>/bin/activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Python code:

    ```bash
    python -m src:main
    ```

#### Test Locally

1. Install `pytest` in the activated virtual environment:

    ```bash
    pip install pytest
    ```

2. Execute tests:

    ```bash
    pytest
    ```

#### Run Using Docker

1. Build the Docker image:

    ```bash
    docker build -t pipol_challenge:latest .
    ```

2. Run the container:

    ```bash
    docker run pipol_challenge:latest
    ```

#### Deploy to Google Cloud Run Job

1. Open the `deploy.sh` script and update the following variables with your GCP project details:

    ```bash
    REGION="us-east1"
    ARTIFACT_REPOSITORY="gcp-artifact-repository"
    IMAGE_NAME="pipol-challenge-image"
    JOB_NAME="pipol-challenge-job"
    ```

2. Execute the deployment script:

    ```bash
    sh ./deploy.sh
    ```

---

**Note:** ChatGPT was used as a tool to assist in solving parts of this challenge. The related conversations are documented in [ChatGPT.md](ChatGPT.md).