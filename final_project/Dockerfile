FROM python:alpine3.9
COPY . /webapp
WORKDIR /webapp
RUN apk add openssl
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
EXPOSE 8080