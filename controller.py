import math_functions as m
import gui as g
import data_base as db

def button_click():
    result = 0
    value_a = g.get_value()
    value_b = g.get_value()
    func = g.get_function()

    db.get_storage(value_a)
    db.get_storage(value_b)  

    m.init(value_a, value_b)
    match func:
        case 1:
            result = m.f_sum() 
        case 2:
            result = m.f_sub()
        case 3:
            result = m.f_mult()
        case 4:
            result = m.f_div() 
    g.view_data(result)