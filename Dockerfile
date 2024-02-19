FROM python:3.10

RUN apt-get update -y && apt-get install -y build-essential

WORKDIR /app

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

RUN pip install -r requirements.txt

# the server
COPY --chown=user app.py app.py
COPY --chown=user chromedriver chromedriver

CMD ["gunicorn","-b","0.0.0.0:8000", "app:app","--timeout","950"]
