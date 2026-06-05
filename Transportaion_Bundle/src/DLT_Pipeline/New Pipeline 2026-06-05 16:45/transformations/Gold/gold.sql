CREATE OR REPLACE VIEW driving.gold.fact_trips AS
SELECT
    t.id,
    t.business_date,
    t.city_id,
    c.city_name,
    t.passenger_category,
    t.distance_kms,
    t.sales_amt,
    t.passenger_rating,
    t.driver_rating
FROM driving.silver.trips t
JOIN driving.silver.city_silver c
    ON t.city_id = c.city_id;