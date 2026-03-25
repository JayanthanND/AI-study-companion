FROM node:20-alpine

WORKDIR /app
ARG NEXT_PUBLIC_API_URL=http://localhost:8000
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}

COPY package*.json ./
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi

COPY . ./

EXPOSE 3000
RUN npm run build
CMD ["npm", "run", "start", "--", "-H", "0.0.0.0", "-p", "3000"]
