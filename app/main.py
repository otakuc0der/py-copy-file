import os


def copy_file(command: str) -> None:
    command_elems = command.split()
    if len(command_elems) == 3:
        command, file_to_copy, new_file_name = command.split()
        if (
            command == "cp"
            and os.path.exists(file_to_copy)
            and file_to_copy != new_file_name
        ):
            with (
                open(file_to_copy, "r") as file_in,
                open(new_file_name, "w") as file_out
            ):
                file_out.write(file_in.read())
