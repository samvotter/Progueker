class EnumDict(dict):

    def __init__(self):
        super().__init__(**self.__dict__)
