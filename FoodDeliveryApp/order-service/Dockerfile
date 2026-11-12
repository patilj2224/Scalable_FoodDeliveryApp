FROM python:3.10-slim

WORKDIR /app

# Copy code
COPY order-service.py /app/

# Install dependencies
RUN pip install flask requests

# Run the service
CMD ["python", "order-service.py"]
