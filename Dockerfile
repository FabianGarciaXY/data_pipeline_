FROM python:3.9

# Main directory
WORKDIR /app

# Copying and installing dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Executing server
CMD ["python", "./src/app.py"]