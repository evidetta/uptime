PREPARE
  energy_prices (numeric, numeric) AS
WITH
  basic_metrics AS (
    SELECT
      EXTRACT(
        year
        FROM
          start_time
      ) AS "year",
      EXTRACT(
        month
        FROM
          start_time
      ) AS "month",
      SUM(
        EXTRACT(
          epoch
          FROM
            duration
        ) / 3600
      ) AS hours_on
    FROM
      uptime
    GROUP BY
      1,
      2
    ORDER BY
      1 DESC,
      2 DESC
  ),
  kilowatt_hours AS (
    SELECT
      *,
      hours_on * $1 AS kilowatt_hours
    FROM
      basic_metrics
  )
SELECT
  *,
  kilowatt_hours * $2 AS price
FROM
  kilowatt_hours;
