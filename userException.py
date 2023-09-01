class customException(Exception):
    def __int__(self, msg):
        super().__init__(msg)
        self.msg = msg

