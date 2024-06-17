error: str = 'n must be an integer greater than 0'
def factorial(x: int) -> int:
    """Calculate factorial of given number

    Args:
        x (int): input

    Returns:
        int: factorial(x)
    """
    result: int = 1
    for i in range(x, 1, -1):
        result *= i
    return result


def approx_sin(x: float, n: int) -> float:
    """Approximate sin function 

    Args:
        x (float): radian
        n (int): numbers of times looped to apporoximate

    Returns:
        float: sin(x)
    """
    # input condition
    
    if n <= 0:
        print(error)
        return 0
    result: float = 0
    for i in range(n):
        result += (-1)**i * ((x ** (2 * i + 1))/factorial(2 * i + 1))
    return result


def approx_cos(x: float, n: int) -> float:
    """Approximate cos function 

    Args:
        x (float): radian
        n (int): numbers of times looped to apporoximate

    Returns:
        float: cos(x)
    """
    # input condition
    if n <= 0:
        print(error)
        return 0
    result: float = 0
    for i in range(n):
        result += (-1)**i * ((x ** (2 * i))/factorial(2 * i))
    return result


def approx_sinh(x: float, n: int) -> float:
    """Approximate sinh function 

    Args:
        x (float): radian
        n (int): numbers of times looped to apporoximate

    Returns:
        float: sinh(x)
    """
    # input condition
    if n <= 0:
        print(error)
        return 0
    result: float = 0
    for i in range(n):
        result += ((x ** (2 * i + 1))/factorial(2 * i + 1))
    return result


def approx_cosh(x: float, n: int) -> float:
    """Approximate cosh function 

    Args:
        x (float): radian
        n (int): numbers of times looped to apporoximate

    Returns:
        float: cosh(x)
    """
    # input condition
    if n <= 0:
        print(error)
        return 0
    result: float = 0
    for i in range(n):
        result += ((x ** (2 * i))/factorial(2 * i))
    return result


def main():
    approx_cos(3.140, 10)


if __name__ == "__main__":
    main()
