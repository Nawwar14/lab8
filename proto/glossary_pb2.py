# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: glossary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eglossary.proto\x12\x08glossary\",\n\x04Term\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x1a\n\x07Keyword\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"\x1f\n\x0cTermResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"*\n\tTermsList\x12\x1d\n\x05terms\x18\x01 \x03(\x0b\x32\x0e.glossary.Term\"\x07\n\x05\x45mpty2\x96\x02\n\x0fGlossaryService\x12\x31\n\x07\x41\x64\x64Term\x12\x0e.glossary.Term\x1a\x16.glossary.TermResponse\x12,\n\x07GetTerm\x12\x11.glossary.Keyword\x1a\x0e.glossary.Term\x12\x33\n\x0bGetAllTerms\x12\x0f.glossary.Empty\x1a\x13.glossary.TermsList\x12\x34\n\nUpdateTerm\x12\x0e.glossary.Term\x1a\x16.glossary.TermResponse\x12\x37\n\nDeleteTerm\x12\x11.glossary.Keyword\x1a\x16.glossary.TermResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glossary_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TERM']._serialized_start=28
  _globals['_TERM']._serialized_end=72
  _globals['_KEYWORD']._serialized_start=74
  _globals['_KEYWORD']._serialized_end=100
  _globals['_TERMRESPONSE']._serialized_start=102
  _globals['_TERMRESPONSE']._serialized_end=133
  _globals['_TERMSLIST']._serialized_start=135
  _globals['_TERMSLIST']._serialized_end=177
  _globals['_EMPTY']._serialized_start=179
  _globals['_EMPTY']._serialized_end=186
  _globals['_GLOSSARYSERVICE']._serialized_start=189
  _globals['_GLOSSARYSERVICE']._serialized_end=467
# @@protoc_insertion_point(module_scope)
