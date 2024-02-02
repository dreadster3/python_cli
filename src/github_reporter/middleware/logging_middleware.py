import logging
from diator.middlewares import Middleware
from diator.middlewares.base import HandleType, Request, Res


class LoggingMiddlware(Middleware):
    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    async def __call__(self, request: Request, handle: HandleType) -> Res:
        self.__logger.info("Handling request %s", request.request_id)
        result = await handle(request)
        return result
