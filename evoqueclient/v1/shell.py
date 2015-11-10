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
import os

from evoqueclient.common import utils
from evoqueclient.openstack.common.apiclient import exceptions


def do_ticket_list(ec, args={}):
    """List all available tickets."""
    tickets = ec.ticket.list()
    field_labels = ["ID", "Name"]
    fields = ["id", "name"]
    utils.print_list(tickets, fields, field_labels)


@utils.arg("name", metavar="<TICKET_NAME>",
           help="Ticket name.")
def do_ticket_create(ec, args):
    """Create a ticket."""
    ec.tickets.add({"name": args.name})


@utils.arg("-f", "--file-name", metavar="<FILE-NAME>",
           help="Workflow file.")
def do_workflow_create(ec, args):
    """Create a workflow."""
    if not args.file_name:
        raise exceptions.CommandError(
            "Provide --file-name <FILE-NAME> for workflow "
            "creation.")
    file_name = os.path.abspath(os.path.expanduser(args.file_name))
    ec.workflows.add({"file": file_name})
