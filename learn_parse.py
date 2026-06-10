
def parse_args(parts):

    args = {}

    for part in parts[1:]:

        if "=" in part:

            param_name, param_value = part.split("=", 1)

            args[key] = value

    return args

def terminal():
    running = True

    while running:
        user_input = input("> ")
        parts = user_input.split()

        if not parts:
            continue

        cmd = parts[0].lower()
        args=parse_args(parts)
        print(args)


terminal()




