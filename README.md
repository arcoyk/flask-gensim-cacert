# flask-gensim-cacert
Reproduction of Docker-slim error on flask, gensim on debian

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
pip install docker-slim
docker-slim build flask-image
docker run -p 80:80 flask-image.slim 
```

# Notes
docker image before docker-slim works

