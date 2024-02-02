import asyncio
import logging
from os import environ
import rodi
from diator.mediator import Mediator
from diator.requests import RequestMap
from diator.events import EventEmitter, EventMap
from diator.middlewares import MiddlewareChain
from diator.container.protocol import Container
from diator.container.rodi import RodiContainer
from github_reporter.cli.setup import setup_cli
from github_reporter.clients.github_client import GithubClient
from github_reporter.handlers.users_report_handler import UsersReportHandler
from github_reporter.middleware.logging_middleware import LoggingMiddlware
from github_reporter.requests.users_report_request import UsersReportRequest


async def __main(mediator: Mediator, args):
    arguments = vars(args)
    request = args.request(**arguments)
    await mediator.send(request)


# Configure middlewares
def configure_middlewares() -> MiddlewareChain:
    middleware_chain = MiddlewareChain()
    middleware_chain.add(LoggingMiddlware())

    return middleware_chain


# Configure events
def configure_events() -> EventMap:
    event_map = EventMap()
    return event_map


# Configure request handlers
def configure_request_handlers() -> RequestMap:
    request_map = RequestMap()
    request_map.bind(UsersReportRequest, UsersReportHandler)
    return request_map


# Configure DI
def configure_di() -> Container:
    container = rodi.Container()
    container.add_scoped_by_factory(
        lambda: GithubClient(environ.get("BOT_READER_PAT", "")), GithubClient)

    # Register request handlers
    container.register(UsersReportHandler)

    rodi_container = RodiContainer()
    rodi_container.attach_external_container(container)

    return rodi_container


def main():
    logging.basicConfig(level=logging.INFO)
    parser = setup_cli()
    args = parser.parse_args()

    middlewares = configure_middlewares()
    event_map = configure_events()
    request_map = configure_request_handlers()
    container = configure_di()

    event_emitter = EventEmitter(event_map, container, None)

    mediator = Mediator(request_map, container, event_emitter, middlewares)

    asyncio.run(__main(mediator, args))
