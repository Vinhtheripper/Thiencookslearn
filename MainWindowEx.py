from PyQt6 import QtWidgets
from MainWindow_K234111460 import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_salary)
        self.ui.pushButton_2.clicked.connect(self.prepare_next_entry)
        self.employee_counts = {'Intern': 0, 'Fresher': 0, 'Junior': 0, 'Senior': 0}
        self.salaries = {'Intern': 0, 'Fresher': 0, 'Junior': 0, 'Senior': 0}
    def calculate_salary(self):
        try:
            num_employees = int(self.ui.lineEdit.text())
            if num_employees <= 0:
                raise ValueError("Number of employees must be greater than zero.")

            if self.ui.radioButton.isChecked():
                role = 'Intern'
                salary_per_person = 2000000
            elif self.ui.radioButton_2.isChecked():
                role = 'Junior'
                salary_per_person = 15000000
            elif self.ui.radioButton_3.isChecked():
                role = 'Fresher'
                salary_per_person = 10000000
            elif self.ui.radioButton_4.isChecked():
                role = 'Senior'
                salary_per_person = 30000000
            else:
                QtWidgets.QMessageBox.warning(self, "Role Not Selected", "Please select an employee role.")
                return
            total_salary = num_employees * salary_per_person
            self.employee_counts[role] += num_employees
            self.salaries[role] += total_salary
            self.ui.lineEdit_2.setText(str(self.employee_counts['Intern']))
            self.ui.lineEdit_3.setText(str(self.employee_counts['Fresher']))
            self.ui.lineEdit_4.setText(str(self.employee_counts['Junior']))
            self.ui.lineEdit_5.setText(str(self.employee_counts['Senior']))
            self.ui.lineEdit_6.setText(str(self.salaries['Intern']))
            self.ui.lineEdit_8.setText(str(self.salaries['Fresher']))
            self.ui.lineEdit_9.setText(str(self.salaries['Junior']))
            self.ui.lineEdit_10.setText(str(self.salaries['Senior']))
            self.ui.lineEdit_11.setText(str(sum(self.salaries.values())))
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", str(e))
    def prepare_next_entry(self):
        self.ui.lineEdit.clear()
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
