# Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip


# Copy and install requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire src directory and data directory
COPY src/ /app/src/
COPY data/ /app/data/

# Set working directory to where ETL scripts are
WORKDIR /app/src/etl

# Run ETL
CMD ["python", "main_etl.py"]
