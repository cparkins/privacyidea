# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63\x61service.proto\"\'\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\";\n\x10SetOptionRequest\x12\x12\n\noptionName\x18\x01 \x01(\t\x12\x13\n\x0boptionValue\x18\x02 \x01(\t\")\n\x0eSetOptionReply\x12\x17\n\x06status\x18\x01 \x01(\x0b\x32\x07.Status\"\x13\n\x11GetOptionsRequest\"\x8a\x01\n\x0fGetOptionsReply\x12.\n\x07options\x18\x01 \x03(\x0b\x32\x1d.GetOptionsReply.OptionsEntry\x12\x17\n\x06status\x18\x02 \x01(\x0b\x32\x07.Status\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x10SubmitCSRRequest\x12\x0b\n\x03\x63sr\x18\x01 \x01(\t\x12\x14\n\x0ctemplateName\x18\x02 \x01(\t\x12\x0e\n\x06\x63\x61Name\x18\x03 \x01(\t\"m\n\x0eSubmitCSRReply\x12\x13\n\x0b\x64isposition\x18\x01 \x01(\x05\x12\x1a\n\x12\x64ispositionMessage\x18\x02 \x01(\t\x12\x11\n\trequestId\x18\x03 \x01(\x05\x12\x17\n\x06status\x18\x05 \x01(\x0b\x32\x07.Status\"\x0f\n\rGetCAsRequest\"7\n\x0bGetCAsReply\x12\x0f\n\x07\x63\x61Names\x18\x01 \x03(\t\x12\x17\n\x06status\x18\x02 \x01(\x0b\x32\x07.Status\"3\n\x15GetCertificateRequest\x12\x0e\n\x06\x63\x61Name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\"<\n\x13GetCertificateReply\x12\x0c\n\x04\x63\x65rt\x18\x01 \x01(\t\x12\x17\n\x06status\x18\x02 \x01(\x0b\x32\x07.Status\"%\n\x13GetTemplatesRequest\x12\x0e\n\x06\x63\x61Name\x18\x01 \x01(\t\"C\n\x11GetTemplatesReply\x12\x15\n\rtemplateNames\x18\x01 \x03(\t\x12\x17\n\x06status\x18\x02 \x01(\x0b\x32\x07.Status\"b\n\x13GetCSRStatusRequest\x12\x0e\n\x06\x63\x61Name\x18\x01 \x01(\t\x12\x17\n\rcertRequestId\x18\x02 \x01(\x05H\x00\x12\x14\n\ncertSerial\x18\x03 \x01(\tH\x00\x42\x0c\n\nIDorSerial\"]\n\x11GetCSRStatusReply\x12\x13\n\x0b\x64isposition\x18\x01 \x01(\x05\x12\x1a\n\x12\x64ispositionMessage\x18\x02 \x01(\t\x12\x17\n\x06status\x18\x03 \x01(\x0b\x32\x07.Status*\x19\n\x04\x43ode\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xfd\x02\n\tCAService\x12/\n\tSubmitCSR\x12\x11.SubmitCSRRequest\x1a\x0f.SubmitCSRReply\x12&\n\x06GetCAs\x12\x0e.GetCAsRequest\x1a\x0c.GetCAsReply\x12>\n\x0eGetCertificate\x12\x16.GetCertificateRequest\x1a\x14.GetCertificateReply\x12\x38\n\x0cGetTemplates\x12\x14.GetTemplatesRequest\x1a\x12.GetTemplatesReply\x12\x38\n\x0cGetCSRStatus\x12\x14.GetCSRStatusRequest\x1a\x12.GetCSRStatusReply\x12/\n\tSetOption\x12\x11.SetOptionRequest\x1a\x0f.SetOptionReply\x12\x32\n\nGetOptions\x12\x12.GetOptionsRequest\x1a\x10.GetOptionsReplyB\x07\xaa\x02\x04Grpcb\x06proto3')

