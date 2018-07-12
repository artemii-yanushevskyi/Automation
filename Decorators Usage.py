    '''(Варіант 5) Т17.5 Побудувати декоратор, який перевіряє, чи належать усі параметри
декорованої функції заданому типу (ім’я цього типу є параметром декоратора). Якщо
ні, то ініціює виключення. Виконати перевірку роботи декоратора для функції, яка
обчислює середнє значення декількох числових змінних.
    '''
    '''Коли Python зустрічає позначення декоратора перед описом
функції f, він модифікує програмний код так, щоб замість
виклику функції був викликаний декоратор, а функція була
йому передана як параметр.
    '''
def extractor(function):
    types = [type(None), type(3)] # type int or type None
    def _extractor(*args, **kw):
        for a in args:
            if type(a) not in types: break
        else:
            for key, value in kw.items():
                if type(value) not in types: break
            else:
                function(*args, **kw)
    return _extractor
@extractor
def someFunction(*args, **kw):
    print(args)
    print(kw)

someFunction(5, 7, 8, 32, m=534, f=56)
