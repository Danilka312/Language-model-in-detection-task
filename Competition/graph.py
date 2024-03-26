import matplotlib.pyplot as plt

# Считываем данные из файла efficiency_BERT.txt
with open("efficiency_BERT.txt", "r") as file:
    efficiency_bert = [float(line.strip()) for line in file]

# Считываем данные из файла efficiency_MISTRAL.txt
with open("efficiency_MISTRAL.txt", "r") as file:
    efficiency_mistral = [float(line.strip()) for line in file]

# Создаем фигуру и оси для графиков
fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Строим график для BERT
ax[0].plot(efficiency_bert, label='BERT')
ax[0].set_ylabel('Эффективность')

# Строим график для MISTRAL
ax[1].plot(efficiency_mistral, label='MISTRAL')
ax[1].set_ylabel('Эффективность')
ax[1].set_xlabel('Номер примера')

# Добавляем заголовок
fig.suptitle('Сравнение эффективности моделей BERT и MISTRAL')

# Отображаем графики
plt.show()
