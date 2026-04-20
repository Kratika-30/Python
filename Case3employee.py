class Employee:
    def __init__(self):
        self.__emp_id = 0
        self.name = ""
        self.basic = 0.0

    def inputDetails(self):
        self.emp_id = int(input("Enter employee ID:"))
        self.name = input("Enter Name:")
        self.basic = float(input("Enter Basic Salary:"))

class SalaryOut(Employee):
    def calculateSalaray(self):
        self.hra = 0.20*self.basic
        self.da = 0.10*self.basic
        self.tax = 0.05*self.basic

        self.gross = self.basic + self.hra + self.da
        self.net = self.gross - self.tax

    def displaySalaray(self):
        print("Salary Details-->")
        print("ID:",self.emp_id)
        print("Name:",self.name)
        print("Basic Salary:",self.basic)
        print("HRA:",self.hra)
        print("DA:",self.da)
        print("Tax:",self.tax)
        print("Gross Salary:",self.gross)
        print("Net Salary:",self.net)

if __name__ == "__main__":
    emp = SalaryOut()
    emp.inputDetails()
    emp.calculateSalaray()
    emp.displaySalaray()