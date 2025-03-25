import functions
import time

now = time.strftime('%b-%d-%Y %H:%M:%S')
print('it is:', now)

while True:
    user_actions = input('type add, show, edit, complete or exit:')
    user_actions = user_actions.strip()

    if user_actions.startswith('add'):
        action = user_actions[4:]
        todos = functions.get_todos()
        todos.append(action + '\n')
        functions.write_todos(todos)

    elif user_actions.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)
        functions.write_todos(todos)

    elif user_actions.startswith('edit'):
        try:
            edit = int(user_actions[5:])
            number = edit - 1
            todos = functions.get_todos()
            edit_new = input('what change you want:')
            todos[number] = edit_new
            functions.write_todos(todos)
        except ValueError:
            print('The index is out of range')
            continue

    elif user_actions.startswith('complete'):
        try:
            complete = int(user_actions[9:])
            index_remove = complete - 1
            todos = functions.get_todos()
            todo_to_remove = todos[index_remove].strip('\n')
            todos.pop(index_remove)

            functions.write_todos(todos)

            message = f'todo: {todo_to_remove} will be removed'
            print(message)
        except IndexError:
            print('there is no item with that number')
            continue
    elif user_actions.startswith('exit'):
        print('Bye')
        break
    else:
        print('No command are mathc')
        break