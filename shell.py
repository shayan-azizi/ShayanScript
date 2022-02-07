import main

while True:
    text = input("~ ")
    result, error = main.run('<stdin>', text)
    
    if error:
        print(error.as_string())
    else:
        print(result)