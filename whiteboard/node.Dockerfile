# pull official base image
FROM node:14-alpine AS build

LABEL maintainer="Mohammad Rabetian <mohammadrabetian@gmail.com>"

ENV NODE_ENV=production

# make directory & install dependencies
RUN mkdir /code
WORKDIR /code
COPY package.json package-lock.json /code/
RUN npm install


# copy project
COPY . /code/
RUN npm run build:app

FROM nginx:1.17-alpine

COPY --from=build /code/build /usr/share/nginx/html

HEALTHCHECK CMD wget -q -O /dev/null http://localhost || exit 1
