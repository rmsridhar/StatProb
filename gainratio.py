from info_gain import info_gain

# Example of color to indicate whether something is fruit or vegatable
produce = ['apple', 'apple', 'apple', 'strawberry', 'eggplant']
fruit   = [ True  ,  True  ,  True  ,  True       ,  False    ]
colour  = ['green', 'green', 'red'  , 'red'       , 'purple'  ]

ig  = info_gain.info_gain(fruit, colour)
iv  = info_gain.intrinsic_value(fruit, colour)
igr = info_gain.info_gain_ratio(fruit, colour)

print(ig, iv, igr)
