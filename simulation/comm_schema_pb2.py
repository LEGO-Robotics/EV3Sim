# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simulation/comm_schema.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simulation/comm_schema.proto',
  package='serverComm',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1csimulation/comm_schema.proto\x12\nserverComm\" \n\x0cRobotRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\"=\n\tRobotData\x12\x0c\n\x04tick\x18\x01 \x01(\x05\x12\x11\n\ttick_rate\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"E\n\nRobotWrite\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x16\n\x0e\x61ttribute_path\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x1d\n\x0bWriteResult\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\xa1\x01\n\x10SimulationDealer\x12I\n\x12RequestTickUpdates\x12\x18.serverComm.RobotRequest\x1a\x15.serverComm.RobotData\"\x00\x30\x01\x12\x42\n\rSendWriteInfo\x12\x16.serverComm.RobotWrite\x1a\x17.serverComm.WriteResult\"\x00\x62\x06proto3'
)




_ROBOTREQUEST = _descriptor.Descriptor(
  name='RobotRequest',
  full_name='serverComm.RobotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.RobotRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=76,
)


_ROBOTDATA = _descriptor.Descriptor(
  name='RobotData',
  full_name='serverComm.RobotData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tick', full_name='serverComm.RobotData.tick', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tick_rate', full_name='serverComm.RobotData.tick_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='serverComm.RobotData.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=139,
)


_ROBOTWRITE = _descriptor.Descriptor(
  name='RobotWrite',
  full_name='serverComm.RobotWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.RobotWrite.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_path', full_name='serverComm.RobotWrite.attribute_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='serverComm.RobotWrite.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=210,
)


_WRITERESULT = _descriptor.Descriptor(
  name='WriteResult',
  full_name='serverComm.WriteResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.WriteResult.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=241,
)

DESCRIPTOR.message_types_by_name['RobotRequest'] = _ROBOTREQUEST
DESCRIPTOR.message_types_by_name['RobotData'] = _ROBOTDATA
DESCRIPTOR.message_types_by_name['RobotWrite'] = _ROBOTWRITE
DESCRIPTOR.message_types_by_name['WriteResult'] = _WRITERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RobotRequest = _reflection.GeneratedProtocolMessageType('RobotRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTREQUEST,
  '__module__' : 'simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RobotRequest)
  })
_sym_db.RegisterMessage(RobotRequest)

RobotData = _reflection.GeneratedProtocolMessageType('RobotData', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTDATA,
  '__module__' : 'simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RobotData)
  })
_sym_db.RegisterMessage(RobotData)

RobotWrite = _reflection.GeneratedProtocolMessageType('RobotWrite', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTWRITE,
  '__module__' : 'simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RobotWrite)
  })
_sym_db.RegisterMessage(RobotWrite)

WriteResult = _reflection.GeneratedProtocolMessageType('WriteResult', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESULT,
  '__module__' : 'simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.WriteResult)
  })
_sym_db.RegisterMessage(WriteResult)



_SIMULATIONDEALER = _descriptor.ServiceDescriptor(
  name='SimulationDealer',
  full_name='serverComm.SimulationDealer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=244,
  serialized_end=405,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestTickUpdates',
    full_name='serverComm.SimulationDealer.RequestTickUpdates',
    index=0,
    containing_service=None,
    input_type=_ROBOTREQUEST,
    output_type=_ROBOTDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendWriteInfo',
    full_name='serverComm.SimulationDealer.SendWriteInfo',
    index=1,
    containing_service=None,
    input_type=_ROBOTWRITE,
    output_type=_WRITERESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMULATIONDEALER)

DESCRIPTOR.services_by_name['SimulationDealer'] = _SIMULATIONDEALER

# @@protoc_insertion_point(module_scope)
