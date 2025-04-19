FROM node:20-slim

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV VITE_BASE_API_URL=http://web:8000/api

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]