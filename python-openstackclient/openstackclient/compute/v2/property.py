import logging

from cliff import columns as cliff_columns
import iso8601
from novaclient import api_versions
from novaclient.v2 import servers
from openstack import exceptions as sdk_exceptions
from openstack import utils as sdk_utils
from osc_lib.cli import format_columns
from osc_lib.cli import parseractions
from osc_lib.command import command
from osc_lib import exceptions
from osc_lib import utils
from oslo_utils import strutils

from openstackclient.i18n import _
from openstackclient.identity import common as identity_common
from openstackclient.network import common as network_common


class CreatePropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(CreatePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'NAMESPACE',
            metavar='<NAMESPACE>',
            help=_('NAMESPACE'),
        )
        parser.add_argument(
            '--name',
            metavar='<NAME>',
            help=_('NAME'),
        )
        parser.add_argument(
            '--title',
            metavar='<TITLE>',
            help=_('TITLE'),
        )
        parser.add_argument(
            '--schema',
            metavar='<SCHEMA>',
            help=_('SCHEMA'),
        )
        return parser

    def take_action(self, parsed_args):
        print("NAMESPACE : " + parsed_args.NAMESPACE)
        print("name : " + parsed_args.name)
        print("title : " + parsed_args.title)
        print("schema : " + parsed_args.schema)