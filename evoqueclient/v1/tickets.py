#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from evoqueclient.common import base


class Ticket(base.Resource):
    def __repr__(self):
        return "<Ticket %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class TicketManager(base.Manager):
    resource_class = Ticket

    def list(self, **kwargs):
        """Get tickets list with pagination support."""

        url = '/v1/ticket'
        return self._list(url, response_key='tickets')

    def add(self, data):
        return self._create('/v1/ticket', data)
