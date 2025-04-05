# Pipol Challenge
Technical Challenge Resolution Repository for Data Engineer position.
Details: https://mia-platform.notion.site/Python-Code-Challenge-Scraping-and-Ingest-Advanced-1add2fa22f91806b8eb9d3d52981161e

## Requirements

* Python 3.12
* Google Chrome

## Instructions

### How to 

* **Run locally**
    
    1. Clone Github repository

    ```bash
    git clone git@github.com:nvoviedo-code/pipol_challenge.git
    ```

    2. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

    3. Configure credentials for BigQuery connection

    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_credentials.json"
    ```

    4. Configure BigQuery DATASET_ID

    ```bash
    export DATASET_ID="bq-dataset-id"
    ```


* **Run using Docker**
    
    1. Execute the steps 3 and 4 for local running (enviroment vars setup)
    
    2. Run deploy bash script:

    ```bash
    ./deploy.sh
    ```

* **Test**

    After follow the instruction for setting up your environment to run locally.

    1. Install pytest
    
    ```bash
    pip install pytest
    ```

    2. Run
        
    ```bash
    pytest
    ```

#
***ChatGPT*** has been used as a tool to help solve parts of the challenge. The chats are available at [ChatGPT.md](ChatGPT.md).
#