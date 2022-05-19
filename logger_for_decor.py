from datetime import datetime
import time


def logger(old_function):

    def new_function(*args):
      
        print(f"вызвана функция {old_function.__name__} с аргументами {args}")
        call_time = time.time()
        date_log = datetime.fromtimestamp(call_time).strftime('%x-%X')
        result = old_function(*args)
        
        with open('logger.txt', 'a', encoding='utf-8') as f:
            print(f"Дата и время вызова: {date_log}, Имя: {old_function.__name__},\n\tАргументы: {args}, Результат: {result} ", file=f)
        
        return result
    
    return new_function
