import os

# Exercitiul 1 - Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
def get_extensions_from_dir(director):
    ext = []
    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            ext.append(os.path.splitext(file)[1])
    return sorted(set(ext))


# Exercitiul 2 - Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul directorului de la calea folder,
# ce incepe cu litera A.
def write_files_with_A(director, fisier):
    with open(fisier, 'w') as fin:
        for file in os.listdir(director):
            if os.path.isfile(os.path.join(director, file)) and file.startswith('A'):
                fin.write(os.path.join(director, file) + '\n')


# Exercitiul 3 - Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un director,
# se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie.
# Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
def get_last_chars_or_tuple(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'r') as fin:
            return fin.read()[-20:]
    elif os.path.isdir(my_path):
        ext = {}
        for root, dirs, files in os.walk(my_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension in ext:
                    ext[extension] += 1
                else:
                    ext[extension] = 1
        return sorted(ext.items(), key=lambda x: x[1], reverse=True)


# Exercitiul 4 - Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv).
# Lista trebuie să fie sortată crescător. Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.
def get_extensions_from_dir_2(director):
    ext = []
    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            ext.append(os.path.splitext(file)[1])
    return sorted(set(ext))


# Exercitiul 5 - Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o listă de fișiere care conțin to_search.
# Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
# Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
def search_in_file_or_dir(target, to_search):
    if os.path.isfile(target):
        with open(target, 'r') as fin:
            if to_search in fin.read():
                return [target]
    elif os.path.isdir(target):
        files = []
        for root, dirs, files in os.walk(target):
            for file in files:
                with open(os.path.join(root, file), 'r') as fin:
                    if to_search in fin.read():
                        files.append(os.path.join(root, file))
        return files
    else:
        raise ValueError("Target is not a file or a directory")


# Exercitiul 6 - Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus:
# o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor(nu se pot deschide, etc), se va apela funcția respectivă cu instanța excepției ca parametru.
def search_in_file(file_path, to_search, callback):
    try:
        with open(file_path, 'r') as fin:
            if to_search in fin.read():
                return file_path
    except Exception as e:
        callback(e)
    return None


def search_in_file_or_dir_with_callback(target, to_search, callback):
    if os.path.isfile(target):
        result = search_in_file(target, to_search, callback)
        return [result] if result else []

    elif os.path.isdir(target):
        files_containing_to_search = []
        for root, dirs, files in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                result = search_in_file(file_path, to_search, callback)
                if result:
                    files_containing_to_search.append(result)
        return files_containing_to_search

    else:
        callback("Target is not a file or a directory")


def error_callback(exception):
    print(f"An error occurred: {str(exception)}")


# Exercitiul 7 - Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu următoarele cămpuri:
# full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.
def get_file_info(file_path):
    if os.path.isfile(file_path):
        file_info = {'full_path': os.path.abspath(file_path), 'file_size': os.path.getsize(file_path),
                     'file_extension': os.path.splitext(file_path)[1], 'can_read': os.access(file_path, os.R_OK),
                     'can_write': os.access(file_path, os.W_OK)}
        return file_info
    else:
        raise ValueError("Target is not a file")


# Exercitiul 8 - Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
def get_files_from_dir(dir_path):
    files_return = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            files_return.append(os.path.join(root, file))
    return files_return


if __name__ == '__main__':
    # Exercitiul 1
    director = input("Introduceti calea catre director: ")
    print(get_extensions_from_dir(director))

    # Exercitiul 2
    director = input("Introduceti calea catre director: ")
    fisier = input("Introduceti calea catre fisier: ")
    write_files_with_A(director, fisier)

    # Exercitiul 3
    my_path = input("Introduceti calea catre fisier/director: ")
    print(get_last_chars_or_tuple(my_path))

    # Exercitiul 4
    director = input("Introduceti calea catre director: ")
    print(get_extensions_from_dir_2(director))

    # Exercitiul 5
    target = input("Introduceti calea catre fisier/director: ")
    to_search = input("Introduceti sirul de caractere: ")
    print(search_in_file_or_dir(target, to_search))

    # Exercitiul 6
    target = input("Introduceti calea catre fisier/director: ")
    to_search = input("Introduceti sirul de caractere: ")
    print(search_in_file_or_dir_with_callback(target, to_search, error_callback))

    # Exercitiul 7
    file_path = input("Introduceti calea catre fisier: ")
    print(get_file_info(file_path))

    # Exercitiul 8
    dir_path = input("Introduceti calea catre director: ")
    print(get_files_from_dir(dir_path))





