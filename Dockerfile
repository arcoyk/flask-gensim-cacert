FROM debian
RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install --no-cache-dir gensim flask
RUN apt clean
EXPOSE 80
ADD ./app ./app
ENV FLASK_APP test.py
CMD cd app && flask run --host='0.0.0.0' --port=80
