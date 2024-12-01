-- USER_INFO 테이블에서 나이 정보가 없는 회원이 몇 명인지 출력
SELECT
    COUNT(*) AS USERS
FROM
    USER_INFO
WHERE
    AGE IS NULL;
    