def get_todos(filepath="../Files/todos.txt"):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_todos(todos_arg, filepath="../Files/todos.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as local_file2:
        local_file2.writelines(todos_arg)

