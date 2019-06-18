FROM node:12.2.0-stretch-slim

RUN mkdir -p /maisie_node_modules

COPY . /app 
WORKDIR /app 
RUN yarn install

RUN /bin/bash -c mount --bind /maisie_node_modules /app/node_modules

EXPOSE 3000
CMD [ "yarn" "start" ]