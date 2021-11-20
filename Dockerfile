FROM python:3.9
ENV PYTHONBUFFERD=1
RUN mkdir /teacherapp
ADD . /teacherapp
WORKDIR /teacherapp
RUN pip install -r requirements.txt