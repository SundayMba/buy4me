class Test:
    username = "mba"
    def __init__(self, **kwargs) -> None:
        print(kwargs.get("name"))

test = Test(**{"name": "kama"})