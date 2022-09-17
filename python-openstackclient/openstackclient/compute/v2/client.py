
from openstackclient.compute.v2 import metadefs # from glanceclient.v2
from openstackclient.common import utils
from openstackclient.compute.v2 import schemas
from openstackclient.common import http


class Client(object):
    """Client for the OpenStack Images v2 API.

    :param string endpoint: A user-supplied endpoint URL for the glance service.
    :param string token: Token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    :param string language_header: Set Accept-Language header to be sent in
                                   requests to glance.
    """

    def __init__(self, endpoint=None, **kwargs):
        self.endpoint_provided = endpoint is not None
        endpoint, self.version = utils.endpoint_version_from_url(endpoint, 2.0)
        self.http_client = http.get_http_client(endpoint=endpoint, **kwargs)
        self.schemas = schemas.Controller(self.http_client)


        self.metadefs_property = (
            metadefs.PropertyController(self.http_client, self.schemas)
        )

