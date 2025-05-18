# Use an official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (for example, if you're using scapy or dpkt)
RUN apt-get update && apt-get install -y \
    netcat \
    hping3 \
    iputils-ping \
    tcpdump \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Notebook
RUN pip install jupyter

# Copy the notebook into the container
COPY ddos_detection.ipynb /app/

# Expose the Jupyter port
EXPOSE 8888

# Command to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
