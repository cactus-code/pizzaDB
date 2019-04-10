SELECT 
    Pizza.name as Pizza
FROM 
    Pizza, Topping, PizzaTopping
WHERE
    Topping.name = 'Ham'
AND
    Pizza.id = PizzaTopping.pid
AND
    Topping.id = PizzaTopping.tid