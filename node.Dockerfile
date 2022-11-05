FROM node:13.12.0-alpine
WORKDIR /

COPY . .

RUN npm install @babel/core
RUN npm install 
