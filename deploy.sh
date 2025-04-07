#!/bin/bash

# Google Cloud project details
REGION="us-east1"
ARTIFACT_REPOSITORY="pipol-artifact-registry"
IMAGE_NAME="pipol-challenge-image"
JOB_NAME="pipol-challenge-job"

# Build the Docker image
docker build -t $ARTIFACT_REPOSITORY/$IMAGE_NAME .

# Push the Docker image to Google Container Registry
docker push $ARTIFACT_REPOSITORY/$IMAGE_NAME

# Deploy the image to Google Cloud Run
gcloud run jobs deploy $JOB_NAME \
  --image $ARTIFACT_REPOSITORY/$IMAGE_NAME \
  --region $REGION \

echo "Deployment to Google Cloud Run completed."