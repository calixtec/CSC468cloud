#References:
#https://medium.com/@alinaseri/dockerize-react-applications-with-nginx-17f752deb54
#https://kinsta.com/knowledgebase/install-react/#how-to-install-react-on-linux

# Use the official Node.js runtime as the base image
FROM node:20-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install --force

RUN npm install -g create-react-app

# Copy the entire application code to the container
COPY . .

# Build the React app for production
RUN npm run build

# Use Nginx as the production server
FROM nginx:alpine

# Copy the built React app to Nginx's web server directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for the Nginx server
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]
