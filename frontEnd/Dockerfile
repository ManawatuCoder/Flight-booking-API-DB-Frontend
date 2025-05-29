FROM node:latest
COPY . /app
WORKDIR /app
run npm install
CMD ["npm", "run", "dev",  "--", "--host", "0.0.0.0", "--port", "8080"]