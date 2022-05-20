from functools import wraps
from datetime import datetime
import time
import os


def logger(input_path):
    
    def _logger(old_function):
        @wraps(old_function)
        def new_function(*args):
        
            print(f"вызвана функция {old_function.__name__} с аргументами {args}")
            call_time = time.time()
            date_log = datetime.fromtimestamp(call_time).strftime('%x-%X')
            result = old_function(*args)
            if not os.path.exists(input_path):
                os.makedirs(input_path)
                print('make_dir')   
            path_write = input_path + '/'
            with open(path_write + 'logger.txt', 'a', encoding='utf-8') as f:
                print(f"Дата и время вызова: {date_log}, Имя: {old_function.__name__},\n\tАргументы: {args}, Результат: {result} ", file=f)
            
            return result
        return new_function
    return _logger
