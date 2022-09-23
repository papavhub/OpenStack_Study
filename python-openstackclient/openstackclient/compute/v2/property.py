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

import json
from openstackclient.common import utils
from osc_lib import utils
from openstackclient.compute.v2 import client

import requests


class CreatePropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(CreatePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
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

        image_client = self.app.client_manager.image
        # kwargs = {'namespace': parsed_args.namespace, "name": parsed_args.name, "title": parsed_args.title, "schema": parsed_args.schema}

        try:
            schema = json.loads(parsed_args.schema)
        except ValueError:
            print('Schema is not a valid JSON object.')
        else:
            fields = {'name': parsed_args.name, 'title': parsed_args.title}
            fields.update(schema)

            kwargs = {"name": parsed_args.name, "title": parsed_args.title, "type": fields["type"], "enum": fields["enum"], "description": fields["description"]}
            print(kwargs)
            metadata_object = image_client.create_metadata_property(**kwargs)

            # 출력
            schema = metadata_object.properties

            column_headers = (
                'Property',
                'Value',
            )

            columns = (
                ("description", schema["description"]),
                ("enum", schema["enum"]),
                ("name", parsed_args.name),
                ("title", parsed_args.title),
                ("type", schema["type"]),
            )

            table = (
                column_headers,
                (
                    columns
                ),
            )
            return table


# +-------------+----------------------------------------------------------+
# | Property    | Value                                                    |
# +-------------+----------------------------------------------------------+
# | description | test property                                            |
# | enum        | ["xen", "qemu", "kvm", "lxc", "uml", "vmware", "hyperv"] |
# | name        | property-create                                          |
# | title       | property-title                                           |
# | type        | string                                                   |
# +-------------+----------------------------------------------------------+