import fail

while True:
    text = input('fail >> ')
    result, error = fail.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
