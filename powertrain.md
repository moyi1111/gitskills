BO_ 512 Diag_Request: 8 Vector__XXX

BO_ 1024 Diag_Response: 8 Vector__XXX

BO_ 103 Ignition_Info: 2 Gateway
 SG_ StarterKey : 0|1@1+ (1,0) [0|1] ""  Engine

BO_ 1544 DiagResponse_Motor: 8 Engine

BO_ 1537 DiagRequest_Motor: 8 Gateway

BO_ 1307 NM_Engine: 4 Engine
 SG_ SleepInd : 12|1@1+ (1,0) [0|1] "" Vector__XXX

BO_ 1306 NM_Gateway_PowerTrain: 4 Gateway
 SG_ SleepInd : 12|1@1+ (1,0) [0|1] "" Vector__XXX

BO_ 1020 GearBoxInfo: 1 Engine
 SG_ EcoMode : 6|2@1+ (1,0) [0|1] "" Vector__XXX
 SG_ ShiftRequest : 3|1@1+ (1,0) [0|0] "" Vector__XXX
 SG_ Gear : 0|3@1+ (1,0) [0|5] ""  Gateway

BO_ 101 EngineStatus: 1 Engine
 SG_ ErrorCode : 2|6@1+ (1,0) [0|0] "" Vector__XXX
 SG_ Status : 0|2@1+ (1,0) [0|0] "" Vector__XXX

BO_ 102 EngineDataIEEE: 8 Engine
 SG_ EngSpeed : 0|32@1- (1,0) [0|8000] "rpm" Vector__XXX
 SG_ EngForce : 32|32@1- (1,0) [0|0] "N" Vector__XXX

BO_ 100 EngineData: 8 Engine
 SG_ PetrolLevel : 24|8@1+ (1,0) [0|255] "l" Vector__XXX
 SG_ EngPower : 48|16@1+ (0.01,0) [0|150] "kW" Vector__XXX
 SG_ EngForce : 32|16@1+ (1,0) [0|0] "N" Vector__XXX
 SG_ IdleRunning : 23|1@1+ (1,0) [0|0] "" Vector__XXX
 SG_ EngTemp : 16|7@1+ (2,-50) [-50|150] "degC" Vector__XXX
 SG_ EngSpeed : 0|16@1+ (1,0) [0|8000] "rpm" Vector__XXX

BO_ 201 ABSdata: 6 Engine
 SG_ AccelarationForce : 32|16@1+ (1,-10000) [0|0] "N" Vector__XXX
 SG_ Diagnostics : 16|8@1+ (1,0) [0|0] "" Vector__XXX
 SG_ GearLock : 15|1@1+ (1,0) [0|0] "" Vector__XXX
 SG_ CarSpeed : 0|10@1+ (0.5,0) [0|300] "mph" Vector__XXX
