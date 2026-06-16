SELECT email from person
GROUP BY email
HAVING COUNT(email) >= 2;