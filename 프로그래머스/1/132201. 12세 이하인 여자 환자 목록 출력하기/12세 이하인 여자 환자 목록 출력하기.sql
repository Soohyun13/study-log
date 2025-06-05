-- 코드를 입력하세요
# 12세이하여 / 이름 번호 성별코드 나이 전화번호
# 전화번호 없으면 NONE / 나이내림 이름오름
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;