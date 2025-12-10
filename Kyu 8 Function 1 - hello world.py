# Creating a unique way of typing printing "hello world!" within its own function
greeting = "hello world!"
message = []
end = ""


def greet():
    for letter in greeting:
        message.append(letter)
        end = "".join(message)

    return end

print (greet())