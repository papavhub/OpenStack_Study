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
        # schema_client = self.app.cliennt_manager.schema
        # schema_client.get('metadefs/property')
        image_client = self.app.client_manager.image
        kwargs = {'namespace': parsed_args.namespace, "name": parsed_args.name, "title": parsed_args.title,
                  "schema": parsed_args.schema}
        metadata_object = image_client.create_metadata_property(**kwargs)
        print("metadata_object : ", metadata_object)
        # info = _format_metadata_object(metadata_object)
        # return zip(*sorted(metadata_object.items()))
        # return metadata_object

# +----------------------------------+-----------+--------------+----------------+---------+-----------+----------------------------------------------+
# | ID                               | Region    | Service Name | Service Type   | Enabled | Interface | URL                                          |
# +----------------------------------+-----------+--------------+----------------+---------+-----------+----------------------------------------------+
# | 1158c61c04bf40be8ce4d9267de0523f | RegionOne | cinder       | block-storage  | True    | public    | http://125.6.36.40/volume/v3/$(project_id)s  |
# | 3ffa4b24f84a418b85224911a4293345 | RegionOne | nova         | compute        | True    | public    | http://125.6.36.40/compute/v2.1              |
# | 7161bcba68f5498ea4150e1a93ccbe03 | RegionOne | cinderv3     | volumev3       | True    | public    | http://125.6.36.40/volume/v3/$(project_id)s  |
# | 87af9d815a0a4ba1aee30c6c4b81e3bd | RegionOne | glance       | image          | True    | public    | http://125.6.36.40/image                     |
# | a50a66a6c71a4a758748f7d81478a382 | RegionOne | placement    | placement      | True    | public    | http://125.6.36.40/placement                 |
# | aa42568cc8414d1493503b52fa275448 | RegionOne | neutron      | network        | True    | public    | http://125.6.36.40:9696/                     |
# | ad01b29f86a64643a06d44fc72c144be | RegionOne | nova_legacy  | compute_legacy | True    | public    | http://125.6.36.40/compute/v2/$(project_id)s |
# | fdaf6e90cd52458e8bb5a663cec55dbd | RegionOne | keystone     | identity       | True    | public    | http://125.6.36.40/identity                  |
# +----------------------------------+-----------+--------------+----------------+---------+-----------+----------------------------------------------+

        # compute_client = self.app.client_manager.compute
        # identity_client = self.app.client_manager.identity
        # image_client = self.app.client_manager.image
        # network_client = self.app.client_manager.network
        # compute_client = self.app.client_manager.sdk_connection.compute
        # volume_client = self.app.client_manager.sdk_connection.volume
