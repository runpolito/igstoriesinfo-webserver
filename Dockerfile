FROM python:latest
LABEL org.opencontainers.image.authors="runpolito"

# Environment variables
ENV PORT=3001

# Create app directory
WORKDIR /usr/src/app

# Install dependencies
RUN pip3 install flask
RUN pip3 install markupsafe
RUN pip3 install instaloader

# Copy files
COPY . .

# Expose port
EXPOSE $PORT
# Run the app
CMD [ "python3", "server.py"]