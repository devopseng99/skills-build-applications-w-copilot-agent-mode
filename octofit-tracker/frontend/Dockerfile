FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Change from port 3000 to Vite's default 5173
EXPOSE 5173

# Update command to specify host for container networking
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]