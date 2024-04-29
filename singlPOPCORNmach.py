class PopcornMachine:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new_(cls)