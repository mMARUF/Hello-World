FROM pythonL3.9.1

WORKDIR /usr/src/ app

COPY demoimg.jpg .
COPY taskB.py

RUN pip install  --no-cache-dir -r requirements.txt
COPY requirements.txt
RUN pip install  --no-cache-dir -r requirements.txt

CMD ["python", ./"taskB.py" ]
