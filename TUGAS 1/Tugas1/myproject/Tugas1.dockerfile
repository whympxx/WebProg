FROM python:3.9-slim-buster
RUN mkdirapp 
WORKDIR /Tugas1 

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \ 
&& pip install --no-cache-dir -r 
requirements.txt

COPY ./Tugas1
EXPOSE 5000
ENTRYPOINT [ "python" ]CMD ["index.py" ]
