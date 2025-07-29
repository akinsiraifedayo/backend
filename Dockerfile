# Use python 3.10 docker image
FROM python:3.10-slim

# Set working directory
WORKDIR /backend

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables
ENV NAME=bank-backend
LABEL maintainer="olympicson <akinsiraolympicson@gmail.com>"

# Run Uvicorn (certs will be mounted at runtime)
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

# EXPOSE 443
# CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile=/etc/ssl/certs/private/privkey.pem", "--ssl-certfile=/etc/ssl/certs/private/cert.pem"]
