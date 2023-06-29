FROM node:18.8.0

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and yarn.lock files to the container
COPY package.json yarn.lock ./

# Install the project dependencies using Yarn
RUN yarn install

# Copy the rest of the application files to the container
COPY . .

# Specify the command to run when the container starts
CMD ["yarn", "dev"]
