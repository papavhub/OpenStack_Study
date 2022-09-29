# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource
from openstack.common import metadata
from openstack.utils import urljoin
import json
import warlock
from openstack import exceptions


class Property(resource.Resource):
    resources_key = 'properties' ##
    # base_path = '/metadefs/namespaces'
    namespace_name = resource.URI('namespace_name')
    base_path = '/metadefs/namespaces/%(namespace)s/properties' % {'namespace': namespace_name.name}

    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    _store_unknown_attrs_as_properties = True

    _query_mapping = resource.QueryParameters(
        "namespace", "name", "title", "type", "additionalItems", "description", "default", "items", "operators", "enum", "maximum", "minItems", "readonly", "minimum", "maxItems", "maxLength", "uniqueItems", "pattern", "minLength"
    )

    properties = resource.Body('properties', alternate_id=True)

    def _action(self, session, action):
        """Call an action on an image ID."""
        url = urljoin(self.base_path, self.id, 'actions', action)
        return session.post(url,)

    def deactivate(self, session):
        """Deactivate an image

        Note: Only administrative users can view image locations
        for deactivated images.
        """
        self._action(session, "deactivate")

# class Property(resource.Resource):
#     resources_key = 'properties'
#
#     # capabilities
#     allow_create = True
#     allow_fetch = True
#     allow_commit = True
#     allow_delete = True
#
#     _store_unknown_attrs_as_properties = True   #####
#
#     properties = resource.Body('properties', alternate_id=True)   #####
#
#     #: An identifier (a name) for the namespace.
#     namespace_name = resource.URI('namespace_name')
#     base_path = '/metadefs/namespaces/%(namespace_name)s/properties' % {'namespace_name': namespace_name.name}   #####
#
#
#     #: The name of the property
#     name = resource.Body('name', alternate_id=True)
#     #: The property type.
#     type = resource.Body('type')
#     #: The title of the property.
#     title = resource.Body('title')
#     #: Detailed description of the property.
#     description = resource.Body('description')
#     #: A list of operator
#     operators = resource.Body('operators', type=list)
#     #: Default property description.
#     default = resource.Body('default')
#     #: Indicates whether this is a read-only property.
#     readonly = resource.Body('readonly', type=bool)
#     #: Minimum allowed numerical value.
#     minimum = resource.Body('minimum', type=int)
#     #: Maximum allowed numerical value.
#     maximum = resource.Body('maximum', type=int)
#     #: Enumerated list of property values.
#     enum = resource.Body('enum', type=list)
#     #: A regular expression ( `ECMA 262 <http://www.ecma-international.org
#     # /publications/standards/Ecma-262.htm>`_ )
#     #: that a string value must match.
#     pattern = resource.Body('pattern')
#     #: Minimum allowed string length.
#     minLength = resource.Body('minLength', type=int, minimum=0, default=0)
#     #: Maximum allowed string length.
#     maxLength = resource.Body('maxLength', type=int, minimum=0)
#     #: Schema for the items in an array.
#     items = resource.Body('items', type=dict)
#     #: Indicates whether all values in the array must be distinct.
#     uniqueItems = resource.Body('uniqueItems', type=bool, default=False)
#     #: Minimum length of an array.
#     minItems = resource.Body('minItems', type=int, minimum=0, default=0)
#     #: Maximum length of an array.
#     maxItems = resource.Body('maxItems', type=int, minimum=0)
#     #: Describes extra items, if you use tuple typing.  If the value of
#     #: ``items`` is an array (tuple typing) and the instance is longer than
#     #: the list of schemas in ``items``, the additional items are described by
#     #: the schema in this property.  If this value is ``false``, the instance
#     #: cannot be longer than the list of schemas in ``items``.  If this value
#     #: is ``true``, that is equivalent to the empty schema (anything goes).
#     additionalItems = resource.Body('additionalItems', type=bool)
