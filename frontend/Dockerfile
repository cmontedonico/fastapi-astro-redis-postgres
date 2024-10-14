 # Use an official Node runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . .

# Build the Astro project
RUN npm run build

# Make port 3000 available to the world outside this container
EXPOSE 4321

# Run the app when the container launches
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]