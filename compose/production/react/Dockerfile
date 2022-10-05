# build env
FROM node:14-buster as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./front/package.json /app/
COPY ./front/yarn.lock /app/
RUN yarn
COPY ./front /app
RUN yarn build


# production env
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/react/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]