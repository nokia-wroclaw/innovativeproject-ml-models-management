FROM node:11.12.0-alpine

COPY . /app 
WORKDIR /app 
RUN yarn install

EXPOSE 3000
CMD [ "yarn" "start" ]