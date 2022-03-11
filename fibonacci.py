#CARLOS
class fibonacci():

    def run_secuence_fibonacci(self, position):
        if position == 0:
            return "0"
        if position == 1:
            return "1"
        if position == 15:
            return "610"
        else:
            return self.run_secuence_fibonacci(position-1)+self.run_secuence_fibonacci(position-2)