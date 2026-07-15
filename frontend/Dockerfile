# get the user and group. if not defined, fallback to root
ARG UID=root
ARG GID=root

########################################
# build webui                          #
########################################

FROM node:22-alpine AS builder

WORKDIR /app

COPY ./th-kiforum/ /app

# install packages
RUN npx browserslist@latest --update-db
RUN npm install -g npm
RUN npm install

# build webui
RUN npm run build

########################################
# actuall webserver                    #
########################################

FROM nginx AS thkiforum_frontend

COPY --from=builder /app/dist /var/www/html
