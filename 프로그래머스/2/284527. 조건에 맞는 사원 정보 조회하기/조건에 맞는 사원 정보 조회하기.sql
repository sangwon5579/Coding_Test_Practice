SELECT J.SCORE, J.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM    HR_EMPLOYEES E JOIN 
        (
            SELECT G.EMP_NO AS EMP_NO, SUM(G.SCORE) AS SCORE
            FROM HR_EMPLOYEES E
                    JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
            WHERE G.YEAR = "2022"
            GROUP BY G.EMP_NO
            ORDER BY SUM(G.SCORE) DESC
            LIMIT 1
        ) AS J
        ON E.EMP_NO = J.EMP_NO
