-- ITEM_A(ROOT) -> ITEM_B(PARENT) -> ITEM_C(PARENT)
-- ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 

SELECT
    it.ITEM_ID,
    ii.ITEM_NAME
FROM
    ITEM_TREE AS it
INNER JOIN
    ITEM_INFO AS ii
    ON it.ITEM_ID = ii.ITEM_ID
WHERE
    it.PARENT_ITEM_ID IS NULL;