FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# 🔐 Accept secret at build/runtime
ARG FLASK_SECRET_KEY
ENV FLASK_SECRET_KEY=${FLASK_SECRET_KEY}

# Expose Flask port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
