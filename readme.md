# Flask Application Deployment to Google Cloud Run

This guide provides instructions for deploying a Flask application to Google Cloud Run using Docker.

## Prerequisites

- Docker installed on your machine
- Google Cloud SDK installed and configured
- A Google Cloud project set up

## Steps

### 1. Build the Docker Image

Build the Docker image for your Flask application:

docker build -t gcr.io/persuasive-byte-443015-n7/image-flask-micro .

Replace your-project-id with your Google Cloud project ID and your-image-name with the name you want to give your Docker image.

2. Push the Docker Image to Google Container Registry
Push the Docker image to Google Container Registry:

docker push gcr.io/persuasive-byte-443015-n7/image-flask-micro

3. Deploy to Google Cloud Run
Deploy the Docker image to Google Cloud Run:

gcloud run deploy --image gcr.io/persuasive-byte-443015-n7/image-flask-micro --platform managed

Follow the prompts to complete the deployment. You will need to specify the service name and region.

4. Access Your Application
Once the deployment is complete, you will receive a URL where your application is hosted. You can access your Flask application using this URL.

Files
app.py: The main Flask application file.
math_helper.py: The helper class for arithmetic operations.
requirements.txt: The file listing the dependencies for the Flask application.
Dockerfile: The Dockerfile for containerizing the Flask application.