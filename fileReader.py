file_name = input("Please write the name or destination of the fie which you want to read")
file = open(file_name)
file_reader = file.read()
print(file_reader)