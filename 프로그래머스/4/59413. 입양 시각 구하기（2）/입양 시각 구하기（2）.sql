-- 코드를 입력하세요
WITH RECURSIVE hours AS (
    SELECT 0 AS hour
    UNION ALL
    SELECT hour + 1 FROM hours WHERE hour < 23
)

SELECT
    h.hour AS HOUR,
    COUNT(ANIMAL_ID) AS COUNT
FROM hours h
LEFT JOIN ANIMAL_OUTS a ON HOUR(DATETIME) = h.hour
GROUP BY hour
ORDER BY hour;