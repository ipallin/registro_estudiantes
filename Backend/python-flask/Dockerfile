# Set base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies directory to container
ADD ./requirements ./requirements

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements/prod.txt

# Copy the content of the local API directory to the working directory
COPY . .

# Establish the runtime user (with no password and no sudo)
RUN useradd -m user
USER user

# Expose a default API port
EXPOSE 5000

LABEL BACKEND="Python + Flask"
LABEL DB-CONNECTOR="PostgreSQL"
LABEL CreatedFrom="DataNext Project"

# Set a healthcheck
HEALTHCHECK \
    --interval=30s \
    --timeout=30s \
    --retries=5 \
    --start-period=10s \
    CMD python healthcheck.py

# command to run on container start
CMD [ "gunicorn", "-c", "gunicorn.conf.py", "api:app" ]
