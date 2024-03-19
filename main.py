#1
def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                
                name, salary_str = line.strip().split(',')
                
                salary = int(salary_str)
                
                total_salary += salary
               
                num_developers += 1
    except FileNotFoundError:
        print("Error: File not found.")
        return None, None
    except ValueError:
        print("Error: File contains invalid data.")
        return None, None
    
    if num_developers > 0:
        average_salary = total_salary / num_developers
    else:
        average_salary = 0

    return total_salary, average_salary

total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Total salary: {total}, Average salary: {average}")

        
        
#2
        
    def get_cats_info(path):
    try:
        cats_info = []

        
        with open(path, 'r') as file:
            
            for line in file:
                
                cat_id, name, age = line.strip().split(',')
               
                cats_info.append({"id": cat_id, "name": name, "age": age})

        return cats_info

    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)   
        
        
#3
        
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in concats:
        raise KeyError("Contact")
    contacts[name] = phone
    return "contact updated successfully"

def show_contact(args, contacts):
    name, _ = args
    return contacts[name]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_contact(args,contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()    