import argparse
from github_reporter.requests.users_report_request import UsersReportRequest


def setup_cli():
    parser = argparse.ArgumentParser(description='A simple CLI tool')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='enable verbose mode')

    subparsers = parser.add_subparsers(help='sub-command help')

    generate_parent_parser = argparse.ArgumentParser(add_help=False)
    generate_parent_parser.add_argument(
        "name", type=str, help="name of the file")

    generate_parser = subparsers.add_parser('generate', help='generate help')
    generate_parser.add_argument(
        '-p', "--p", type=str, help='path to folder to store file', required=False, default='.')

    generate_subparsers = generate_parser.add_subparsers(
        help='sub-command help')

    users_parser = generate_subparsers.add_parser(
        'users', help='users help', parents=[generate_parent_parser])
    users_parser.add_argument(
        "-l", "--limit", type=int, help="limit of users to show")
    users_parser.set_defaults(request=UsersReportRequest)

    return parser
