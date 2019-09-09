# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: push.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='push.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\npush.proto\"l\n\rSubmitRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06header\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x0c\n\x04time\x18\x06 \x01(\t\"\x1c\n\x0bSubmitReply\x12\r\n\x05reply\x18\x01 \x01(\t\"\x1e\n\x0b\x43onnRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\"Z\n\x0cMessageReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0e\n\x06header\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\t\"+\n\x0cLogInRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\nLogInReply\x12\r\n\x05reply\x18\x01 \x01(\t\"\x1e\n\x0eHistoryRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\x0cHistoryReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xcb\x01\n\x0bMessageSync\x12/\n\rSubmitMessage\x12\x0e.SubmitRequest\x1a\x0c.SubmitReply\"\x00\x12\x34\n\x11PushMessageStream\x12\x0c.ConnRequest\x1a\r.MessageReply\"\x00\x30\x01\x12%\n\x05LogIn\x12\r.LogInRequest\x1a\x0b.LogInReply\"\x00\x12.\n\nGetHistory\x12\x0f.HistoryRequest\x1a\r.HistoryReply\"\x00\x62\x06proto3')
)




_SUBMITREQUEST = _descriptor.Descriptor(
  name='SubmitRequest',
  full_name='SubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='SubmitRequest.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='SubmitRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='SubmitRequest.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='SubmitRequest.header', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='SubmitRequest.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='SubmitRequest.time', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=14,
  serialized_end=122,
)


_SUBMITREPLY = _descriptor.Descriptor(
  name='SubmitReply',
  full_name='SubmitReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='SubmitReply.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=124,
  serialized_end=152,
)


_CONNREQUEST = _descriptor.Descriptor(
  name='ConnRequest',
  full_name='ConnRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='ConnRequest.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=154,
  serialized_end=184,
)


_MESSAGEREPLY = _descriptor.Descriptor(
  name='MessageReply',
  full_name='MessageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MessageReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='MessageReply.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='MessageReply.header', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='MessageReply.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='MessageReply.time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=186,
  serialized_end=276,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LogInRequest',
  full_name='LogInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='LogInRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='LogInRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=278,
  serialized_end=321,
)


_LOGINREPLY = _descriptor.Descriptor(
  name='LogInReply',
  full_name='LogInReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='LogInReply.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=323,
  serialized_end=350,
)


_HISTORYREQUEST = _descriptor.Descriptor(
  name='HistoryRequest',
  full_name='HistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HistoryRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=352,
  serialized_end=382,
)


_HISTORYREPLY = _descriptor.Descriptor(
  name='HistoryReply',
  full_name='HistoryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='HistoryReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=384,
  serialized_end=415,
)

DESCRIPTOR.message_types_by_name['SubmitRequest'] = _SUBMITREQUEST
DESCRIPTOR.message_types_by_name['SubmitReply'] = _SUBMITREPLY
DESCRIPTOR.message_types_by_name['ConnRequest'] = _CONNREQUEST
DESCRIPTOR.message_types_by_name['MessageReply'] = _MESSAGEREPLY
DESCRIPTOR.message_types_by_name['LogInRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LogInReply'] = _LOGINREPLY
DESCRIPTOR.message_types_by_name['HistoryRequest'] = _HISTORYREQUEST
DESCRIPTOR.message_types_by_name['HistoryReply'] = _HISTORYREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREQUEST,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:SubmitRequest)
  })
_sym_db.RegisterMessage(SubmitRequest)

SubmitReply = _reflection.GeneratedProtocolMessageType('SubmitReply', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREPLY,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:SubmitReply)
  })
_sym_db.RegisterMessage(SubmitReply)

ConnRequest = _reflection.GeneratedProtocolMessageType('ConnRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNREQUEST,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:ConnRequest)
  })
_sym_db.RegisterMessage(ConnRequest)

MessageReply = _reflection.GeneratedProtocolMessageType('MessageReply', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEREPLY,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:MessageReply)
  })
_sym_db.RegisterMessage(MessageReply)

LogInRequest = _reflection.GeneratedProtocolMessageType('LogInRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:LogInRequest)
  })
_sym_db.RegisterMessage(LogInRequest)

LogInReply = _reflection.GeneratedProtocolMessageType('LogInReply', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREPLY,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:LogInReply)
  })
_sym_db.RegisterMessage(LogInReply)

HistoryRequest = _reflection.GeneratedProtocolMessageType('HistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYREQUEST,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:HistoryRequest)
  })
_sym_db.RegisterMessage(HistoryRequest)

HistoryReply = _reflection.GeneratedProtocolMessageType('HistoryReply', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYREPLY,
  '__module__' : 'push_pb2'
  # @@protoc_insertion_point(class_scope:HistoryReply)
  })
_sym_db.RegisterMessage(HistoryReply)



_MESSAGESYNC = _descriptor.ServiceDescriptor(
  name='MessageSync',
  full_name='MessageSync',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=418,
  serialized_end=621,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubmitMessage',
    full_name='MessageSync.SubmitMessage',
    index=0,
    containing_service=None,
    input_type=_SUBMITREQUEST,
    output_type=_SUBMITREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PushMessageStream',
    full_name='MessageSync.PushMessageStream',
    index=1,
    containing_service=None,
    input_type=_CONNREQUEST,
    output_type=_MESSAGEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LogIn',
    full_name='MessageSync.LogIn',
    index=2,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetHistory',
    full_name='MessageSync.GetHistory',
    index=3,
    containing_service=None,
    input_type=_HISTORYREQUEST,
    output_type=_HISTORYREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGESYNC)

DESCRIPTOR.services_by_name['MessageSync'] = _MESSAGESYNC

# @@protoc_insertion_point(module_scope)
