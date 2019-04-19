a note on lambda functions
===
# introduction
this is a short overview of lambda functions and their use in python. 

## what 
lambda functions are a compact way (usually a one-liner) to define and execute a small/simple, *one-time*, *unnamed* function that does exactly what you need and then disappears. while defined, a lambda function is just like any other function.

## why
they are especially useful for transforming data on the fly in a one liner using transformation functions,  e.g. `apply()`, `map()`, `filter()`. these functions apply some transform across multiple inputs, and they expect functions as input arguments (as well as the list of inputs). if the a  transformation that does everything you want does not exist, you have to create a new function. if the transformation only needs to happens once  (like in the `datetime` exercise), it is unnecessary to define a whole separate named function for it separately - that function would only be called once. so that's where lambda functions are useful.

## how
instead of the usual function definition format:

```
def function_name(argument1, argument2):
   <do stuff>
   return value
```

which we then would invoke with `value = function_name(variable1, variable2)` wherever we wanted the `value`, we instead use the `lambda` keyword and then give the function actions in-line where we want value, like so: 

```(lambda <input var(s)> : <expression with input var(s)>)```

for example, if we need to convert from a ratio to a percentage by multiplying by 100 and rounding down to single digit precision, we can do that by a lambda function like so:

```lambda ratio: round(ratio*100,1)``` 

and putting that as the function argument to a call of a transform function, e.g.

```map(lambda ratio: round(ratio,1), list_of_ratio_values)```