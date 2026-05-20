from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = []


@app.route('/')
def index():
    return render_template(
        'index.html',
        employees=employees
    )


# CREATE
@app.route('/add', methods=['POST'])
def add_employee():
    employee_name = request.form.get('employee_name')

    if employee_name:
        employees.append(employee_name.strip())

    return redirect(url_for('index'))


# DELETE
@app.route('/delete/<int:index>')
def delete_employee(index):

    if 0 <= index < len(employees):
        employees.pop(index)

    return redirect(url_for('index'))


# ✏️ EDIT PAGE
@app.route('/edit/<int:index>')
def edit_employee(index):

    if 0 <= index < len(employees):
        return render_template(
            'edit.html',
            employee=employees[index],
            index=index
        )

    return redirect(url_for('index'))


# ✏️ UPDATE ACTION
@app.route('/update/<int:index>', methods=['POST'])
def update_employee(index):

    if 0 <= index < len(employees):
        updated_name = request.form.get('employee_name')

        if updated_name:
            employees[index] = updated_name.strip()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )