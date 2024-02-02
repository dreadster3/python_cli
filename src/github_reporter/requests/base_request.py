from diator.requests.request import Request


class BaseRequest(Request):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.verbose = kwargs.pop("verbose", False)
