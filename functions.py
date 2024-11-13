FILEPATH = 'todos.txt'

def get_todos(file_dir=FILEPATH):
    """
    get to-do list from text file

    """
    with open(file_dir, 'r') as file_input:
        todos_list = file_input.readlines()
    return todos_list

def write_todos(todos_data,file_dir=FILEPATH):
    with open(file_dir, 'w') as file_output:
        file_output.writelines(todos_data)

if __name__=='__main__':
    print('Successfully Imported Functions Module')