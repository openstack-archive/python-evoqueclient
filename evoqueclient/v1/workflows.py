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
from evoqueclient.common import exceptions

from oslo_serialization import jsonutils


class Workflow(base.Resource):
    def __repr__(self):
        return "<Workflow %s>" % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class WorkflowManager(base.Manager):
    resource_class = Workflow

    def add(self, data):
        file_name = data.get('file')
        return self._create('/v1/workflow', {
                "data": open(file_name).read(),
            })
