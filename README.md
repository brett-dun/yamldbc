# yamldbc
Create .dbc files (CAN Bus Databases) from human-readable .yaml definitions.

Install Requirements: `pip install -r requirements.txt`
(Note: Currently cantools==38 is required due to breaking changes in 39.0.0)

Usage: `python main.py bus.yaml bus.dbc`

## yaml Structure

`bus` (List): Names of the CAN bus(es).

`nodes` (List): Names of the node(s) on the network.

`messages` (List): List of CAN bus message definitions.

### Messages

`frame_id` (int): CAN bus arbitration ID. A bus may not have multiple messages with the same arbitration ID. The lower the value, the higher the priority.

`name` (str): Name of the message.

`length` (int): Length of the message in *bytes*.

`signals` (List): Definition of signals(s) that are in this message. See [Signals](#signals) below for documentation on defining signals.

`senders` (List): Name(s) of the nodes that send this message.

`cycle_time` (int): The period in milliseconds that this message is sent.

`bus_name` (str): Name of the CAN bus that this message is sent on.

## Signals

`name` (str): Name of the signal.

`start` (int): Starting postion, in *bits*, of the signal.

`length` (int): Length of the signal in *bits*.

`is_signed` Optional(bool): Whether or not the value is signed (for integers).

`scale` Optional(float): How to scale the value.

`unit` Optional(str): Units associated with the signal value.

`is_float` Optional(bool): Wether or not the signal's value is a float.
