SELECT 
    Topping.name as Topping,
    Topping.description as Description
FROM 
    Pizza, Topping, PizzaTopping
WHERE
    Pizza.name = 'Thick Hawaiian'
AND
    Pizza.id = PizzaTopping.pid
AND
    Topping.id = PizzaTopping.tid