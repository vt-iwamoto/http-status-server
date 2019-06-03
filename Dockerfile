FROM python:3.7.3-alpine3.9

RUN pip install Flask

WORKDIR /opt/http-status-server
COPY app.py ./

EXPOSE 5000
ENV FLASK_APP app.py
CMD ["flask", "run", "--host=0.0.0.0"]