_CODE = DESCRIPTOR.enum_types_by_name['Code']
Code = enum_type_wrapper.EnumTypeWrapper(_CODE)
OK = 0
ERROR = 1


_STATUS = DESCRIPTOR.message_types_by_name['Status']
_SETOPTIONREQUEST = DESCRIPTOR.message_types_by_name['SetOptionRequest']
_SETOPTIONREPLY = DESCRIPTOR.message_types_by_name['SetOptionReply']
_GETOPTIONSREQUEST = DESCRIPTOR.message_types_by_name['GetOptionsRequest']
_GETOPTIONSREPLY = DESCRIPTOR.message_types_by_name['GetOptionsReply']
_GETOPTIONSREPLY_OPTIONSENTRY = _GETOPTIONSREPLY.nested_types_by_name['OptionsEntry']
_SUBMITCSRREQUEST = DESCRIPTOR.message_types_by_name['SubmitCSRRequest']
_SUBMITCSRREPLY = DESCRIPTOR.message_types_by_name['SubmitCSRReply']
_GETCASREQUEST = DESCRIPTOR.message_types_by_name['GetCAsRequest']
_GETCASREPLY = DESCRIPTOR.message_types_by_name['GetCAsReply']
_GETCERTIFICATEREQUEST = DESCRIPTOR.message_types_by_name['GetCertificateRequest']
_GETCERTIFICATEREPLY = DESCRIPTOR.message_types_by_name['GetCertificateReply']
_GETTEMPLATESREQUEST = DESCRIPTOR.message_types_by_name['GetTemplatesRequest']
_GETTEMPLATESREPLY = DESCRIPTOR.message_types_by_name['GetTemplatesReply']
_GETCSRSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetCSRStatusRequest']
_GETCSRSTATUSREPLY = DESCRIPTOR.message_types_by_name['GetCSRStatusReply']
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  })
_sym_db.RegisterMessage(Status)

SetOptionRequest = _reflection.GeneratedProtocolMessageType('SetOptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETOPTIONREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:SetOptionRequest)
  })
_sym_db.RegisterMessage(SetOptionRequest)

SetOptionReply = _reflection.GeneratedProtocolMessageType('SetOptionReply', (_message.Message,), {
  'DESCRIPTOR' : _SETOPTIONREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:SetOptionReply)
  })
_sym_db.RegisterMessage(SetOptionReply)

GetOptionsRequest = _reflection.GeneratedProtocolMessageType('GetOptionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPTIONSREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetOptionsRequest)
  })
_sym_db.RegisterMessage(GetOptionsRequest)

GetOptionsReply = _reflection.GeneratedProtocolMessageType('GetOptionsReply', (_message.Message,), {

  'OptionsEntry' : _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETOPTIONSREPLY_OPTIONSENTRY,
    '__module__' : 'caservice_pb2'
    # @@protoc_insertion_point(class_scope:GetOptionsReply.OptionsEntry)
    })
  ,
  'DESCRIPTOR' : _GETOPTIONSREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetOptionsReply)
  })
_sym_db.RegisterMessage(GetOptionsReply)
_sym_db.RegisterMessage(GetOptionsReply.OptionsEntry)

SubmitCSRRequest = _reflection.GeneratedProtocolMessageType('SubmitCSRRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITCSRREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:SubmitCSRRequest)
  })
_sym_db.RegisterMessage(SubmitCSRRequest)

SubmitCSRReply = _reflection.GeneratedProtocolMessageType('SubmitCSRReply', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITCSRREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:SubmitCSRReply)
  })
_sym_db.RegisterMessage(SubmitCSRReply)

GetCAsRequest = _reflection.GeneratedProtocolMessageType('GetCAsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCASREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetCAsRequest)
  })
_sym_db.RegisterMessage(GetCAsRequest)

GetCAsReply = _reflection.GeneratedProtocolMessageType('GetCAsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETCASREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetCAsReply)
  })
_sym_db.RegisterMessage(GetCAsReply)

