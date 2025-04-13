FROM python:3
WORKDIR /usr/src/app.py

# Install all of the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the soruce
COPY . .
CMD ["python", "app.py"]
  