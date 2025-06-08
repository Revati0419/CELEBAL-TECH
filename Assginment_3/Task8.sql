SELECT 
    COUNTRY.Continent, 
    FLOOR(AVG(CITY.Population)) AS AvgPopulation
FROM 
    CITY
JOIN 
    COUNTRY 
ON 
    CITY.CountryCode = COUNTRY.Code
GROUP BY 
    COUNTRY.Continent;
