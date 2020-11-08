# Repo
Reproduction of Docker-slim error on [flask](https://github.com/pallets/flask), [gensim](https://github.com/RaRe-Technologies/gensim) on debian

# Dockerfile
```
FROM debian
RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install --no-cache-dir gensim flask
RUN apt clean
EXPOSE 80
ADD ./app ./app
ENV FLASK_APP test.py
CMD cd app && flask run --host='0.0.0.0' --port=80
```

# Error
```
FileNotFoundError: [Errno 2] No such file or directory: '/usr/local/lib/python3.7/dist-packages/certifi/cacert.pem'
```

this error occurs on...
https://github.com/python/cpython/blob/41761933c1c30bb6003b65eef1ba23a83db4eae4/Lib/importlib/resources.py#L91

# How to reproduce the bug
```
git clone git@github.com:arcoyk/flask-gensim-cacert.git
docker build -t flask-image .
docker-slim build flask-image
docker run -p 80:80 flask-image.slim 
```

# Notes
This repo includes > 300MB file (Word2Vec model) which may take time to clone.
docker image before docker-slim works.

# Versions
Docker version 19.03.12, build 48a66213fe
docker-slim version darwin|Transformer|1.32.0|latest|latest
