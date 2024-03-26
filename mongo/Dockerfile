FROM mongo:latest

# Set environment variables for MongoDB initialization
ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=secret

# Expose the MongoDB default port (27017) if needed
EXPOSE 27017

# Set the working directory (optional)
WORKDIR /usr/src/app

# Copy any initialization scripts or configuration files if needed
COPY init.js /docker-entrypoint-initdb.d/

# Command to start mongod with authentication enabled
CMD ["mongod", "--auth"]
