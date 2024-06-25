FROM python:3.9-slim

# Make new dir "/app" to Docker Image
WORKDIR /app

# Copy all Dirfiles to Docker Image dir '/app'
COPY . /app

# install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "./venv/fast_api.py"]