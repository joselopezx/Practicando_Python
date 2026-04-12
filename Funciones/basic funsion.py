#there are two pars above a function, Header and body
#Header
# The header function defines the name of the function and its argument(s).
# Every function header begins with def, which tells Python that we are about to define a function.
# The argument is the name of the variable that will be used as input to the function. It is always enclosed in perenteses that appear immediately after the name of the function. 
# A function can alse have no arguments, or it can heve multiple arguments. 

def add_three(input_var):        # Header whit add_three name and input_var as the arguments
    output_var = input_var + 3   # | Body has an add ant it returs the result variable output_var
    return output_var            # |

# Calling the function

add = add_three(10)
print(add)