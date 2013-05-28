# Create your views here.

import logging

from bms.apps.tree.models import Tree
from bms.apps.lib.shortcuts import render_json_ok

logger = logging.getLogger(__name__)

def load_menu(request, parent_id):
    parent_id = int(parent_id)
    result = Tree.load_menu(parent_id)
    return render_json_ok(result)
    
    