# Stage 1: Building Vue.js
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Start the http-server
FROM node:lts-alpine
WORKDIR /scenic-navigation-app
COPY --from=build-stage /app/dist /scenic-navigation-app
RUN npm install -g http-server

EXPOSE 8080


CMD ["http-server", "/scenic-navigation-app", "-p", "8080"]
