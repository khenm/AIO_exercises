import math


def is_number(n):
    try:
        float(n)    # Type-casting the string to 'float'
        # If string is not a valid 'float'
        # it'll raise 'ValueError' exception
    except ValueError:
        return False
    return True


def activation_func():
    """Computing sigmoid or relu or elu function based
    on function and variable choice from input. 
    If not match function name, end function.  
    Returns: 
        print the result after computing f(x) based on the 
        activation function from input.  
    """
    # get input
    x = input('Input x = ')
    activation_choice: str = input(
        'Input activation function (sigmoid|relu|elu): ')

    # input condition
    if is_number(x):
        x = float(x)  # convert x into float type
    else:
        print('x must be a number')
        return
    if activation_choice not in ('sigmoid', 'relu', 'elu'):
        print(f'{activation_choice} is not supported')
        return

    # sigmoid function
    if activation_choice == 'sigmoid':
        sigmoid_x: float = 1 / (1 + math.exp(-x))
        print(f'sigmoid: f({x}) = {sigmoid_x}')
        return

    # relu function
    if activation_choice == 'relu':
        relu_x: float = 0 if x <= 0 else x
        print(f'relu: f({x}) = {relu_x}')
        return

    # elu function
    if activation_choice == 'elu':
        alpha: float = 0.01  # coefficient alpha
        elu_x: float = alpha * (math.exp(x) - 1) if x <= 0 else x
        print(f'elu: f({x}) = {elu_x}')


def main():
    activation_func()


if __name__ == "__main__":
    main()
