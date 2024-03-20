#1
fh = open('salary.txt', 'w')
fh.write('Alex Korp,3000\n')
fh.write('Nikita Borisenko,2000\n')
fh.write('Sitarama Raju,1000\n')
fh.close()

fh = open('salary.txt', 'r')
all_file = fh.read()

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

fh.close()
        
        
#2
fh = open('cats.txt', 'w')
fh.write('60b90c1c13067a15887e1ae1,Tayson,3\n')
fh.write('60b90c2413067a15887e1ae2,Vika,1\n')
fh.write('60b90c2e13067a15887e1ae3,Barsik,2\n')
fh.write('60b90c3b13067a15887e1ae4,Simon,12\n')
fh.write('60b90c4613067a15887e1ae5,Tessi,5\n')
fh.close()

fh = open('cats.txt', 'r')
all_file = fh.read()

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

fh.close()        
        
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