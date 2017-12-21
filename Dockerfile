FROM python:2.7-alpine
MAINTAINER jieyang <admin@jevic.cn>
ENV EFRESHED_AT 2017-12-21

ENV TZ Asia/Shanghai
RUN pip install flask werkzeug requests

COPY ./alarm /alarm
COPY docker-entrypoint.sh /

ENTRYPOINT ["./docker-entrypoint.sh"]
EXPOSE 51001
CMD ["python","/alarm/alarm.py"]
