# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: powerocean.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10powerocean.proto\"\x8b\x02\n\x1b\x45MS_CMD_ID_HEARTBEAT_REPORT\x12\x0f\n\x07\x62ytes_1\x18\x01 \x03(\x05\x12\x0f\n\x07\x63mdFunc\x18\x02 \x01(\r\x12\r\n\x05int_3\x18\x03 \x01(\x05\x12\r\n\x05int_4\x18\x04 \x01(\x05\x12\r\n\x05int_5\x18\x05 \x01(\x05\x12\r\n\x05int_6\x18\x06 \x01(\x05\x12\r\n\x05int_7\x18\x07 \x01(\x05\x12\r\n\x05int_8\x18\x08 \x01(\x05\x12\r\n\x05int_9\x18\t \x01(\x05\x12\x0e\n\x06int_10\x18\n \x01(\x05\x12\x0e\n\x06int_14\x18\x0b \x01(\x05\x12\x0e\n\x06int_15\x18\x0c \x01(\x05\x12\x0e\n\x06int_16\x18\r \x01(\x05\x12\x0e\n\x06int_17\x18\x0e \x01(\x05\x12\x11\n\tdevice_sn\x18\x18 \x01(\t\"\x9d\x02\n\x1e\x45MS_CMD_ID_BP_HEARTBEAT_REPORT\x12\x0f\n\x07\x62ytes_1\x18\x01 \x03(\x05\x12\r\n\x05int_2\x18\x02 \x01(\x05\x12\r\n\x05int_3\x18\x03 \x01(\x05\x12\r\n\x05int_4\x18\x04 \x01(\x05\x12\r\n\x05int_5\x18\x05 \x01(\x05\x12\r\n\x05int_6\x18\x06 \x01(\x05\x12\r\n\x05int_7\x18\x07 \x01(\x05\x12\r\n\x05int_8\x18\x08 \x01(\x05\x12\r\n\x05int_9\x18\t \x01(\x05\x12\x0e\n\x06int_10\x18\n \x01(\x05\x12\x0e\n\x06int_14\x18\x0b \x01(\x05\x12\x0e\n\x06int_15\x18\x0c \x01(\x05\x12\x0e\n\x06int_16\x18\r \x01(\x05\x12\x0e\n\x06int_17\x18\x0e \x01(\x05\x12\x15\n\x08moduleSn\x18\x0f \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_moduleSn\"\xa6\x06\n\x18\x45MS_CMD_ID_CHANGE_REPORT\x12\x12\n\x05pdata\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x10\n\x03src\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x11\n\x04\x64\x65st\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x11\n\x04\x64Src\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x12\n\x05\x64\x44\x65st\x18\x05 \x01(\rH\x04\x88\x01\x01\x12\x14\n\x07\x65ncType\x18\x06 \x01(\rH\x05\x88\x01\x01\x12\x16\n\tcheckType\x18\x07 \x01(\rH\x06\x88\x01\x01\x12\x14\n\x07\x63mdFunc\x18\x08 \x01(\rH\x07\x88\x01\x01\x12\x12\n\x05\x63mdId\x18\t \x01(\rH\x08\x88\x01\x01\x12\x14\n\x07\x64\x61taLen\x18\n \x01(\rH\t\x88\x01\x01\x12\x14\n\x07needAck\x18\x0b \x01(\rH\n\x88\x01\x01\x12\x12\n\x05isAck\x18\x0c \x01(\rH\x0b\x88\x01\x01\x12\x10\n\x03seq\x18\x0e \x01(\rH\x0c\x88\x01\x01\x12\x16\n\tproductId\x18\x0f \x01(\rH\r\x88\x01\x01\x12\x14\n\x07version\x18\x10 \x01(\rH\x0e\x88\x01\x01\x12\x17\n\npayloadVer\x18\x11 \x01(\rH\x0f\x88\x01\x01\x12\x15\n\x08timeSnap\x18\x12 \x01(\rH\x10\x88\x01\x01\x12\x14\n\x07isRwCmd\x18\x13 \x01(\rH\x11\x88\x01\x01\x12\x14\n\x07isQueue\x18\x14 \x01(\rH\x12\x88\x01\x01\x12\x14\n\x07\x61\x63kType\x18\x15 \x01(\rH\x13\x88\x01\x01\x12\x11\n\x04\x63ode\x18\x16 \x01(\tH\x14\x88\x01\x01\x12\x11\n\x04\x66rom\x18\x17 \x01(\tH\x15\x88\x01\x01\x12\x15\n\x08moduleSn\x18\x18 \x01(\tH\x16\x88\x01\x01\x12\x15\n\x08\x64\x65viceSn\x18\x19 \x01(\tH\x17\x88\x01\x01\x42\x08\n\x06_pdataB\x06\n\x04_srcB\x07\n\x05_destB\x07\n\x05_dSrcB\x08\n\x06_dDestB\n\n\x08_encTypeB\x0c\n\n_checkTypeB\n\n\x08_cmdFuncB\x08\n\x06_cmdIdB\n\n\x08_dataLenB\n\n\x08_needAckB\x08\n\x06_isAckB\x06\n\x04_seqB\x0c\n\n_productIdB\n\n\x08_versionB\r\n\x0b_payloadVerB\x0b\n\t_timeSnapB\n\n\x08_isRwCmdB\n\n\x08_isQueueB\n\n\x08_ackTypeB\x07\n\x05_codeB\x07\n\x05_fromB\x0b\n\t_moduleSnB\x0b\n\t_deviceSn\"*\n(EMS_CMD_ID_ENERGY_STREAM_REPORT_PARALLELb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'powerocean_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMS_CMD_ID_HEARTBEAT_REPORT']._serialized_start=21
  _globals['_EMS_CMD_ID_HEARTBEAT_REPORT']._serialized_end=288
  _globals['_EMS_CMD_ID_BP_HEARTBEAT_REPORT']._serialized_start=291
  _globals['_EMS_CMD_ID_BP_HEARTBEAT_REPORT']._serialized_end=576
  _globals['_EMS_CMD_ID_CHANGE_REPORT']._serialized_start=579
  _globals['_EMS_CMD_ID_CHANGE_REPORT']._serialized_end=1385
  _globals['_EMS_CMD_ID_ENERGY_STREAM_REPORT_PARALLEL']._serialized_start=1387
  _globals['_EMS_CMD_ID_ENERGY_STREAM_REPORT_PARALLEL']._serialized_end=1429
# @@protoc_insertion_point(module_scope)
