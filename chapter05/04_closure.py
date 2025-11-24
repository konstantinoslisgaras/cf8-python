def department_id_generator(department):
    """
    Generates unique IDs for students based on departments.

    Params:
        department (str): The name of the department.

    Returns:
        function: A function that generates unique IDs for the given department.
    """
    last_id = 0
    def generate_id():
        """
        Generate a unique id for a student in the department.

        Returns:
            tuple: A tuple containing the unique ID as string and the last id as an integer.
        """
        nonlocal last_id
        last_id += 1
        return f"{department}-{last_id}", last_id

    return generate_id

def main():
    python_id_gen = department_id_generator("Python")
    print(python_id_gen())
    print(python_id_gen())
    print(python_id_gen())

    android_id_gen = department_id_generator("Android")
    print(android_id_gen())

if __name__ == "__main__":
    main()