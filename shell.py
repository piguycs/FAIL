import fail

while True:
    text = input('fail >>')
    result, error = fail.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