GetCertificateRequest = _reflection.GeneratedProtocolMessageType('GetCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCERTIFICATEREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetCertificateRequest)
  })
_sym_db.RegisterMessage(GetCertificateRequest)

GetCertificateReply = _reflection.GeneratedProtocolMessageType('GetCertificateReply', (_message.Message,), {
  'DESCRIPTOR' : _GETCERTIFICATEREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetCertificateReply)
  })
_sym_db.RegisterMessage(GetCertificateReply)

GetTemplatesRequest = _reflection.GeneratedProtocolMessageType('GetTemplatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTEMPLATESREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetTemplatesRequest)
  })
_sym_db.RegisterMessage(GetTemplatesRequest)

GetTemplatesReply = _reflection.GeneratedProtocolMessageType('GetTemplatesReply', (_message.Message,), {
  'DESCRIPTOR' : _GETTEMPLATESREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetTemplatesReply)
  })
_sym_db.RegisterMessage(GetTemplatesReply)

GetCSRStatusRequest = _reflection.GeneratedProtocolMessageType('GetCSRStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCSRSTATUSREQUEST,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetCSRStatusRequest)
  })
_sym_db.RegisterMessage(GetCSRStatusRequest)

GetCSRStatusReply = _reflection.GeneratedProtocolMessageType('GetCSRStatusReply', (_message.Message,), {
  'DESCRIPTOR' : _GETCSRSTATUSREPLY,
  '__module__' : 'caservice_pb2'
  # @@protoc_insertion_point(class_scope:GetCSRStatusReply)
  })
_sym_db.RegisterMessage(GetCSRStatusReply)

_CASERVICE = DESCRIPTOR.services_by_name['CAService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\004Grpc'
  _GETOPTIONSREPLY_OPTIONSENTRY._options = None
  _GETOPTIONSREPLY_OPTIONSENTRY._serialized_options = b'8\001'
  _CODE._serialized_start=1000
  _CODE._serialized_end=1025
  _STATUS._serialized_start=19
  _STATUS._serialized_end=58
  _SETOPTIONREQUEST._serialized_start=60
  _SETOPTIONREQUEST._serialized_end=119
  _SETOPTIONREPLY._serialized_start=121
  _SETOPTIONREPLY._serialized_end=162
  _GETOPTIONSREQUEST._serialized_start=164
  _GETOPTIONSREQUEST._serialized_end=183
  _GETOPTIONSREPLY._serialized_start=186
  _GETOPTIONSREPLY._serialized_end=324
  _GETOPTIONSREPLY_OPTIONSENTRY._serialized_start=278
  _GETOPTIONSREPLY_OPTIONSENTRY._serialized_end=324
  _SUBMITCSRREQUEST._serialized_start=326
  _SUBMITCSRREQUEST._serialized_end=395
  _SUBMITCSRREPLY._serialized_start=397
  _SUBMITCSRREPLY._serialized_end=506
  _GETCASREQUEST._serialized_start=508
  _GETCASREQUEST._serialized_end=523
  _GETCASREPLY._serialized_start=525
  _GETCASREPLY._serialized_end=580
  _GETCERTIFICATEREQUEST._serialized_start=582
  _GETCERTIFICATEREQUEST._serialized_end=633
  _GETCERTIFICATEREPLY._serialized_start=635
  _GETCERTIFICATEREPLY._serialized_end=695
  _GETTEMPLATESREQUEST._serialized_start=697
  _GETTEMPLATESREQUEST._serialized_end=734
  _GETTEMPLATESREPLY._serialized_start=736
  _GETTEMPLATESREPLY._serialized_end=803
  _GETCSRSTATUSREQUEST._serialized_start=805
  _GETCSRSTATUSREQUEST._serialized_end=903
  _GETCSRSTATUSREPLY._serialized_start=905
  _GETCSRSTATUSREPLY._serialized_end=998
  _CASERVICE._serialized_start=1028
  _CASERVICE._serialized_end=1409
# @@protoc_insertion_point(module_scope)
