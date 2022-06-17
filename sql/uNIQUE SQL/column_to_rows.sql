SELECT PRODUCT_ID, "store1" AS store, STORE1 AS price
FROM PRODUCTS
WHERE STORE1 IS NOT NULL
UNION
SELECT PRODUCT_ID, "store2" AS store, STORE2 AS price
FROM PRODUCTS
WHERE STORE2 IS NOT NULL
UNION
SELECT PRODUCT_ID, "store3" AS store, STORE3 AS price
FROM PRODUCTS
WHERE STORE3 IS NOT NULL