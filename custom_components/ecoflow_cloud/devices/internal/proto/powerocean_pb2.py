# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: powerocean.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10powerocean.proto\"\x9d\x0e\n\x0fHeartbeatReport\x12\x15\n\rbpRemainWatth\x18\x01 \x01(\x02\x12\x11\n\tbpDsgTime\x18\x02 \x01(\r\x12\x16\n\x0erateCtrlSwtich\x18\x03 \x01(\x08\x12\x17\n\x0fsysRateCtrlTime\x18\x04 \x01(\r\x12\x10\n\x08\x64uraTime\x18\x05 \x01(\r\x12\x11\n\tpcsActPwr\x18\n \x01(\x02\x12\x11\n\tpcsAcFreq\x18\x0b \x01(\x02\x12\x12\n\npcsBusVolt\x18\x10 \x01(\x02\x12\x12\n\npcsLeakAmp\x18\x11 \x01(\x02\x12\x0e\n\x06pcsDci\x18\x12 \x01(\x02\x12\x0e\n\x06pcsDcv\x18\x13 \x01(\x02\x12\x12\n\npcsVbusRef\x18  \x01(\x02\x12\x19\n\x11pcsActivePowerRef\x18! \x01(\x02\x12\x1d\n\x15pcsActivePowerLimitUp\x18\" \x01(\x02\x12\x1d\n\x15pcsActivePowerLimitDn\x18# \x01(\x02\x12\x12\n\npcsBpPower\x18$ \x01(\x02\x12\x1a\n\x12pcsBpPowerChgLimit\x18% \x01(\x02\x12\x19\n\x11pcsRelayStateShow\x18& \x01(\x02\x12\x1f\n\x17pcsGridSafetyFuncRecord\x18\' \x01(\x02\x12 \n\x18pcsGridSafetyStateRecord\x18( \x01(\x02\x12\x1a\n\x12pcsGridInvErrorRms\x18) \x01(\x02\x12\x15\n\rpcsPfcCurReal\x18* \x01(\x02\x12\x14\n\x0cpcsPfcCurRef\x18+ \x01(\x02\x12\x1b\n\x13pcsReactivePowerRef\x18, \x01(\x02\x12\x15\n\rpcsMeterPower\x18- \x01(\x02\x12\x1d\n\x15pcsCommInterfaceState\x18. \x01(\x02\x12\x19\n\x11pcsAverageVoltage\x18/ \x01(\x02\x12\x13\n\x0bpcsVgridThd\x18\x30 \x01(\x02\x12!\n\x19pcsInterruptOccupancyRate\x18\x31 \x01(\x02\x12\x1d\n\x15\x65msMpptSelfcheckState\x18\x32 \x01(\x02\x12\x1b\n\x13\x65msMpptStartupState\x18\x33 \x01(\r\x12\x1b\n\x13\x65msBpSelfcheckState\x18\x34 \x01(\r\x12\x19\n\x11\x65msBpStartupState\x18\x35 \x01(\r\x12\x1c\n\x14\x65msPcsSelfcheckState\x18\x36 \x01(\r\x12\x1a\n\x12\x65msPcsStartupState\x18\x37 \x01(\r\x12\x12\n\nemsBusVolt\x18\x38 \x01(\x02\x12\x1b\n\x13\x65msActiveOffGridCmd\x18\x39 \x01(\r\x12\x15\n\remsBpAliveNum\x18: \x01(\r\x12\x12\n\nemsBpPower\x18; \x01(\x02\x12\x10\n\x08\x65msBpChg\x18< \x01(\x02\x12\x10\n\x08\x65msBpDsg\x18= \x01(\x02\x12\x17\n\x0f\x65msBpChgRequest\x18> \x01(\r\x12\x16\n\x0e\x65msSelfUsedCnt\x18? \x01(\r\x12\x1d\n\x15\x65msAcMakeupTriggleSoc\x18@ \x01(\r\x12\x1a\n\x12\x65msAcMakeupExitSoc\x18\x41 \x01(\r\x12\x19\n\x11\x65msAcMakeupMinSoc\x18\x42 \x01(\r\x12\x16\n\x0e\x65msAcMakeupCnt\x18\x43 \x01(\r\x12\x18\n\x10\x65msStartFsmState\x18\x44 \x01(\r\x12\x17\n\x0f\x65msMpptRunState\x18\x45 \x01(\r\x12\x16\n\x0e\x65msMpptModStat\x18\x46 \x01(\r\x12\x12\n\nemsStopCmd\x18G \x01(\r\x12\x11\n\temsSysCfg\x18H \x01(\r\x12\x12\n\nemsLpState\x18I \x01(\r\x12\x11\n\temsLpType\x18J \x01(\r\x12\x14\n\x0c\x65msLpMpptCnt\x18K \x01(\r\x12\x12\n\nemsLpBpCnt\x18L \x01(\r\x12\x16\n\x0e\x65msLpStateFlag\x18M \x01(\r\x12\x18\n\x10\x65msSocCalibState\x18N \x01(\r\x12\x1a\n\x12\x65msSocCalibRequest\x18O \x01(\r\x12\x16\n\x0e\x65msMpptHbState\x18P \x01(\r\x12\x15\n\remsNtcTempMax\x18Q \x01(\x02\x12\x1f\n\x17\x65msBusVoltErrSlidFilter\x18R \x01(\x02\x12\x18\n\x10\x65msBusVoltRipple\x18S \x01(\x02\x12\x13\n\x0b\x65msPvInvPwr\x18T \x01(\x02\x12\x15\n\rmpptBusVolRef\x18\x64 \x01(\x02\x12\x15\n\rdcdcBusVolRef\x18\x65 \x01(\x02\x12\x11\n\tdcdcBpVol\x18\x66 \x01(\x02\x12\x1a\n\x12\x64\x63\x64\x63InductanceCurr\x18g \x01(\x02\x12\x18\n\x10innerTemperature\x18h \x01(\x02\x12\x16\n\x0epowerLimitMode\x18i \x01(\r\x12\x15\n\rinvRatedPower\x18j \x01(\r\x12\x17\n\x0f\x64\x63\x64\x63StateRecord\x18k \x01(\r\x12\x13\n\x0b\x65msWorkMode\x18l \x01(\r\x12\x14\n\x0cpcsBackupPwr\x18m \x01(\x02\"\xfe\x01\n\x11\x42pHeartbeatReport\x12\x0f\n\x07\x62ytes_1\x18\x01 \x03(\x05\x12\r\n\x05int_2\x18\x02 \x01(\x05\x12\r\n\x05int_3\x18\x03 \x01(\x05\x12\r\n\x05int_4\x18\x04 \x01(\x05\x12\r\n\x05int_5\x18\x05 \x01(\x05\x12\r\n\x05int_6\x18\x06 \x01(\x05\x12\r\n\x05int_7\x18\x07 \x01(\x05\x12\r\n\x05int_8\x18\x08 \x01(\x05\x12\r\n\x05int_9\x18\t \x01(\x05\x12\x0e\n\x06int_10\x18\n \x01(\x05\x12\x0e\n\x06int_14\x18\x0b \x01(\x05\x12\x0e\n\x06int_15\x18\x0c \x01(\x05\x12\x0e\n\x06int_16\x18\r \x01(\x05\x12\x0e\n\x06int_17\x18\x0e \x01(\x05\x12\x10\n\x08moduleSn\x18\x0f \x01(\t\"\xe0\x34\n\x0c\x43hangeReport\x12\x12\n\nsysWorkSta\x18\x01 \x01(\r\x12\x12\n\nsysGridSta\x18\x02 \x01(\r\x12\x13\n\x0b\x65msWordMode\x18\x03 \x01(\x05\x12\x16\n\x0e\x65msBackupEvent\x18\x04 \x01(\r\x12\x13\n\x0b\x62pChgDsgSta\x18\x05 \x01(\r\x12\x12\n\nemsKeepSoc\x18\x06 \x01(\r\x12\r\n\x05\x62pSoc\x18\x07 \x01(\r\x12\x1b\n\x13\x65msSysSelfCheckStat\x18\x08 \x01(\r\x12\x13\n\x0b\x62pOnlineSum\x18\t \x01(\r\x12\x1b\n\x13sysOnOffMachineStat\x18\n \x01(\r\x12\x18\n\x10sysBatChgUpLimit\x18\x0b \x01(\r\x12\x1a\n\x12sysBatDsgDownLimit\x18\x0c \x01(\r\x12\x18\n\x10\x62pTotalChgEnergy\x18\r \x01(\r\x12\x18\n\x10\x62pTotalDsgEnergy\x18\x0e \x01(\r\x12\x19\n\x11sysBatBackupRatio\x18\x0f \x01(\r\x12\x13\n\x0b\x65msFeedMode\x18\x10 \x01(\r\x12\x14\n\x0c\x65msFeedRatio\x18\x11 \x01(\r\x12\x12\n\nemsFeedPwr\x18\x12 \x01(\r\x12\x13\n\x0bsysMeterCfg\x18\x13 \x01(\r\x12\x12\n\nsysTypeCfg\x18\x14 \x01(\r\x12\x11\n\tpcsRunSta\x18\x15 \x01(\x05\x12\x14\n\x0cpcsAcErrCode\x18\x16 \x01(\r\x12\x14\n\x0cpcsDcErrCode\x18\x17 \x01(\r\x12\x13\n\x0bpcsOverVol1\x18\x1f \x01(\x02\x12\x13\n\x0bpcsOverVol2\x18  \x01(\x02\x12\x13\n\x0bpcsOverVol3\x18! \x01(\x02\x12\x17\n\x0fpcsOverVolTime1\x18\" \x01(\r\x12\x17\n\x0fpcsOverVolTime2\x18# \x01(\r\x12\x17\n\x0fpcsOverVolTime3\x18$ \x01(\r\x12\x12\n\npcsLowVol1\x18% \x01(\x02\x12\x12\n\npcsLowVol2\x18& \x01(\x02\x12\x12\n\npcsLowVol3\x18\' \x01(\x02\x12\x16\n\x0epcsLowVolTime1\x18( \x01(\r\x12\x16\n\x0epcsLowVolTime2\x18) \x01(\r\x12\x16\n\x0epcsLowVolTime3\x18* \x01(\r\x12\x19\n\x11pcsOverVolRecover\x18+ \x01(\x02\x12\x18\n\x10pcsLowVolRecover\x18, \x01(\x02\x12\x19\n\x11pcsVolRecoverTime\x18- \x01(\r\x12\x18\n\x10pcs_10minOverVol\x18. \x01(\x02\x12\x1c\n\x14pcs_10minOverVolTime\x18/ \x01(\r\x12\x14\n\x0cpcsOverFreq1\x18\x30 \x01(\x02\x12\x14\n\x0cpcsOverFreq2\x18\x31 \x01(\x02\x12\x18\n\x10pcsOverFreqTime1\x18\x32 \x01(\r\x12\x18\n\x10pcsOverFreqTime2\x18\x33 \x01(\r\x12\x13\n\x0bpcsLowFreq1\x18\x34 \x01(\x02\x12\x13\n\x0bpcsLowFreq2\x18\x35 \x01(\x02\x12\x17\n\x0fpcsLowFreqTime1\x18\x36 \x01(\r\x12\x17\n\x0fpcsLowFreqTime2\x18\x37 \x01(\r\x12\x1a\n\x12pcsOverFreqRecover\x18\x38 \x01(\x02\x12\x19\n\x11pcsLowFreqRecover\x18\x39 \x01(\x02\x12\x1a\n\x12pcsFreqRecoverTime\x18: \x01(\r\x12\x19\n\x11pcsHvrtLvrtSwitch\x18; \x01(\r\x12#\n\x1bpcsOverVolRideThroughStart1\x18< \x01(\x02\x12#\n\x1bpcsOverVolRideThroughStart2\x18= \x01(\x02\x12)\n!pcsOverVolRideThroughProtectTime1\x18> \x01(\r\x12)\n!pcsOverVolRideThroughProtectTime2\x18? \x01(\r\x12\"\n\x1apcsLowVolRideThroughStart1\x18@ \x01(\x02\x12\"\n\x1apcsLowVolRideThroughStart2\x18\x41 \x01(\x02\x12\"\n\x1apcsLowVolRideThroughStart3\x18\x42 \x01(\x02\x12(\n pcsLowVolRideThroughProtectTime1\x18\x43 \x01(\r\x12(\n pcsLowVolRideThroughProtectTime2\x18\x44 \x01(\r\x12(\n pcsLowVolRideThroughProtectTime3\x18\x45 \x01(\r\x12$\n\x1cpcsHighVolRideThroughRecover\x18\x46 \x01(\x02\x12#\n\x1bpcsLowVolRideThroughRecover\x18G \x01(\x02\x12\x1d\n\x15pcsIslandDetectSwitch\x18H \x01(\r\x12$\n\x1cpcsActivePowerDeratingSwitch\x18I \x01(\r\x12%\n\x1dpcsActivePowerDeratingPercent\x18J \x01(\x02\x12\x1e\n\x16pcsActivePowerGradient\x18K \x01(\x02\x12%\n\x1dpcsActivePowerSoftstartSwitch\x18L \x01(\r\x12#\n\x1bpcsActivePowerSoftstartTime\x18M \x01(\r\x12!\n\x19pcsOverFreqDeratingSwitch\x18N \x01(\r\x12%\n\x1dpcsOverFreqDeratingPowerBased\x18O \x01(\x02\x12 \n\x18pcsOverFreqDeratingStart\x18P \x01(\x02\x12\x1e\n\x16pcsOverFreqDeratingEnd\x18Q \x01(\x02\x12 \n\x18pcsOverFreqDeratingSlope\x18R \x01(\x02\x12\'\n\x1fpcsOverFreqDeratingRecoverSlope\x18S \x01(\x02\x12&\n\x1epcsOverFreqDeratingFrozeSwitch\x18T \x01(\r\x12&\n\x1epcsOverFreqDeratingCutoffPower\x18U \x01(\x02\x12#\n\x1bpcsUnderFreqIncrementSwitch\x18V \x01(\r\x12\"\n\x1apcsUnderFreqIncrementStart\x18W \x01(\x02\x12 \n\x18pcsUnderFreqIncrementEnd\x18X \x01(\x02\x12\"\n\x1apcsUnderFreqIncrementSlope\x18Y \x01(\x02\x12)\n!pcsUnderFreqIncrementRecoverSlope\x18Z \x01(\x02\x12(\n pcsUnderFreqIncrementFrozeSwitch\x18[ \x01(\r\x12\x1d\n\x15pcsAntiBackFlowSwitch\x18\\ \x01(\r\x12 \n\x18pcsOverVolDeratingSwitch\x18] \x01(\r\x12\x1f\n\x17pcsOverVolDeratingStart\x18^ \x01(\x02\x12\x1d\n\x15pcsOverVolDeratingEnd\x18_ \x01(\x02\x12\'\n\x1fpcsOverVolDeratingStartingPower\x18` \x01(\x02\x12\"\n\x1apcsOverVolDeratingEndPower\x18\x61 \x01(\x02\x12#\n\x1bpcsOverVolDeratingTimeConst\x18\x62 \x01(\x02\x12\x1d\n\x15pcsReactPwrModeSelect\x18\x63 \x01(\r\x12\x1f\n\x17pcsReactPwrCompensation\x18\x64 \x01(\x02\x12\x12\n\npcsPfValue\x18\x65 \x01(\x02\x12\x1a\n\x12pcsReactPwrPercent\x18\x66 \x01(\x02\x12\x0f\n\x07pcsQuV1\x18g \x01(\x02\x12\x0f\n\x07pcsQuV2\x18h \x01(\x02\x12\x0f\n\x07pcsQuV3\x18i \x01(\x02\x12\x0f\n\x07pcsQuV4\x18j \x01(\x02\x12\x0f\n\x07pcsQuQ1\x18k \x01(\x02\x12\x0f\n\x07pcsQuQ2\x18l \x01(\x02\x12\x0f\n\x07pcsQuQ3\x18m \x01(\x02\x12\x0f\n\x07pcsQuQ4\x18n \x01(\x02\x12\x16\n\x0epcsQuTimeConst\x18o \x01(\x02\x12\x11\n\tpcsCospP1\x18p \x01(\x02\x12\x11\n\tpcsCospP2\x18q \x01(\x02\x12\x11\n\tpcsCospP3\x18r \x01(\x02\x12\x12\n\npcsCospPf1\x18s \x01(\x02\x12\x12\n\npcsCospPf2\x18t \x01(\x02\x12\x12\n\npcsCospPf3\x18u \x01(\x02\x12%\n\x1dpcsSafetyCountryCodeSelection\x18v \x01(\r\x12$\n\x1cpcsReconnectGridDetectSwitch\x18w \x01(\r\x12\x19\n\x11pcsOnGridWaitTime\x18x \x01(\r\x12\x18\n\x10pcsHighVolOnGrid\x18y \x01(\x02\x12\x17\n\x0fpcsLowVolOnGrid\x18z \x01(\x02\x12\x19\n\x11pcsHighFreqOnGrid\x18{ \x01(\x02\x12\x18\n\x10pcsLowFreqOnGrid\x18| \x01(\x02\x12%\n\x1dpcsFaultRecoverOnGridWaitTime\x18} \x01(\r\x12$\n\x1cpcsFaultRecoverHighVolOnGrid\x18~ \x01(\x02\x12#\n\x1bpcsFaultRecoverLowVolOnGrid\x18\x7f \x01(\x02\x12&\n\x1dpcsFaultRecoverHighFreqOnGrid\x18\x80\x01 \x01(\x02\x12%\n\x1cpcsFaultRecoverLowFreqOnGrid\x18\x81\x01 \x01(\x02\x12\x1d\n\x14pcsPowerDeratingFlag\x18\x82\x01 \x01(\r\x12\x1c\n\x13pcsPowerDeratingSet\x18\x83\x01 \x01(\r\x12\x13\n\npcsSendEnd\x18\x84\x01 \x01(\r\x12\x17\n\x0erateCtrlSwtich\x18\x85\x01 \x01(\x08\x12\x18\n\x0fsysRateCtrlTime\x18\x86\x01 \x01(\r\x12\x11\n\x08\x64uraTime\x18\x87\x01 \x01(\r\x12\x1f\n\x16pcs_10minOverVolSwitch\x18\x88\x01 \x01(\r\x12$\n\x1bpcsActivePowerSoftStartRate\x18\x89\x01 \x01(\x02\x12\'\n\x1epcsActivePowerNormalRampUpRate\x18\x8a\x01 \x01(\x02\x12&\n\x1dpcsOverFreqDeratingStartDelay\x18\x8b\x01 \x01(\x02\x12$\n\x1bpcsOverFreqDeratingEndDelay\x18\x8c\x01 \x01(\x02\x12.\n%pcsOverFreqDeratingRecoverSlopeSwitch\x18\x8d\x01 \x01(\r\x12(\n\x1fpcsUnderFreqIncrementStartDelay\x18\x8e\x01 \x01(\x02\x12&\n\x1dpcsUnderFreqIncrementEndDelay\x18\x8f\x01 \x01(\x02\x12$\n\x1bpcsOverVolDeratingDelayTime\x18\x90\x01 \x01(\r\x12\x1f\n\x16pcsOngridReconnectFlag\x18\x91\x01 \x01(\r\x12\x19\n\x10pcsQuLockinPower\x18\x92\x01 \x01(\x02\x12\x1a\n\x11pcsQuLockoutPower\x18\x93\x01 \x01(\x02\x12\x1b\n\x12pcsQuMinimumCosphi\x18\x94\x01 \x01(\x02\x12\x15\n\x0cpcsFastCheck\x18\x95\x01 \x01(\r\x12\x1a\n\x11pcsFunctionEnable\x18\x96\x01 \x01(\r\x12\x17\n\x0e\x65msCtrlLedType\x18\x97\x01 \x01(\r\x12\x19\n\x10\x65msCtrlLedBright\x18\x98\x01 \x01(\r\x12\x30\n\'pcsUnderFreqIncrementRecoverSlopeSwitch\x18\x99\x01 \x01(\r\x12$\n\x1bpcsOverVolDeratingDaleyTime\x18\x9a\x01 \x01(\x02\x12\x12\n\tpcsCospP4\x18\x9b\x01 \x01(\x02\x12\x13\n\npcsCospPf4\x18\x9c\x01 \x01(\x02\x12\x15\n\x0cpcsReserved1\x18\x9d\x01 \x01(\r\x12\x15\n\x0cpcsReserved2\x18\x9e\x01 \x01(\r\x12\x15\n\x0cpcsReserved3\x18\x9f\x01 \x01(\r\x12\x15\n\x0cpcsReserved4\x18\xa0\x01 \x01(\r\x12\x15\n\x0cpcsReserved5\x18\xa1\x01 \x01(\r\x12\x15\n\x0cpcsReserved6\x18\xa2\x01 \x01(\r\x12\x15\n\x0cpcsReserved7\x18\xa3\x01 \x01(\x02\x12\x15\n\x0cpcsReserved8\x18\xa4\x01 \x01(\x02\x12\x15\n\x0cpcsReserved9\x18\xa5\x01 \x01(\x02\x12\x16\n\rpcsReserved10\x18\xa6\x01 \x01(\x02\x12\x16\n\rpcsReserved11\x18\xa7\x01 \x01(\x02\x12\x16\n\rpcsReserved12\x18\xa8\x01 \x01(\x02\x12\x16\n\rpcsReserved13\x18\xa9\x01 \x01(\x02\x12\x16\n\rpcsReserved14\x18\xaa\x01 \x01(\x02\x12\x16\n\rpcsReserved15\x18\xab\x01 \x01(\x02\x12\x16\n\rpcsReserved16\x18\xac\x01 \x01(\x02\x12\x19\n\x10sysMulPeakSwitch\x18\xb4\x01 \x01(\x08\x12\x17\n\x0esysMulPeakTime\x18\xb5\x01 \x01(\r\x12\x15\n\x0c\x65msSgReadyEn\x18\xb7\x01 \x01(\x08\x12\x15\n\x0c\x65msSgRunStat\x18\xb8\x01 \x01(\r\x12\x13\n\nemsStopAll\x18\xb9\x01 \x01(\r\x12\x11\n\x08iot_4gOn\x18\xba\x01 \x01(\x11\x12\x12\n\tiot_4gSta\x18\xbb\x01 \x01(\x11\x12\x12\n\tiot_4gPdp\x18\xbc\x01 \x01(\x11\x12\x12\n\tiot_4gErr\x18\xbd\x01 \x01(\x11\x12\x14\n\x0bsysHeatStat\x18\xbe\x01 \x01(\r\x12\x19\n\x10pcsAcWarningCode\x18\xbf\x01 \x01(\r\x12\x1d\n\x14pcsRelaySelfCheckSta\x18\xc0\x01 \x01(\r\x12\x17\n\x0epcsRunFsmState\x18\xc1\x01 \x01(\r\x12\x17\n\x0emppt1FaultCode\x18\xc2\x01 \x01(\r\x12\x17\n\x0emppt2FaultCode\x18\xc3\x01 \x01(\r\x12\x19\n\x10mppt1WarningCode\x18\xc4\x01 \x01(\r\x12\x19\n\x10mppt2WarningCode\x18\xc5\x01 \x01(\r\x12\x16\n\rbpLineOffFlag\x18\xc6\x01 \x01(\r\x12\x16\n\rbpRestartFlag\x18\xc7\x01 \x01(\r\x12\x16\n\rbpReverseFlag\x18\xc8\x01 \x01(\r\x12\x1e\n\x15\x62\x61tRelayCloseFailFlag\x18\xc9\x01 \x01(\r\x12\x1b\n\x12\x62\x61tSoftRelayStatus\x18\xca\x01 \x01(\r\x12\x17\n\x0e\x62\x61tRealyStatus\x18\xcb\x01 \x01(\r\x12\x1a\n\x11pcsRelayStateShow\x18\xcc\x01 \x01(\r\x12\x15\n\x0c\x65msWorkState\x18\xcd\x01 \x01(\r\x12\x18\n\x0f\x61\x66\x63iFaultCntCh1\x18\xcf\x01 \x01(\r\x12\x1a\n\x11\x61\x66\x63iFaultValueCh1\x18\xd0\x01 \x01(\x02\x12\x1d\n\x14\x61\x66\x63iFaultMaxValueCh1\x18\xd1\x01 \x01(\x02\x12\x1c\n\x13\x61\x66\x63iProtectValueCh1\x18\xd2\x01 \x01(\x02\x12\x19\n\x10\x61\x66\x63iFaultFlagCh1\x18\xd3\x01 \x01(\r\x12\x18\n\x0f\x61\x66\x63iFaultCntCh2\x18\xd4\x01 \x01(\r\x12\x1a\n\x11\x61\x66\x63iFaultValueCh2\x18\xd5\x01 \x01(\x02\x12\x1d\n\x14\x61\x66\x63iFaultMaxValueCh2\x18\xd6\x01 \x01(\x02\x12\x1c\n\x13\x61\x66\x63iProtectValueCh2\x18\xd7\x01 \x01(\x02\x12\x19\n\x10\x61\x66\x63iFaultFlagCh2\x18\xd8\x01 \x01(\r\x12\x1d\n\x14\x61\x66\x63iSelfTestCmdState\x18\xd9\x01 \x01(\r\x12\x1b\n\x12\x61\x66\x63iEnableCmdState\x18\xda\x01 \x01(\r\x12\x1c\n\x13\x61\x66\x63iFaultClearState\x18\xdb\x01 \x01(\r\x12\x1c\n\x13\x61\x66\x63iSellfTestResult\x18\xdc\x01 \x01(\r\x12\x1a\n\x11\x61\x66\x63iSwitchFreqCh1\x18\xdd\x01 \x01(\r\x12\x1a\n\x11\x61\x66\x63iSwitchFreqCh2\x18\xde\x01 \x01(\r\x12\x13\n\nsysCalStat\x18\xdf\x01 \x01(\r\x12\x13\n\nethWanStat\x18\xe0\x01 \x01(\r\x12\x14\n\x0bwifiStaStat\x18\xe1\x01 \x01(\r\x12\x19\n\x10wireless_4gIccid\x18\xe2\x01 \x01(\t\x12\x1b\n\x12virtualHardEdition\x18\xe3\x01 \x01(\r\x12\x11\n\x08userRole\x18\xe4\x01 \x01(\r\x12\x13\n\nchgDsgMode\x18\xe5\x01 \x01(\r\x12\x12\n\tchgDsgPwr\x18\xe6\x01 \x01(\x02\x12\x1b\n\x12parallelAllowState\x18\xe7\x01 \x01(\x08\x12\x18\n\x0fparallelTypeSet\x18\xe8\x01 \x01(\r\x12\x15\n\x0cparallelType\x18\xe9\x01 \x01(\r\x12\x14\n\x0b\x61\x66\x63iIsExist\x18\xea\x01 \x01(\r\x12\x0f\n\x06\x61\x66\x63iEn\x18\xeb\x01 \x01(\r\x12\x12\n\tafciEnSet\x18\xec\x01 \x01(\r\x12\x18\n\x0fparallelTypeCur\x18\xed\x01 \x01(\r\x12(\n\x1fpcsPcsAntiBackFlowProtectSwitch\x18\xee\x01 \x01(\r\x12*\n!pcsAntiBackFlowExportCurrentLimit\x18\xef\x01 \x01(\x02\x12*\n!pcsAntiBackFlowImportCurrentLimit\x18\xf0\x01 \x01(\x02\x12\x1c\n\x13pcsFreqLocalCommand\x18\xf1\x01 \x01(\r\x12\x1e\n\x15pcsFreqExternalSignal\x18\xf2\x01 \x01(\r\x12\x19\n\x10pcsAutoTestState\x18\xf3\x01 \x01(\r\x12\x18\n\x0fpcsAutoTestFlag\x18\xf4\x01 \x01(\r\x12\x1c\n\x13pcsAvgOvpProtectCnt\x18\xf5\x01 \x01(\r\x12\x19\n\x10pcsOvpProtectCnt\x18\xf6\x01 \x01(\r\x12\x1a\n\x11pcsUvp1ProtectCnt\x18\xf7\x01 \x01(\r\x12\x1a\n\x11pcsUvp2ProtectCnt\x18\xf8\x01 \x01(\r\x12\x19\n\x10pcsOfpProtectCnt\x18\xf9\x01 \x01(\r\x12\x19\n\x10pcsUfpProtectCnt\x18\xfa\x01 \x01(\r\x12\x1e\n\x15pcsAvgOvpProtectValue\x18\xfb\x01 \x01(\x02\x12\x1b\n\x12pcsOvpProtectValue\x18\xfc\x01 \x01(\x02\x12\x1c\n\x13pcsUvp1ProtectValue\x18\xfd\x01 \x01(\x02\x12\x1c\n\x13pcsUvp2ProtectValue\x18\xfe\x01 \x01(\x02\x12\x1b\n\x12pcsOfpProtectValue\x18\xff\x01 \x01(\x02\x12\x1b\n\x12pcsUfpProtectValue\x18\x80\x02 \x01(\x02\x12\x1b\n\x12pcsAutoTestPercent\x18\x81\x02 \x01(\r\"\x1c\n\x1a\x45nergyStreamReportParallelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'powerocean_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEARTBEATREPORT._serialized_start=21
  _HEARTBEATREPORT._serialized_end=1842
  _BPHEARTBEATREPORT._serialized_start=1845
  _BPHEARTBEATREPORT._serialized_end=2099
  _CHANGEREPORT._serialized_start=2102
  _CHANGEREPORT._serialized_end=8854
  _ENERGYSTREAMREPORTPARALLEL._serialized_start=8856
  _ENERGYSTREAMREPORTPARALLEL._serialized_end=8884
# @@protoc_insertion_point(module_scope)
