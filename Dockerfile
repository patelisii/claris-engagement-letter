FROM python:3.11
 
WORKDIR /app

COPY . /app
 
COPY requirements.txt .
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
EXPOSE 8000
 
# Run the backend server
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]