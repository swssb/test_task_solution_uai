def count_words_in_string(file) -> None:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(f'{len(line.split())} words in line')


count_words_in_string('task_5_text_file.txt')
