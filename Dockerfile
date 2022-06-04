FROM python:3.8
RUN apt-get update && \
  apt-get install -y fonts-ipafont && \
  rm -rf /var/lib/apt/lists/*
COPY predictor/ /predictor/
COPY src/ /src/
RUN python3 -m pip install matplotlib
RUN python3 -m pip install -e predictor
WORKDIR /src
CMD ["python3", "test.py", "/wall_river.txt"]
