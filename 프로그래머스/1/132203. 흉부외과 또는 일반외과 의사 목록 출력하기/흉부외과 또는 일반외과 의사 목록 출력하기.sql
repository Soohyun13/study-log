-- 코드를 입력하세요
# 흉부외과 OR 일반외과 / 이름 ID 진료과 고용일자 / 고용내림 이름오름
SELECT
    DR_NAME,
    DR_ID,
    MCDP_CD,
    DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS 'HIRE_YMD'
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME;