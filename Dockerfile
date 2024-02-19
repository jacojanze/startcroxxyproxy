FROM python:3.10

RUN apt-get update -y && apt-get install -y \
    build-essential \
    wget \
    unzip \
    libgconf-2-4 \
    xvfb

# Install Chrome browser version 114.0.5735.90
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.90-1_amd64.deb \
    && dpkg -i /tmp/chrome.deb || apt-get -f install -y \
    && rm /tmp/chrome.deb

# Download ChromeDriver version 114.0.5735.90
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip

RUN chmod +x /usr/local/bin/chromedriver

WORKDIR /app

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

RUN pip install -r requirements.txt

# Make sure the file has appropriate permissions
COPY --chown=user app.py app.py

CMD ["gunicorn","-b","0.0.0.0:8000", "app:app","--timeout","950"]
