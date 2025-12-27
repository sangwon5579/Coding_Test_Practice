SELECT C.CART_ID AS CART_ID
FROM CART_PRODUCTS C JOIN (
                            SELECT *
                            FROM CART_PRODUCTS
                            WHERE NAME = "Milk" OR NAME = "Yogurt"
) CP ON C.ID = CP.ID
GROUP BY C.CART_ID
HAVING COUNT(DISTINCT C.NAME) >= 2
ORDER BY CART_ID