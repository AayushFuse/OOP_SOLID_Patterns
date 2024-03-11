class SayHello:
    def __init__(self) -> None:
        print("Hi")

    def __str__(self) -> str:
        return "Hello from SayHello class"
    


print(SayHello())