CREATE TABLE uptime (
    start_time TIMESTAMP WITHOUT TIME ZONE,
    duration INTERVAL
);

COPY uptime FROM '/csv' CSV;
