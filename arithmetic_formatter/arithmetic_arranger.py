def arithmetic_arranger(problems, show_solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        operands = problem.split()
        operand1 = operands[0]
        operator = operands[1]
        operand2 = operands[2]

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        result = str(eval(problem))

        line1 += operand1.rjust(width)
        line2 += operator + operand2.rjust(width - 1)
        line3 += "-" * width
        line4 += result.rjust(width)

        if problem != problems[-1]:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if show_solution:
        arranged_problems += "\n" + line4

    return arranged_problems
