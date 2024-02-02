from github_reporter.requests.base_request import BaseRequest


class UsersReportRequest(BaseRequest):
    def __init__(self, limit: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = limit
