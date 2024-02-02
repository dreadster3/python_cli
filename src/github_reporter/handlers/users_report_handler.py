import logging
from diator.requests.request_handler import RequestHandler
from github_reporter.clients.github_client import GithubClient

from github_reporter.requests.users_report_request import UsersReportRequest


class UsersReportHandler(RequestHandler[UsersReportRequest, None]):
    def __init__(self, client: GithubClient):
        self.__client: GithubClient = client
        self.__logger = logging.getLogger(__name__)

    async def handle(self, request: UsersReportRequest) -> None:
        self.__logger.info(self.__client.get_user("dreadster3"))
        return None
