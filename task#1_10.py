import pulp

# Створення проблеми оптимізації
# В імені проблеми немає пробілів, щоб уникнути попереджень
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
# Змінимо імена змінних для уникнення пробілів
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

# Функція мети
# Мета - максимізувати загальну кількість вироблених напоїв
problem += lemonade + fruit_juice, "Total_Products"

# Обмеження
# Додаємо обмеження на використання ресурсів: води, цукру, лимонного соку та фруктового пюре
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Рішення задачі
# Виконуємо розв'язання задачі
problem.solve()

# Виведення результатів
# Виводимо оптимальну кількість виробництва "Лимонаду" та "Фруктового соку"
print("Оптимальна кількість виробництва Лимонаду:", pulp.value(lemonade))
print("Оптимальна кількість виробництва Фруктового соку:", pulp.value(fruit_juice))
