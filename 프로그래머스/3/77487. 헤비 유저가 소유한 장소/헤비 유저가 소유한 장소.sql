SELECT P.ID, P.NAME, P.HOST_ID
FROM PLACES P JOIN (
                    SELECT *
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING COUNT(*) >= 2
) PP 
    ON P.HOST_ID = PP.HOST_ID

ORDER BY ID