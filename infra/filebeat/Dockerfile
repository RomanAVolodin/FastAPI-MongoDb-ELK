FROM elastic/filebeat:8.10.2

COPY filebeat.yaml /usr/share/filebeat/filebeat.yml
USER root
RUN chown -R root /usr/share/filebeat/
RUN chmod -R go-w /usr/share/filebeat/