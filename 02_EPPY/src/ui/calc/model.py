class Model:

    def __init__(self):
        pass

    def exec_expression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = 'OPERATION NOT SUPPORTED'

        return result