import re
import time
from typing import Callable


def timeit(N: float):
    def decorate(func: Callable):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            time_delta = end_time - start_time
            print(f'Время выполнения функции: {time_delta}')
            if time_delta > N:
                print(f'Время выполнения функции больше чем N на {time_delta - N}')
            return result

        return wrapper

    return decorate


def find_emails(input_file: str) -> str:
    with open(input_file, 'r', encoding='utf-8') as f:
        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        for line in f:
            result = pattern.findall(line)
            for email in result:
                yield email


@timeit(N=0.00014)
def copy_emails_to_file(input_file: str, output_file: str) -> None:
    with open(output_file, 'w', encoding='utf-8') as f:
        emails_generator = find_emails(input_file)
        for email in emails_generator:
            f.write(email + '\n')


copy_emails_to_file('task_6_text_file.txt', 'task_6_result.txt')
