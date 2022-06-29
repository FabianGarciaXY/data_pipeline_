FROM python:3.9

# Main directory
WORKDIR /app

# Copying and installing dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Setting up python path environment
ENV PYTHONPATH="/app/src:$PYTHONPATH"

# Executing server
RUN ["chmod", "+x", "./src/data/scripts/init.sh"]
ENTRYPOINT [ "bash", "./src/data/scripts/init.sh" ]