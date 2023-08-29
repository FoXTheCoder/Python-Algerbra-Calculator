from math import sqrt

def quadratic_solver(a, b, c):
    D = (b * b) - (4 * a * c)

    if D < 0:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(-D) / (2 * a)
        return (f"x1 = {real_part} + {imaginary_part}i", f"x2 = {real_part} - {imaginary_part}i")
    elif D == 0:
        x = -b / (2 * a)
        return f"x = {x}"
    else:
        square_root_D = sqrt(D)
        two_a = 2 * a
        x1 = (-b + square_root_D) / two_a
        x2 = (-b - square_root_D) / two_a
        return (f"x1 = {x1}", f"x2 = {x2}")

def alpha_beta_solver(a, b, c):
    alpha = (-1 * b) / (2 * a)
    beta = (4 * a * c) + (b * b) / (4 * a)
    function_expression = f"{a}*(x+{alpha})²+{beta}"
    return alpha, beta, function_expression

def quadratic_solver_formule():
    return (
        "Quadratic Formula: ax^2 + bx + c = 0",
        "Discriminant: D = b^2 - 4ac",
        "x1 = (-b + sqrt(D)) / (2a)",
        "x2 = (-b - sqrt(D)) / (2a)"
    )

def alpha_beta_solver_formule():
    return (
        "Alpha and Beta Solver formules:",
        "alpha = (-b) / (2a)",
        "beta = (4ac + b^2) / (4a)",
        "Function Expression: a * (x + alpha)^2 + beta"
    )

def main():
    print("Welcome to my algebra solver\n")
    print("! Made by FoxTheCoder !")

    menu1 = "1: Quadratic solver\n2: Alpha and Beta solver\n3: Display formulas\n4: Credits\n\n"
    answer1 = input(menu1)

    if answer1 == "1":
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        solutions = quadratic_solver(a, b, c)
        for solution in solutions:
            print(solution)
    
    elif answer1 == "2":
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        alpha, beta, function_expression = alpha_beta_solver(a, b, c)
        print(f"alpha = {alpha}")
        print(f"beta = {beta}")
        print(f"top = {alpha};{beta}")
        print(f"function expression = {function_expression}")
    
    elif answer1 == "3":
        menu2 = "1: Quadratic solver Formule\n2: Alpha and Beta solver formule\n"
        answer2 = input(menu2)
        if answer2 == "1":
            formulas = quadratic_solver_formule()
        elif answer2 == "2":
            formulas = alpha_beta_solver_formule()
        else:
            print("Choose a correct option")
            return
        
        for formula in formulas:
            print(formula)
    
    elif answer1 == "4":
        print("\nCredits:")
        print("Made by FoxTheCoder"
    
    else:
        print("\nChoose a correct option")

if __name__ == "__main__":
    main()
