FROM python:3.12-slim

# Install dependencies for selenium and Chrome
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src

# Copy GCP Credentials
COPY pipolchallenge.json pipolchallenge.json

# Copy the .env file
COPY .env .env

# Run the application
CMD ["python", "-m" , "src.main"]