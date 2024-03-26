global_penalty = 0
# Открываем файл text.txt для чтения
with open("keywords_oracle.txt", "r") as file1:
    # Открываем файл text2.txt для чтения
    with open("keywords_BERT.txt", "r") as file2:
        # Открываем файл для записи
        with open("efficiency_BERT.txt", "w") as result_file:
            # Считываем строки из обоих файлов по очереди
            for line1, line2 in zip(file1, file2):
                # Разбиваем строки на слова
                words1 = set(line1.strip().split(','))
                words2 = set(line2.strip().split(','))
               
                penalty = len(words2) - len(words1)
                
                if penalty < 0:
                    penalty = 0
                
                global_penalty += penalty
                
                common_words = [word for word in words1 if word in words2]

                efficiency = len(common_words) / len(words1)
                
                # Записываем результат в файл
                result_file.write(str(efficiency) + '\n')

# Выводим общее несоответствие
print("Global Penalty:", global_penalty)
