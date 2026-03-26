def goida():
    print('\n=== Goida Menu ===')
    print('[1] Показать характеристики игрока')
    print('[2] Показать характеристики игрока')

    actions = {
        "1": lambda: print("Шо"),
        "2": lambda: print("Шо2")
    }
    return actions


def debug_menu():
    print('\n=== Debug Menu ===')
    print('[1] Показать характеристики игрока')
    print('[2] Показать характеристики игрока')

    actions = {
        "1": lambda: print("Шо"),
        "2": goida
    }
    return actions

def handle_actions(actions_menu, choice):
    for actions in actions_menu:
        if str(choice) in actions:
            if callable(actions_menu[actions]):
                actions_menu[actions]()
                break
            else:
                print(actions_menu[actions])
                break
    else:
        print('Неверный выбор. Пожалуйста, выберите действие из меню.')
        return True