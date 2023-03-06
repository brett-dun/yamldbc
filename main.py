
import cantools
import sys
from typing import Dict, List
import yaml


# Lile names for input/output.
in_fname: str = sys.argv[1]
out_fname: str = sys.argv[2]

# Database object to store definitions.
db = cantools.db.Database()

with open(in_fname, encoding='utf-8') as f:
    # Load the list of message defs from the yaml file.
    data = yaml.safe_load(f)
    for msg_def in data['messages']:
        # Create Signal objects from dictionary definition.
        msg_def['signals'] = [cantools.db.Signal(
            **sig,) for sig in msg_def['signals']]
        # Create Message object from dictionary definition.
        db.messages.append(cantools.db.Message(**msg_def))

# Build the list of CAN nodes.
for msg in db.messages:
    # if msg.comment:
    #     print(msg.comment)
    if msg.senders:
        for sender in msg.senders:
            try:
                db.get_node_by_name(sender)
            except KeyError:
                print('KeyError', sender)
                db.nodes.append(cantools.db.Node(sender))
    for sig in msg.signals:
        if sig.receivers:
            for receiver in sig.receivers:
                try:
                    db.get_node_by_name(receiver)
                except KeyError:
                    db.nodes.append(cantools.db.Node(receiver))

# Dump the CAN database to the output file.
cantools.database.dump_file(db, out_fname)