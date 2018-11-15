//Maya ASCII 2017ff04 scene
//Name: Danli_Builder.ma
//Last modified: Wed, Nov 14, 2018 08:29:34 PM
//Codeset: 936
requires maya "2017ff04";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" "mtoa" "1.4.2.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 8 , 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "107DFA5E-4A3C-8468-D535-93AB9DB9DD58";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 106.1497157694363 288.53378344929519 160.14727352497951 ;
	setAttr ".r" -type "double3" 683.0616472947263 2919.3999999983371 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "FA3ABC14-4081-9E20-FF77-1CBD9A3DC6C1";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 203.74819983756532;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 87.464525378864877 139.81180036592048 -0.60454738966531141 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "F21F865D-47FA-1A30-4A2E-41BC1A9695B0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 82.655455945577671 1002.0950118129247 -3.3574785243616012 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "038C3D1B-44D6-52CF-F334-B08D8FF9EC22";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 861.55260401908231;
	setAttr ".ow" 17.96632258956328;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 83.958613210740651 140.54240779384219 -2.6292435820648268 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "05C102B1-48D2-215E-7C7D-6488C8A51771";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 18.039410528456418 130.40580316758906 1006.0643379254424 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9160896F-4AED-8D7B-4D18-27A16CE26706";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 997.32602980132924;
	setAttr ".ow" 107.34251187757671;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 11.288700000000011 129.40986648981868 8.7383081241130984 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "6D49A004-4990-9708-65E9-E7B0A6D0AA60";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1012.9449210023331 117.42867160130569 -7.8086123497294384 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "259F897F-4738-F009-8C99-4C827C8C619F";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1006.5175535824104;
	setAttr ".ow" 129.63982675825577;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 6.4273674199224402 3.1727492809295654 5.0599141716236886 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Danli_BuilderGrp";
	rename -uid "28A70A30-421F-FC9B-6EA6-1D9E997A7F9E";
createNode joint -n "Root" -p "Danli_BuilderGrp";
	rename -uid "2487AF95-40BA-FCA2-34A3-42BA602466E5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ds" 2;
	setAttr ".sd" 2;
	setAttr ".radi" 0.5;
createNode joint -n "C_Pelvis" -p "Root";
	rename -uid "A867E6A2-4CED-73A7-E258-8D9B76884D7B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".t" -type "double3" -5.4522272510289061e-015 97.751427058735217 -1.7492691165208469 ;
	setAttr ".r" -type "double3" 0 0 -9.005800580889936 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -90 -11.941089405944894 90 ;
	setAttr ".bps" -type "matrix" 4.4408920985006262e-016 0.97223495543719041 0.23400681918705785 0
		 -3.3306690738754696e-016 0.2340068191870579 -0.97223495543719041 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -6.4455392890319039e-015 100.97468777030896 -1.9155815877663289 1;
	setAttr ".typ" 1;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "C_Spine_0" -p "C_Pelvis";
	rename -uid "B75F5C5C-4BAA-1FB2-4832-5EAFA1E4237B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 5.5444705492328765 0.40060443408775076 1.9384102142541614e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 4.8251325258620703 ;
	setAttr ".bps" -type "matrix" 4.1395750754731127e-016 0.98869385804653387 0.14994817458395523 0
		 -3.6984858124261542e-016 0.14994817458395529 -0.98869385804653387 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -5.3353162644067695e-015 105.83586254749487 -0.74554749183103919 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "C_Spine_1" -p "C_Spine_0";
	rename -uid "0605ADF3-4BAF-A144-30B4-C0A53FD4AEF2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.5750380130811577 0.6162633127950099 -8.001906288426794e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 5.0993120799518179 ;
	setAttr ".bps" -type "matrix" 3.7978272818216287e-016 0.99805704421244823 0.062306793352821133 0
		 -4.0486277981122344e-016 0.062306793352821188 -0.99805704421244823 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -4.7914256492695083e-015 110.77933183772758 0.0041933810887363476 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Spine_2" -p "C_Spine_1";
	rename -uid "907F3AB6-4336-BB5E-DB3F-16B1542DB981";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 5.5099627187144415 0.78567411906282147 3.0367156094663685e-015 ;
	setAttr ".r" -type "double3" 0 0 4.9552840130198632 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 5.099371220341391 ;
	setAttr ".bps" -type "matrix" 3.4265666894241041e-016 0.99966659224587928 -0.025820618650819249 0
		 -4.3673241044288111e-016 -0.025820618650819194 -0.99966659224587928 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -4.3817604091748187e-015 115.76961705878978 0.31572734785284201 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Spine_3" -p "C_Spine_2";
	rename -uid "499B6866-4FB9-4E6D-9054-048E442D81BF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 5.5913347958377022 0.058319441453352404 9.0194966457049053e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 4.824789910637052 ;
	setAttr ".bps" -type "matrix" 3.0402762245271328e-016 0.99379025555777634 -0.11126961830800715 0
		 -4.6445236126830941e-016 -0.11126961830800709 -0.99379025555777634 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -4.1131226509679485e-015 120.76795002001921 0.18662425459874643 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_ChestBegin" -p "C_Spine_3";
	rename -uid "32E4E942-4FBD-3652-C030-268D0378B7E7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 5.5395069476027157 -0.23867159341951261 3.132681375985221e-015 ;
	setAttr ".r" -type "double3" 0 0 3.5768495072362905 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -2.7610804420581587 ;
	setAttr ".bps" -type "matrix" 2.6239101504358873e-016 0.98031079737301496 -0.19746073167565195 0
		 -4.8918273306235261e-016 -0.1974607316756519 -0.98031079737301496 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -3.9854124727198454e-015 125.73690129780813 -0.36972383694129407 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.65517241379310198;
createNode joint -n "C_ChestEnd" -p "C_ChestBegin";
	rename -uid "A19923CF-4B64-AAE2-1A78-78B824B76016";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 26.4963688235879 0.94622694111923711 6.3553796513104995e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 6.0480597069556706e-017 0.98017587611435708 -0.19812938167634997 0
		 -3.957012367318657e-016 -0.19812938167635016 -0.9801758761143573 0 -1.0000000000000002 2.2204460492503136e-016 3.3306690738754696e-016 0
		 -1.360977951735926e-014 150.15467294050094 -5.3054764838503967 1;
	setAttr ".radi" 0.65517241379310198;
createNode joint -n "C_Neck_0" -p "C_ChestBegin";
	rename -uid "12757C6B-486B-79DC-FC75-9BBA7FFBD611";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 21.690934063480945 3.6182256403719535 7.6908164251037104e-015 ;
	setAttr ".r" -type "double3" 0 0 2.6479069417235244 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -29.004709583626489 ;
	setAttr ".bps" -type "matrix" 4.0929698190886877e-016 0.99049282793029758 0.13756437699725235 0
		 -3.749996956028749e-016 0.13756437699725241 -0.99049282793029758 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -5.7909254448923091e-015 150.49894006453104 -5.8632689451436821 1;
	setAttr ".typ" 7;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Neck_1" -p "C_Neck_0";
	rename -uid "51625563-4A9C-985F-9B3C-80B416BED992";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 5.935003839749073 -0.0068557068871226718 -9.3226708254349303e-017 ;
	setAttr ".r" -type "double3" 0 0 4.1744780194208675e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 1.7369994155771411 ;
	setAttr -av ".is" -type "double3" 1 1 1 ;
	setAttr -av ".is";
	setAttr ".bps" -type "matrix" 3.9774202365524855e-016 0.99420750314017159 0.10747762883403142 0
		 -3.8723387470698558e-016 0.10747762883403147 -0.99420750314017159 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -3.2692166900159024e-015 156.60143909637154 -5.0157247189066902 1;
	setAttr ".typ" 7;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Head" -p "C_Neck_1";
	rename -uid "1ECC2B33-4724-580B-504C-AFA47C85A8F9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 4.9740662222150807 0.16655032274392437 1.6452140996774609e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0 0 18.256071274301714 ;
	setAttr ".bps" -type "matrix" 3.9774202365524855e-016 0.99420750314017159 0.10747762883403142 0
		 -3.8723387470698558e-016 0.10747762883403147 -0.99420750314017159 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -1.0072601522555171e-015 163.08851152654773 -4.3144474094236802 1;
	setAttr ".typ" 8;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_FacialRoot" -p "C_Head";
	rename -uid "A953FC7A-4B22-D2AB-3CC2-62A13035AA43";
	setAttr ".t" -type "double3" 3.898190029754744 -0.40663109581948742 -9.4046668144994926e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.9837095073778706 27.927043278189814 -63.230731446679862 ;
	setAttr ".radi" 1.169502703832018;
createNode joint -n "R_Eye" -p "C_FacialRoot";
	rename -uid "0CF320C0-46ED-AED2-0116-3AA5F1686F8B";
	setAttr ".t" -type "double3" 5.4344371282275601 -0.2271556103644351 6.6301403833925683 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_UpperTeeth" -p "C_FacialRoot";
	rename -uid "AE947622-483A-9AA8-8179-36A6A094100A";
	setAttr ".t" -type "double3" 4.0392581516125441 -5.7319294293902683 3.1830535001922846 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidUpper" -p "C_FacialRoot";
	rename -uid "9151DF6D-4FD2-F7E8-2E47-4882FBE45AA7";
	setAttr ".t" -type "double3" 5.7640317496885016 0.43123082185658657 6.6953784991184495 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidLower" -p "C_FacialRoot";
	rename -uid "89947858-4FDF-9D65-ED62-B38A782DF9BC";
	setAttr ".t" -type "double3" 5.152594882273422 -0.63584384586604936 6.5488826865307921 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_Jaw" -p "C_FacialRoot";
	rename -uid "838B4D02-46ED-E42A-BB77-4694E9E584D9";
	setAttr ".t" -type "double3" 0.16436249493362451 -2.1273950746718264 0.46326852461109724 ;
	setAttr ".r" -type "double3" 5.0552479265667838 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 13.071002108670072 60.477845958002632 -18.110959232148456 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_JawEnd" -p "C_Jaw";
	rename -uid "275A2353-4F6A-86B3-8B49-40A73071594F";
	setAttr ".t" -type "double3" 1.8932934647136745e-014 -2.3690434981274109 8.2559646911089146 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_LowerTeeth" -p "C_Jaw";
	rename -uid "7A2A5370-47CC-EE29-517E-D582C38946E3";
	setAttr ".t" -type "double3" 1.6199640310652189e-014 -2.0677581001610301 6.0903653848357573 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -7.5549687203861124e-014 -9.5416640443905503e-015 
		-2.1946285137169665e-017 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidUpper" -p "C_FacialRoot";
	rename -uid "3188CDBF-46DF-F248-D149-8887416464AD";
	setAttr ".t" -type "double3" 8.7544470398705378 -0.54685347258538353 1.1392253508168186 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_Eye" -p "C_FacialRoot";
	rename -uid "988373A9-454C-2920-E717-28983CD1EF3D";
	setAttr ".t" -type "double3" 8.4217614980349786 -1.2045167457536943 1.0796707382389117 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidLower" -p "C_FacialRoot";
	rename -uid "D68707A6-458B-25E1-8FCF-03870A60AE0E";
	setAttr ".t" -type "double3" 8.1387748963319027 -1.6126140826451385 1.0007039542186043 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_Breast" -p "C_ChestBegin";
	rename -uid "A735DB52-407E-F2C1-D9B4-7DA7BE45B9A5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 3.6216725013752882 -7.0416956106231874 -9.1580023467670539 ;
	setAttr ".r" -type "double3" 1.2424041724466862e-017 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 101.42759163891114 89.999999999999972 0 ;
	setAttr ".bps" -type "matrix" 1 1.1542575317290093e-016 -4.5543866415314589e-016 0
		 8.9978394366786654e-017 -0.99999976735171558 -0.00068212646580104175 0 -4.2749774439139096e-016 0.00068212646580120828 -0.99999976735171558 0
		 -7.8906599999999987 133.34433177133462 7.0608686229479503 1;
	setAttr ".radi" 0.5;
createNode joint -n "L_Clav" -p "C_ChestBegin";
	rename -uid "FEA7F2BA-481A-ACAB-3BBB-B592833FDD6C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 17.717465117478394 2.8146310782710469 -3.0703178607186445 ;
	setAttr ".r" -type "double3" 453.64271315784737 85.181119910967013 358.39192852048114 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.97096663178489051 0.21828050916169012 0.097864290118605174 0
		 0.21724984896944344 -0.97588583281488517 0.021197745963948203 0 0.10013142904732321 0.00067869824772238128 -0.99497398774321211 0
		 -1.5920100000000004 148.55822219678041 -4.5013362696721906 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "L_Shoulder" -p "L_Clav";
	rename -uid "B3FEA652-42AE-7BFC-E761-6289889E69CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 11.62861517694321 -0.53654373303520675 -0.36061534919197763 ;
	setAttr ".r" -type "double3" -1.4483562180595446 -0.31329252667945029 -6.4029795759279855 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.26235226505945086 0.96470156178127819 -0.022851383217186154 0
		 0.96011801640670313 -0.26333161408024858 -0.093967311322336461 0 -0.096667903615593617 0.0027125122403274561 -0.99531299533760365 0
		 -15.337299999999994 145.46816650143637 -5.8867444007556049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "L_Elbow" -p "L_Shoulder";
	rename -uid "F83E0B9F-4C50-F894-D07E-9CB645EF7EE6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 29.479203199182187 -4.2002457405487803e-006 0.23433965075284813 ;
	setAttr ".r" -type "double3" 0 -5.5518388240060403 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.9757330068530286e-016 0.25590483538524006 5.5908745408870696e-017 ;
	setAttr ".bps" -type "matrix" 0.43389320214860133 0.85690266771633017 -0.27830649864828944 0
		 0.46157048511156973 -0.47669839186407365 -0.74813857704844777 0 -0.77375020284527474 0.19615417725565557 -0.60235717173621639 0
		 -22.884002750078423 117.71811015626857 -5.2294136802891966 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "L_Wrist" -p "L_Elbow";
	rename -uid "402AA4B0-4F47-6B8E-0674-B68AB30319E4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 26.994227765693438 -1.0143278670825964e-005 -1.4781712564087004 ;
	setAttr ".r" -type "double3" -4.0473011799247295e-016 10.793878565708315 16.323772778487712 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.9583805768143171 -8.9104923241024334 -16.228280983552949 ;
	setAttr ".bps" -type "matrix" 0.42895584361388206 0.86277461858135351 -0.26761323166335294 0
		 0.46607536049615472 -0.46516195703129459 -0.75259425460814888 0 -0.77380271553405833 0.19810176996336093 -0.60165193107768 0
		 -33.622499955472293 96.510213366543951 1.6584548023795049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "L_Thumb_0" -p "L_Wrist";
	rename -uid "E0C9A5B6-4F2A-F2CD-43FC-88965E4BEB2D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.3758886220066984 -0.72272955455377996 2.4977474489450389 ;
	setAttr ".r" -type "double3" -3.7902587073532845 3.4015237073310893 20.744484932451666 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -97.275199514637777 -60.955912782371051 -30.696574869998368 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_1" -p "L_Thumb_0";
	rename -uid "8E3FB754-49EE-DA80-1688-5FA3755AF92E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.3098160274219808 -0.20986386494280396 -0.044042231667667409 ;
	setAttr ".r" -type "double3" -4.6325268754074562 -22.726223731614439 11.845653740274699 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.0524004023769572e-016 -7.9513867036588187e-015 
		7.2715006906401332 ;
	setAttr ".bps" -type "matrix" 0.055315044616028729 0.85188961445670097 -0.5207920224234821 0
		 -0.066970927679814024 0.52358150699809647 0.84933933170159248 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.392099955341656 90.343855173995593 7.8988800193043414 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_2" -p "L_Thumb_1";
	rename -uid "65D694B0-4286-BEF5-0657-ADA68B81CD77";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 3.6941865454295169 0.032166701857583746 -0.047032100924560893 ;
	setAttr ".r" -type "double3" 0 0 8.1445315905649398 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182695930376e-006 -7.9513874826969763e-015 1.9121667007214815 ;
	setAttr ".bps" -type "matrix" 0.02538865761252548 0.98757423772182551 -0.15508881665932572 0
		 -0.08306789620426222 0.15668642148488737 0.98414891654792691 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.5844999553725 87.380918895272671 9.7102593440773521 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_3" -p "L_Thumb_2";
	rename -uid "80D9F012-481C-9C35-7FB3-658F461E985D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.7209765953392591 -0.28166741017844288 8.751927311578811e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472935639464e-006 -1.272221889173292e-014 -9.5324154644603887 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_0" -p "L_Wrist";
	rename -uid "ACE6919F-4BB9-8D64-9B90-5383C2A7E3F2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.2521483735856407 0.60707656548939326 1.2813748389362298 ;
	setAttr ".r" -type "double3" -10.93088521410108 -16.951738870401282 3.4104074863930105 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -166.09489755727895 -23.723410970468716 2.7909266548808409 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_1" -p "L_Index_0";
	rename -uid "9DD623A4-4BCA-2FE4-C618-F986F367E941";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 5.1998029864568522 0.026995571332392387 0.36383855142075028 ;
	setAttr ".r" -type "double3" -7.6618347441088259 -9.8718344184259994 2.116282334792237 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.1408133517827731 -1.0849562550793492 14.469913880452955 ;
	setAttr ".bps" -type "matrix" 0.070409717061975116 0.99555393555438121 -0.062568627485633771 0
		 -0.98388301355159469 0.058975043043975897 -0.1688080565097374 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.526199955645332 87.643111883799548 6.0556173428662277 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_2" -p "L_Index_1";
	rename -uid "0C67260A-47A1-0C1C-85B3-1092834E95B4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.4484968723274392 -0.14016461836264077 -0.069097931548405711 ;
	setAttr ".r" -type "double3" 0 0 -0.41343324266079867 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075475167936065e-006 2.4172215589075463e-012 10.602423120057887 ;
	setAttr ".bps" -type "matrix" -0.11181985677680931 0.98940839977785855 -0.092559916159378919 0
		 -0.98004062785301338 -0.12520668012878922 -0.15441390808019673 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.848899955890239 83.080615224110034 6.3423652107990893 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_3" -p "L_Index_2";
	rename -uid "AC985A44-444A-99E4-00AD-F8921F3E0324";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.6742380016990683 -0.057258112049363902 -0.027581716154962521 ;
	setAttr ".r" -type "double3" 0 0 1.6697912077683464e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4184753380935306e-006 1.114179776505247e-007 3.7411148802044685 ;
	setAttr ".bps" -type "matrix" -0.17552764371641655 0.97913048973488204 -0.10243793419867887 0
		 -0.97065614864558369 -0.18949717246277237 -0.14804547519305628 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.54449995602824 80.387542747408176 6.5942982539178967 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Index_4" -p "L_Index_3";
	rename -uid "D83DA718-4F47-5DC8-2BF9-52B24491095A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.9999487889166971 -9.5583433548540597e-005 5.0735682346925159e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.6222548091771992e-006 2.1328754221312682e-021 -7.0438748376024053e-015 ;
	setAttr ".bps" -type "matrix" -0.17552764376574126 0.97906038632627457 -0.10310580100408247 0
		 -0.97065615208658595 -0.1895981125786585 -0.14791615910060019 0 -0.16436751713921696 0.074116905178621365 0.98361069721523109 0
		 -37.193500000000043 78.323900000000023 6.6473899999999677 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Middle_0" -p "L_Wrist";
	rename -uid "13297D4F-4101-EFBE-A7AD-3FBBDAC8553D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.3340645361147949 0.61247576066605802 -0.16697893793607352 ;
	setAttr ".r" -type "double3" -5.3604445037339801 -18.618362734140231 -2.4273170613722477 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.74956821965023 -10.140718264058906 -3.9529010410603305 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_1" -p "L_Middle_0";
	rename -uid "F9DC6A27-4091-9F1F-9AD4-5781976C9770";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.1570263115850992 -0.28671969097409894 -0.24542006309361242 ;
	setAttr ".r" -type "double3" -0.010626023248719911 0.62382641793922844 -6.8567216829640527 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.0816030219549297 -0.98478532917936401 9.2733107384517854 ;
	setAttr ".bps" -type "matrix" 0.10395166297972064 0.9916543542235956 -0.076260694418124136 0
		 -0.97763766959898024 0.087786495698780886 -0.19109714323873037 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -37.576399955864808 87.488331567080024 3.3879011425116676 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_2" -p "L_Middle_1";
	rename -uid "792E0810-4CB8-D936-B3A3-3B89A21E116E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 5.4502208675993975 0.13658826170568733 -0.025264485742642506 ;
	setAttr ".r" -type "double3" -0.85924902415109339 -0.7412614019272632 5.7122260911334131 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.0913097838706637e-006 -4.9298597704866393e-014 12.229208181143044 ;
	setAttr ".bps" -type "matrix" -0.34213987638704557 0.92704975369059783 -0.15335924872031434 0
		 -0.92169499631984086 -0.36285476607024247 -0.13716687828728594 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -38.072799956113705 82.753082069150992 3.7520511892174429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_3" -p "L_Middle_2";
	rename -uid "A4E4A0A2-41B2-436A-BB03-44B1BD3FBCF0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.7262367298877628 -0.095322647400230665 0.001902526610983557 ;
	setAttr ".r" -type "double3" 0 0 -4.4779671029307639 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4231603136943348e-006 1.8640247401522494e-007 5.1136715350965511 ;
	setAttr ".bps" -type "matrix" -0.4647814717253399 0.86882465116624141 -0.17065142562160487 0
		 -0.86634839689122833 -0.48603348917903533 -0.11494304067864308 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -36.918399956256252 79.6253283979663 4.2694677865740021 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Middle_4" -p "L_Middle_3";
	rename -uid "E8DE9696-4D6B-E784-A8CE-1086F894A50B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.3070211180663449 4.8744769785002973e-006 -2.7786433982157632e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 4.8296730789029342e-006 9.7776588390340548e-021 -1.5712553400649925e-014 ;
	setAttr ".bps" -type "matrix" -0.46478147176281848 0.86870804318900663 -0.17124403407043384 0
		 -0.86634839685366949 -0.48611178182206682 -0.11461147779717742 0 -0.18280765513256333 0.095087703056191936 0.97853956994718994 0
		 -35.846200000000053 77.514099999999985 4.5119399999999752 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Ring_0" -p "L_Wrist";
	rename -uid "CB838C1E-49B6-8799-3D63-04917CC2C5C5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.4531677530367517 0.34126257085424072 -1.8009442161961267 ;
	setAttr ".r" -type "double3" 0.86109351435228365 -13.339706265298895 -4.4087345126047621 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 164.06839155610425 -0.73322402526783015 0.72391043010532663 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_1" -p "L_Ring_0";
	rename -uid "85C76638-4B0E-1E0D-76A5-4B93125EDA6B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.9419624529280597 0.37975299810474894 -0.14403569629809354 ;
	setAttr ".r" -type "double3" -6.6781506409712206 1.0511029070935907 -7.331159369791802 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.2608413222005197 -3.9270558582583468 13.880797026208295 ;
	setAttr ".bps" -type "matrix" -0.048874618441212436 0.99701866515257287 -0.059708064862364088 0
		 -0.93751071452645818 -0.066412347386439724 -0.34155974625636643 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.878599956028665 87.318262414793537 1.436814679904429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_2" -p "L_Ring_1";
	rename -uid "17173F69-4838-B025-0475-6EAD8733A99F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.7053975233399434 0.1474026895179501 -0.040347896039632576 ;
	setAttr ".r" -type "double3" -0.16766030783023628 2.5839136488309 -2.0257787650949353 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.5122662475342308e-016 1.2722218725854015e-014 8.5519751351837439 ;
	setAttr ".bps" -type "matrix" -0.5992120192045679 0.7599241105944099 -0.25191328305208532 0
		 -0.72267560095831995 -0.64882367765463878 -0.23825996536187455 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.671399956256458 83.091888787317785 1.6899118183151796 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_3" -p "L_Ring_2";
	rename -uid "037BA854-4E41-7931-73BF-599F27EE181F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.5517611795472717 0.035586311894764473 0.013243913722243504 ;
	setAttr ".r" -type "double3" 0 0 2.7700166137525266 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9090959104585593e-006 1.2722230932760373e-014 0.37953028054157478 ;
	setAttr ".bps" -type "matrix" -0.65072860768519603 0.71015866795716542 -0.26875071249280685 0
		 -0.67665895938779275 -0.70294486616896223 -0.21909168812835048 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -34.734899956336264 80.636032872997248 2.504046803748186 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Ring_4" -p "L_Ring_3";
	rename -uid "5B68AD30-4573-EE3B-8C1B-6AAEAB73CC4B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.4799326019100505 -7.9379589791983562e-005 -9.0800624512610284e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.2074182697257336e-006 7.7183681763022425e-021 -2.513443368117596e-022 ;
	setAttr ".bps" -type "matrix" -0.65072860770563634 0.70997518078224808 -0.26923506789922219 0
		 -0.67665896822087535 -0.70309414983428609 -0.21861211584691231 0 -0.34450677763978116 0.039923165480920647 0.93793455049818775 0
		 -33.121200000000037 78.766999999999967 3.0184399999999769 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Pinky_0" -p "L_Wrist";
	rename -uid "B41A91E9-4138-C6D3-240A-649AB0B7A0FD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.3313343049689905 -0.83122418360767369 -2.7473963202209668 ;
	setAttr ".r" -type "double3" -18.092337094931757 -19.368678750733842 0.034882595680378936 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 163.29778161456539 8.0744848581134843 0.79558088526347259 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_1" -p "L_Pinky_0";
	rename -uid "13F3425B-431D-7D71-F7E1-32AEF4B6557D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.6891324180822167 -0.051185817554936924 -0.13644049790449608 ;
	setAttr ".r" -type "double3" 2.0549951925839927 7.4245184576119385 -17.703436665549987 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.212706485275667 -7.1521486105678314 21.000260753196642 ;
	setAttr ".bps" -type "matrix" -0.15484431070880841 0.98623547281342838 -0.057989926759633319 0
		 -0.80131607645459935 -0.15971042023289406 -0.57652851385203763 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -35.020399956122709 87.931386935486174 -0.21152847538694763 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_2" -p "L_Pinky_1";
	rename -uid "BE9218AA-4BE3-28A5-9281-A6AB0D31D80F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.5939110778114438 0.0059680142950429872 -0.012693913405709356 ;
	setAttr ".r" -type "double3" -0.39976398688358289 3.2640817207088815 -2.9862355407327956 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472925988586e-006 1.5902787151565399e-015 6.8855114422302188 ;
	setAttr ".bps" -type "matrix" -0.47969722470878084 0.82573243661521722 -0.29674318143504091 0
		 -0.66028386891561475 -0.56243556901034497 -0.49768608897761768 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -34.468499956312485 84.416245127431338 -0.0048361978950919871 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_3" -p "L_Pinky_2";
	rename -uid "09E7687A-4F67-C328-A055-C89A1514CB79";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.1350789087042434 0.074088007832821795 0.019135108186486782 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4242564105554578e-006 1.7911174576888958e-007 6.0210688115630857 ;
	setAttr ".bps" -type "matrix" -0.54631084569401323 0.76218098590756578 -0.34731053050269445 0
		 -0.60632390256410917 -0.64594734374209284 -0.46381392205491606 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -33.628699956356272 82.970590433278744 0.51465380386059834 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Pinky_4" -p "L_Pinky_3";
	rename -uid "0FAD6CC4-4467-55F9-8202-C8A806E2C0D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.1986903450876554 3.6254112693256957e-005 -1.9891313209896566e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 4.3534084824281436e-006 -1.3558656975045113e-021 -1.3609145324450959e-014 ;
	setAttr ".bps" -type "matrix" -0.54631084571130817 0.76194389892066949 -0.3478303534135051 0
		 -0.60632390248966272 -0.64626357315736116 -0.46337319654851244 0 -0.57785446708310706 -0.042247945600334832 0.81504559747577898 0
		 -32.290600000000055 80.994700000000023 1.2117299999999669 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Breast" -p "C_ChestBegin";
	rename -uid "A9614E92-4D72-99F6-55D3-DCA7FE2D93A6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 3.6217075471458173 -7.0417031285967155 9.1579999999999924 ;
	setAttr ".r" -type "double3" 1.2424041724466862e-017 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -78.57240836108889 89.999999999999957 0 ;
	setAttr ".bps" -type "matrix" 1 1.1542575317290093e-016 -4.5543866415314589e-016 0
		 8.9978394366786654e-017 -0.99999976735171558 -0.00068212646580104175 0 -4.2749774439139096e-016 0.00068212646580120828 -0.99999976735171558 0
		 -7.8906599999999987 133.34433177133462 7.0608686229479503 1;
	setAttr ".radi" 0.5;
createNode joint -n "R_Clav" -p "C_ChestBegin";
	rename -uid "DF9A427E-45D0-49D3-4803-4E9B4E473364";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 17.717502996247518 2.8146256702758237 3.0703199999999939 ;
	setAttr ".r" -type "double3" 453.64271315784737 85.181119910967013 358.39192852048114 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -8.537736532683031e-007 2.786693475882494e-014 180 ;
	setAttr ".bps" -type "matrix" 0.97096663178489051 0.21828050916169012 0.097864290118605174 0
		 0.21724984896944344 -0.97588583281488517 0.021197745963948203 0 0.10013142904732321 0.00067869824772238128 -0.99497398774321211 0
		 -1.5920100000000004 148.55822219678041 -4.5013362696721906 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "R_Shoulder" -p "R_Clav";
	rename -uid "610E78DB-416D-FC14-AD98-F18C323A7889";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -11.628592881405778 0.53695266737722136 0.36061741987217566 ;
	setAttr ".r" -type "double3" -1.4483562180595446 -0.31329252667945029 -6.4029795759279855 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377364625159377e-007 -2.7010274577923975e-022 -3.8433538012272986e-022 ;
	setAttr ".bps" -type "matrix" 0.26235226505945086 0.96470156178127819 -0.022851383217186154 0
		 0.96011801640670313 -0.26333161408024858 -0.093967311322336461 0 -0.096667903615593617 0.0027125122403274561 -0.99531299533760365 0
		 -15.337299999999994 145.46816650143637 -5.8867444007556049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "R_Elbow" -p "R_Shoulder";
	rename -uid "E4983B57-4FD4-4F52-1D66-5FB509DB8BBF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -29.47916267739523 -0.00025353802195127173 -0.23434718898680296 ;
	setAttr ".r" -type "double3" 0 -5.5518388240060403 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182696868446e-006 0.25590483538513525 -1.7414023907853381e-014 ;
	setAttr ".bps" -type "matrix" 0.43389320214860133 0.85690266771633017 -0.27830649864828944 0
		 0.46157048511156973 -0.47669839186407365 -0.74813857704844777 0 -0.77375020284527474 0.19615417725565557 -0.60235717173621639 0
		 -22.884002750078423 117.71811015626857 -5.2294136802891966 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "R_Wrist" -p "R_Elbow";
	rename -uid "68060083-4ACD-2506-0BF7-689AAFE8E453";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -26.994247888329681 -0.00051372918053971262 1.4781695105745039 ;
	setAttr ".r" -type "double3" -4.0473011799247295e-016 10.793878565708315 16.323772778487712 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.95838057680862221 -8.9104923241023162 -16.22828098355297 ;
	setAttr ".bps" -type "matrix" 0.42895584361388206 0.86277461858135351 -0.26761323166335294 0
		 0.46607536049615472 -0.46516195703129459 -0.75259425460814888 0 -0.77380271553405833 0.19810176996336093 -0.60165193107768 0
		 -33.622499955472293 96.510213366543951 1.6584548023795049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "R_Thumb_0" -p "R_Wrist";
	rename -uid "1165C7D8-49D8-0318-2463-6A92AE607498";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.37585628637855 0.72282634313756944 -2.497749804362674 ;
	setAttr ".r" -type "double3" -3.7902587073532845 3.4015237073310893 20.744484932451666 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -97.275199514626649 -60.955912782369687 -30.696574870007098 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_1" -p "R_Thumb_0";
	rename -uid "2C5C769F-4960-BA99-4F5A-89852B3F2574";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.3097853516042228 0.20990749581989121 0.043954378094383628 ;
	setAttr ".r" -type "double3" -4.6325268754074562 -22.726223731614439 11.845653740274699 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.4787793334710979e-006 0 7.2715006906401332 ;
	setAttr ".bps" -type "matrix" 0.055315044616028729 0.85188961445670097 -0.5207920224234821 0
		 -0.066970927679814024 0.52358150699809647 0.84933933170159248 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.392099955341656 90.343855173995593 7.8988800193043414 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_2" -p "R_Thumb_1";
	rename -uid "B104C02D-4158-801E-80B4-BBAEA77BA35B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.6942090298463022 -0.032203674383112002 0.047093821869140129 ;
	setAttr ".r" -type "double3" 0 0 8.1445315905649398 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.0963464666400934e-006 3.0180788046920354e-007 1.9121672825396376 ;
	setAttr ".bps" -type "matrix" 0.02538865761252548 0.98757423772182551 -0.15508881665932572 0
		 -0.08306789620426222 0.15668642148488737 0.98414891654792691 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.5844999553725 87.380918895272671 9.7102593440773521 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_3" -p "R_Thumb_2";
	rename -uid "B6092261-4155-9DC0-E3DF-20AB68EBF30E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7210860524860614 0.28158017963276905 9.9518006493326538e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.8908495917493088e-006 2.1883739694161455e-007 -9.5324154644603105 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_0" -p "R_Wrist";
	rename -uid "FDC453C2-4340-ECD9-EF1A-F38C316116D9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.2521300985414854 -0.60716189859113001 -1.281384637911525 ;
	setAttr ".r" -type "double3" -10.93088521410108 -16.951738870401282 3.4104074863930105 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -166.09489755727307 -23.723410970470592 2.7909266548795428 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_1" -p "R_Index_0";
	rename -uid "728982FD-4CF5-8010-11AA-0D8B9FBF551B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.1998237541239973 -0.02721268516555142 -0.36384007517430561 ;
	setAttr ".r" -type "double3" -7.6618347441088259 -9.8718344184259994 2.116282334792237 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.14081335178277607 -1.0849562550793219 14.46991388045301 ;
	setAttr ".bps" -type "matrix" 0.070409717061975116 0.99555393555438121 -0.062568627485633771 0
		 -0.98388301355159469 0.058975043043975897 -0.1688080565097374 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.526199955645332 87.643111883799548 6.0556173428662277 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_2" -p "R_Index_1";
	rename -uid "546D6F0F-45E6-EE6F-FFF2-FBA2F45DDEED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.4485466844228725 0.13989200842198102 0.069078964626843486 ;
	setAttr ".r" -type "double3" 0 0 -0.41343324266079867 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.091309792139952e-006 3.2203116742242588e-014 10.602423120057885 ;
	setAttr ".bps" -type "matrix" -0.11181985677680931 0.98940839977785855 -0.092559916159378919 0
		 -0.98004062785301338 -0.12520668012878922 -0.15441390808019673 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.848899955890239 83.080615224110034 6.3423652107990893 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_3" -p "R_Index_2";
	rename -uid "77E72B5C-48B0-3EC6-A475-F8B441BF55E6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.6742600568045845 0.05716402088353334 0.027574094000238247 ;
	setAttr ".r" -type "double3" 0 0 1.6697912077683464e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.5620484518032726e-006 2.2276042328969221e-008 3.7411148802044707 ;
	setAttr ".bps" -type "matrix" -0.17552764371641655 0.97913048973488204 -0.10243793419867887 0
		 -0.97065614864558369 -0.18949717246277237 -0.14804547519305628 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.54449995602824 80.387542747408176 6.5942982539178967 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Index_4" -p "R_Index_3";
	rename -uid "7D0F529C-4194-644F-6D3F-FFA2A6526C1D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.0000442760113035 -8.4408877285113704e-005 -6.3289637260766085e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.3066511133632065e-006 1.0521355155876613e-022 -1.2855938506757017e-015 ;
	setAttr ".bps" -type "matrix" -0.17552764376574126 0.97906038632627457 -0.10310580100408247 0
		 -0.97065615208658595 -0.1895981125786585 -0.14791615910060019 0 -0.16436751713921696 0.074116905178621365 0.98361069721523109 0
		 -37.193500000000043 78.323900000000023 6.6473899999999677 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Middle_0" -p "R_Wrist";
	rename -uid "BA77696E-4D52-6C25-1C0F-0385C5FB5FFD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.3340823167090861 -0.61228245022428496 0.16698615348285589 ;
	setAttr ".r" -type "double3" -5.3604445037339801 -18.618362734140231 -2.4273170613722477 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.74956821964437 -10.140718264060171 -3.9529010410603136 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_1" -p "R_Middle_0";
	rename -uid "31FE85C4-49E5-55EC-EE95-42AA20BD8F5A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.157044218465316 0.28668032242583763 0.24542120947009138 ;
	setAttr ".r" -type "double3" -0.010626023248719911 0.62382641793922844 -6.8567216829640527 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.0816030219557193 -0.98478532917937056 9.2733107384518636 ;
	setAttr ".bps" -type "matrix" 0.10395166297972064 0.9916543542235956 -0.076260694418124136 0
		 -0.97763766959898024 0.087786495698780886 -0.19109714323873037 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -37.576399955864808 87.488331567080024 3.3879011425116676 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_2" -p "R_Middle_1";
	rename -uid "39CF9D7E-42FE-9A14-A381-C8B74E3A892A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -5.4501567603885093 -0.13672573022819279 0.025223748435060145 ;
	setAttr ".r" -type "double3" -0.85924902415109339 -0.7412614019272632 5.7122260911334131 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.6998693239525152e-006 -4.1347209911146569e-014 12.22920818114304 ;
	setAttr ".bps" -type "matrix" -0.34213987638704557 0.92704975369059783 -0.15335924872031434 0
		 -0.92169499631984086 -0.36285476607024247 -0.13716687828728594 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -38.072799956113705 82.753082069150992 3.7520511892174429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_3" -p "R_Middle_2";
	rename -uid "DD2B39C3-43AF-0770-4078-3888930BFA52";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7262413977722844 0.095505063466106321 -0.0018537596765355602 ;
	setAttr ".r" -type "double3" 0 0 -4.4779671029307639 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.5664193808194016e-006 1.1417443399020682e-007 5.113671543837909 ;
	setAttr ".bps" -type "matrix" -0.4647814717253399 0.86882465116624141 -0.17065142562160487 0
		 -0.86634839689122833 -0.48603348917903533 -0.11494304067864308 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -36.918399956256252 79.6253283979663 4.2694677865740021 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Middle_4" -p "R_Middle_3";
	rename -uid "80613BC7-4953-FCAE-2908-54B076E38D9C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.3069302290549629 0.00014497881329589291 6.4448194606825382e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 4.2688682312579694e-006 -8.9010876007546205e-023 -4.1705265215139931e-015 ;
	setAttr ".bps" -type "matrix" -0.46478147176281848 0.86870804318900663 -0.17124403407043384 0
		 -0.86634839685366949 -0.48611178182206682 -0.11461147779717742 0 -0.18280765513256333 0.095087703056191936 0.97853956994718994 0
		 -35.846200000000053 77.514099999999985 4.5119399999999752 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Ring_0" -p "R_Wrist";
	rename -uid "0BC7540C-4C3C-70BE-FEF2-01B414D5F8CF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.4531529226917002 -0.34134259379140985 1.8009374639529865 ;
	setAttr ".r" -type "double3" 0.86109351435228365 -13.339706265298895 -4.4087345126047621 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 164.0683915561095 -0.73322402526958042 0.72391043010642331 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_1" -p "R_Ring_0";
	rename -uid "CF35D53B-4F68-AD91-855B-288D17B650BC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.9420045032793496 -0.3800453118105338 0.14394617048110803 ;
	setAttr ".r" -type "double3" -6.6781506409712206 1.0511029070935907 -7.331159369791802 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.2608413222006476 -3.9270558582584827 13.88079702620839 ;
	setAttr ".bps" -type "matrix" -0.048874618441212436 0.99701866515257287 -0.059708064862364088 0
		 -0.93751071452645818 -0.066412347386439724 -0.34155974625636643 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.878599956028665 87.318262414793537 1.436814679904429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_2" -p "R_Ring_1";
	rename -uid "A35EC8A4-4E77-45FF-E955-D8A975C22CFA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.7054165621743707 -0.1478357716545986 0.040231330257803677 ;
	setAttr ".r" -type "double3" -0.16766030783023628 2.5839136488309 -2.0257787650949353 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377364625159387e-007 9.4787915988669299e-023 8.5519751351837439 ;
	setAttr ".bps" -type "matrix" -0.5992120192045679 0.7599241105944099 -0.25191328305208532 0
		 -0.72267560095831995 -0.64882367765463878 -0.23825996536187455 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.671399956256458 83.091888787317785 1.6899118183151796 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_3" -p "R_Ring_2";
	rename -uid "7D046BA0-4358-5B14-329A-688E1F48A624";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.5517299414715566 -0.035642758695445309 -0.013270781823379707 ;
	setAttr ".r" -type "double3" 0 0 2.7700166137525266 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.478779333455298e-006 -4.7708071796154505e-015 0.37953028054061455 ;
	setAttr ".bps" -type "matrix" -0.65072860768519603 0.71015866795716542 -0.26875071249280685 0
		 -0.67665895938779275 -0.70294486616896223 -0.21909168812835048 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -34.734899956336264 80.636032872997248 2.504046803748186 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Ring_4" -p "R_Ring_3";
	rename -uid "5C40771F-4A5D-35E6-194A-7A9A9FEB7205";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.479795180924711 0.00078541953791955166 0.00022842681332946313 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.909095910416422e-006 3.2158829368532666e-020 6.9292112432253998e-016 ;
	setAttr ".bps" -type "matrix" -0.65072860770563634 0.70997518078224808 -0.26923506789922219 0
		 -0.67665896822087535 -0.70309414983428609 -0.21861211584691231 0 -0.34450677763978116 0.039923165480920647 0.93793455049818775 0
		 -33.121200000000037 78.766999999999967 3.0184399999999769 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Pinky_0" -p "R_Wrist";
	rename -uid "B788B802-4F29-5831-F09B-EB9C0D3E9880";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.3313373637239891 0.83113860748414936 2.7473832926451385 ;
	setAttr ".r" -type "double3" -18.092337094931757 -19.368678750733842 0.034882595680378936 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 163.29778161457074 8.0744848581118536 0.79558088526522486 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_1" -p "R_Pinky_0";
	rename -uid "4101554D-4814-6208-2D0E-D48B842A2752";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.6891609652105046 0.050635774083858109 0.13600504244713818 ;
	setAttr ".r" -type "double3" 2.0549951925839927 7.4245184576119385 -17.703436665549987 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.21270648527576 -7.1521486105678171 21.000260753196642 ;
	setAttr ".bps" -type "matrix" -0.15484431070880841 0.98623547281342838 -0.057989926759633319 0
		 -0.80131607645459935 -0.15971042023289406 -0.57652851385203763 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -35.020399956122709 87.931386935486174 -0.21152847538694763 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_2" -p "R_Pinky_1";
	rename -uid "333E3A23-457C-AAA6-81BA-62BAFA58FA0C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5938280018065569 -0.0054679960714452136 0.012868739254557227 ;
	setAttr ".r" -type "double3" -0.39976398688358289 3.2640817207088815 -2.9862355407327956 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4148365388774422e-006 -9.5416641865724244e-015 6.8855114422302188 ;
	setAttr ".bps" -type "matrix" -0.47969722470878084 0.82573243661521722 -0.29674318143504091 0
		 -0.66028386891561475 -0.56243556901034497 -0.49768608897761768 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -34.468499956312485 84.416245127431338 -0.0048361978950919871 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_3" -p "R_Pinky_2";
	rename -uid "84F342F9-4541-B65F-3877-75910EFE82FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.1351783452594546 -0.074179076045794545 -0.019154190457769005 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.416814309602791e-006 3.7605808296975473e-008 6.0210687710898707 ;
	setAttr ".bps" -type "matrix" -0.54631084569401323 0.76218098590756578 -0.34731053050269445 0
		 -0.60632390256410917 -0.64594734374209284 -0.46381392205491606 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -33.628699956356272 82.970590433278744 0.51465380386059834 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Pinky_4" -p "R_Pinky_3";
	rename -uid "705EC9C3-4074-5422-2834-B9858B5C643C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.1985774110272942 0.00010777422389196545 5.4820132120880771e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.9124823603063784e-006 2.0966509481088061e-021 -2.5679388016955874e-015 ;
	setAttr ".bps" -type "matrix" -0.54631084571130817 0.76194389892066949 -0.3478303534135051 0
		 -0.60632390248966272 -0.64626357315736116 -0.46337319654851244 0 -0.57785446708310706 -0.042247945600334832 0.81504559747577898 0
		 -32.290600000000055 80.994700000000023 1.2117299999999669 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Hip" -p "C_Pelvis";
	rename -uid "2194CF6E-4676-EB92-E991-95B8467E2EAD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -5.0929759293704846 -0.7254953837186322 -8.2086503022897066 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.067223683321926922 178.37259626741269 23.310230232946132 ;
	setAttr -av ".is" -type "double3" 1 1 1 ;
	setAttr -av ".is";
	setAttr ".bps" -type "matrix" 0.04367621427123513 0.99879915221154247 -0.022195536678289766 0
		 -1.3006955835555549e-012 0.022216737247664126 0.999753177832443 0 0.99904573884629189 -0.043665434013329021 0.00097034297773582754 0
		 -8.2375200000000035 99.635493474825282 -2.2160409616281522 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "L_Knee" -p "L_Hip";
	rename -uid "2E3EB79F-40D0-0132-8886-B8A2D6270CEA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 40.891386882548673 -0.041734211329129134 -0.12321833538651461 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 7.7150948596808062 ;
	setAttr ".bps" -type "matrix" 0.043710370994654441 0.99896923390645309 0.012242270045389339 0
		 3.5294000512962886e-010 -0.012253981865253649 0.99992491714550569 0 0.99904424499994482 -0.043707089090908237 -0.00053562644606822672 0
		 -10.096999562900118 57.112293455685503 -1.2710809628003075 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "L_Ankle" -p "L_Knee";
	rename -uid "E9397239-4ED8-7181-CC71-9193E0A8922E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 45.144806828546876 0.81149944987865652 -0.34356651373457048 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.11106232739602673 -3.9405698870282539 -72.430662072435709 ;
	setAttr -av ".is" -type "double3" 1 1 1 ;
	setAttr -av ".is";
	setAttr ".bps" -type "matrix" 0.089586411029085211 0.82001406268021293 -0.56528860944266346 0
		 -0.078021190938231205 0.57160461050695421 0.81681139990316831 0 0.99291840990260016 -0.029070711272434359 0.11518647933940374 0
		 -11.971399122896578 14.273993436447512 -1.7960609639808891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "L_Ball" -p "L_Ankle";
	rename -uid "EA81F17C-437F-52EA-FBB2-CA8D777841FD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 11.228815760636383 3.6859404417555197e-014 -2.3092638912203256e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -8.7198046459577263 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "L_Toe" -p "L_Ball";
	rename -uid "22DEF18F-4AED-1E11-F873-6997C79C07B7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 8.7017316428973004 6.2172489379008766e-015 -1.7763568394002505e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Hip" -p "C_Pelvis";
	rename -uid "CD49DDAE-4C7F-35DF-F27B-379970745A25";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -5.0929458357841808 -0.72548528688372627 8.2086499999999969 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -179.93277631667542 1.6274037325873114 23.310230232946132 ;
	setAttr -av ".is" -type "double3" 1 1 1 ;
	setAttr -av ".is";
	setAttr ".bps" -type "matrix" 0.04367621427123513 0.99879915221154247 -0.022195536678289766 0
		 -1.3006955835555549e-012 0.022216737247664126 0.999753177832443 0 0.99904573884629189 -0.043665434013329021 0.00097034297773582754 0
		 -8.2375200000000035 99.635493474825282 -2.2160409616281522 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "R_Knee" -p "R_Hip";
	rename -uid "6A5FF4D2-446B-99E6-B346-47A0DBF715B8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -40.89137838553593 0.041733621015773048 0.12321512407854485 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 8.5377367037950694e-007 3.5782791432321861e-013 7.715094859680816 ;
	setAttr ".bps" -type "matrix" 0.043710370994654441 0.99896923390645309 0.012242270045389339 0
		 3.5294000512962886e-010 -0.012253981865253649 0.99992491714550569 0 0.99904424499994482 -0.043707089090908237 -0.00053562644606822672 0
		 -10.096999562900118 57.112293455685503 -1.2710809628003075 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "R_Ankle" -p "R_Knee";
	rename -uid "6DD08D51-4883-C1ED-BD3D-8182F9A9CE98";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -45.144850168937531 -0.81149091168966603 0.34353186755536846 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.11106232739700697 -3.940569887030676 -72.430662072435652 ;
	setAttr ".bps" -type "matrix" 0.089586411029085211 0.82001406268021293 -0.56528860944266346 0
		 -0.078021190938231205 0.57160461050695421 0.81681139990316831 0 0.99291840990260016 -0.029070711272434359 0.11518647933940374 0
		 -11.971399122896578 14.273993436447512 -1.7960609639808891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "R_Ball" -p "R_Ankle";
	rename -uid "5E5F2A9C-4A7B-FD7A-00AC-5E8DE8EFA2F9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -11.228809405219856 6.3842592958884836e-006 5.3899808222013235e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 8.5377364810059067e-007 -2.4251729386916867e-014 -8.7198046459577121 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Toe" -p "R_Ball";
	rename -uid "BD286592-4DAE-F4E9-2C39-A3A57F0AA8DD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -8.7017664088686182 3.2157868692372915e-006 -5.4262502127144785e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode transform -n "locator_L_Foot_Ext" -p "Danli_BuilderGrp";
	rename -uid "67A6E1BE-4984-8BED-FDA7-2BAAE729B177";
	setAttr ".t" -type "double3" 15.396000648567925 0.52180777411644597 3.965269403832814 ;
	setAttr ".r" -type "double3" 0 9.4173334103142192 0 ;
createNode locator -n "locator_L_Foot_ExtShape" -p "locator_L_Foot_Ext";
	rename -uid "F29237AB-4035-C160-E92F-218216BEA562";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -3.5527136788005009e-015 -2.7755575615628914e-017 
		0 ;
createNode transform -n "locator_L_Foot_Int" -p "Danli_BuilderGrp";
	rename -uid "A09854E8-4D9B-C673-70A5-E2B1F1270BE2";
	setAttr ".t" -type "double3" 6.427367419922442 0.52518719836740413 5.0599141716236877 ;
	setAttr ".r" -type "double3" 0 4.6348474218739044 0 ;
createNode locator -n "locator_L_Foot_IntShape" -p "locator_L_Foot_Int";
	rename -uid "9D43950C-443A-9ED5-60EF-C9BABBA614B2";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -1.572007826684607e-015 0 5.8882639917960951e-016 ;
createNode transform -n "locator_L_Foot_Base" -p "Danli_BuilderGrp";
	rename -uid "7FD10D27-4946-0719-5826-B09868D7BFC8";
	setAttr ".t" -type "double3" 9.4789462086957688 0.87666600942611694 -10.08525659116237 ;
	setAttr ".r" -type "double3" 0 2.8342171357441188 0 ;
createNode locator -n "locator_L_Foot_BaseShape" -p "locator_L_Foot_Base";
	rename -uid "22E9525E-401A-EC58-EAB1-07AEC17AB34F";
	setAttr -k off ".v";
createNode transform -n "locator_L_Foot_BaseSwive" -p "Danli_BuilderGrp";
	rename -uid "B4A7CE6B-4B31-A3BF-57C6-01888111C488";
	setAttr ".t" -type "double3" 10.179226875305176 0.39494422098822923 -5.8215718269348145 ;
	setAttr ".r" -type "double3" 0 5.5049381691980628 0 ;
createNode locator -n "locator_L_Foot_BaseSwiveShape" -p "locator_L_Foot_BaseSwive";
	rename -uid "5A39BEB1-47FF-0B3A-A316-4BB934187B72";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 1.1102230246251565e-016 -5.5511151231257827e-016 ;
createNode transform -n "locator_L_Foot_ToeSwive" -p "Danli_BuilderGrp";
	rename -uid "A8E3862C-4EE0-C5CF-0A49-6BBD9753B20C";
	setAttr ".t" -type "double3" 11.061084747314453 0.35744698434657796 4.6842575073242188 ;
	setAttr ".r" -type "double3" 0 4.2562357227711889 0 ;
createNode locator -n "locator_L_Foot_ToeSwiveShape" -p "locator_L_Foot_ToeSwive";
	rename -uid "8EB5E4F5-4C96-A985-AAE2-91BD7F12E686";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 2.7755575615628914e-017 0 ;
createNode transform -n "locator_L_LegPV" -p "Danli_BuilderGrp";
	rename -uid "DFD27427-4BEC-BBFF-8758-2893483A331D";
	setAttr ".t" -type "double3" 10.70231348172387 50.125032684726207 45.752019378948184 ;
createNode locator -n "locator_L_LegPVShape" -p "locator_L_LegPV";
	rename -uid "4578B3D6-422B-745B-C186-E29E4F5B133D";
	setAttr -k off ".v";
createNode transform -n "locator_R_LegPV" -p "Danli_BuilderGrp";
	rename -uid "9A4EB3CD-4306-0694-4D4A-23B1A216C26B";
	setAttr ".t" -type "double3" -10.702 50.125032684726207 45.752019378948184 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode locator -n "locator_R_LegPVShape" -p "locator_R_LegPV";
	rename -uid "C19F1B2F-42DC-9E2D-DE75-D290BB40DE0A";
	setAttr -k off ".v";
createNode transform -n "locator_L_ArmPV" -p "Danli_BuilderGrp";
	rename -uid "76E955B2-4889-6262-C370-93A3E0568122";
	setAttr ".t" -type "double3" 45.198964644805699 141.57973010018569 -51.091824987540441 ;
createNode locator -n "locator_L_ArmPVShape" -p "locator_L_ArmPV";
	rename -uid "0FB34EC9-43A1-40CE-DFCB-049C3D711343";
	setAttr -k off ".v";
createNode transform -n "locator_R_ArmPV" -p "Danli_BuilderGrp";
	rename -uid "55CF71CC-4A17-C1B0-8066-13853A07D89E";
	setAttr ".t" -type "double3" -45.199 141.57973010018569 -51.091824987540441 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode locator -n "locator_R_ArmPVShape" -p "locator_R_ArmPV";
	rename -uid "85AC052F-42A6-A7AA-036F-EEAFE5F2A7B9";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "04316D1B-4F34-BCB4-9CFA-16A240C5521E";
	setAttr -s 130 ".lnk";
	setAttr -s 130 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "977C823A-4C54-9ABC-D16C-5BB04086BFB7";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 0 ;
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "D0AC5692-4395-573C-14CF-338E16A93E64";
createNode displayLayerManager -n "layerManager";
	rename -uid "F1E72D0D-4B54-F68C-E2EE-378DF35161B2";
	setAttr ".cdl" 2;
	setAttr -s 3 ".dli[1:2]"  1 2;
createNode displayLayer -n "defaultLayer";
	rename -uid "C88278F6-4870-E782-9E2F-E38DD6348366";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "1125BCD0-4A6C-176D-B61E-728F1E7E32C1";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "D54C03A3-4EF0-A8DC-A8AE-10BE7EC92377";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "35E8EF1E-4E08-F324-2DC3-BC9B49006F09";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n"
		+ "            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n"
		+ "            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n"
		+ "            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n"
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1875\n            -height 1075\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n"
		+ "            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n"
		+ "            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n"
		+ "            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n"
		+ "            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n"
		+ "                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n"
		+ "                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n"
		+ "                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n"
		+ "                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n"
		+ "                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n"
		+ "                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n"
		+ "                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n"
		+ "                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n"
		+ "                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1875\\n    -height 1075\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1875\\n    -height 1075\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "26C8EC8A-4839-4B2C-4A82-818025A0BFFA";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 120 -ast 0 -aet 250 ";
	setAttr ".st" 6;
createNode blinn -n "blinn1";
	rename -uid "607A2F54-4756-892E-A26B-26A32BE5FF6A";
	setAttr ".ec" 0.40000000596046448;
	setAttr ".sro" 0.30000001192092896;
createNode shadingEngine -n "blinn1SG";
	rename -uid "94C8F6BE-4DB0-4B27-9B4C-5A892B60201F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "19C657F3-43CE-2C89-5C30-69893CE31A75";
createNode blinn -n "blinn2";
	rename -uid "A7CCE33A-41B2-4658-6F5D-B7A672A1CA94";
	setAttr ".ec" 0.40000000596046448;
	setAttr ".sro" 0.30000001192092896;
createNode shadingEngine -n "blinn2SG";
	rename -uid "16752F95-45AC-8105-D023-59AD00463A84";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "04910D07-47A8-D06E-8326-EDB5C46A8E6F";
createNode file -n "file1";
	rename -uid "1F26E87C-4840-7860-5884-17ABCDF04033";
	setAttr ".ftn" -type "string" "D:/ZG/girl/base/tex/body.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "40704B3E-4004-BF15-B6BD-3FB0BFD58DD0";
createNode file -n "file2";
	rename -uid "110CC95C-4732-BC5A-1898-1EA5A4755C23";
	setAttr ".ftn" -type "string" "D:/ZG/girl/base/tex/head.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture2";
	rename -uid "7991FFB8-4886-FAC6-AF4D-B9A85481481A";
createNode renderLayerManager -n "pasted__renderLayerManager";
	rename -uid "CAB473EB-4EE7-5313-2B0C-6C8F63113034";
createNode renderLayer -n "pasted__defaultRenderLayer";
	rename -uid "CA23FEC8-4051-D33F-3E8C-77A466B96449";
	setAttr ".g" yes;
createNode renderLayerManager -n "pasted__renderLayerManager1";
	rename -uid "4AE68E5D-4298-A948-F02E-A99E6C852627";
createNode renderLayer -n "pasted__defaultRenderLayer1";
	rename -uid "2148CA82-4D30-7767-830C-C29BF6A75CBD";
	setAttr ".g" yes;
createNode renderLayerManager -n "pasted__pasted__renderLayerManager";
	rename -uid "659BB30F-47CE-AAE6-BD03-87910448AEF8";
createNode renderLayer -n "pasted__pasted__defaultRenderLayer";
	rename -uid "D8538F14-4F5D-991F-75BC-DD9216A3F334";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "F4D21862-4AA1-9059-192E-2BA92EEA5882";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -707.23627301080751 -559.57891923102795 ;
	setAttr ".tgi[0].vh" -type "double2" 676.59038950104809 575.41580280595804 ;
	setAttr -s 2 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 48.571430206298828;
	setAttr ".tgi[0].ni[0].y" 80;
	setAttr ".tgi[0].ni[0].nvs" 1923;
	setAttr ".tgi[0].ni[1].x" -258.57144165039062;
	setAttr ".tgi[0].ni[1].y" 57.142856597900391;
	setAttr ".tgi[0].ni[1].nvs" 1923;
createNode renderLayerManager -n "renderLayerManager5";
	rename -uid "A064131F-4EAD-54C1-EE86-4990D41BF377";
createNode renderLayer -n "defaultRenderLayer5";
	rename -uid "BCEBCB55-41EC-A5EB-5803-0AB57B49C2A3";
	setAttr ".g" yes;
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_bodySG";
	rename -uid "7458C025-49BE-4CB8-45F5-80BCF7AD5C39";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo19";
	rename -uid "E2665DF0-4527-0483-B37D-F689201B58F1";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body";
	rename -uid "3995C1A0-49B3-F06F-603F-1DBBFE7E8C73";
	setAttr ".sc" -type "float3" 0.18099999 0.18099999 0.18099999 ;
createNode file -n "Elisa_Model_file6";
	rename -uid "416DF2BF-4A60-C778-EAAD-338511D8D0DE";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture6";
	rename -uid "BB984DB0-4E2A-0D5D-4D65-6DA8E2F52BEF";
createNode materialInfo -n "Elisa_Model_materialInfo24";
	rename -uid "E6F6798A-4F10-014D-210B-138691F1CF88";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_clothes01_SG";
	rename -uid "CB1129B1-4243-AFD8-6730-EABB0216A47F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_clothes03";
	rename -uid "E0EC3892-4B0A-FA49-A8B6-6DA570A25CB7";
	setAttr ".sc" -type "float3" 0.066265061 0.066265061 0.066265061 ;
	setAttr ".ec" 0.58703804016113281;
	setAttr ".sro" 0.27710843086242676;
createNode file -n "Elisa_Model_file9";
	rename -uid "D83DF775-4BC9-032A-D0C6-58829BAF7063";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_clothes01_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture9";
	rename -uid "B93C3515-472A-E09A-26BE-9D8AF7FA35B1";
createNode materialInfo -n "Elisa_Model_materialInfo25";
	rename -uid "F073546F-43F9-471A-EEF0-5BA042FE2724";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_clothes02_SG";
	rename -uid "4937A0CB-4D3D-D24C-6ECD-F39CE3D7A5C1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_clothes04";
	rename -uid "37D9F77C-497E-FF1E-0DCD-5D92B7C0DE32";
	setAttr ".sc" -type "float3" 0.48795182 0.48795182 0.48795182 ;
	setAttr ".rfl" 0.41935482621192932;
	setAttr ".ec" 0.49027353525161743;
	setAttr ".sro" 0.17469879984855652;
createNode file -n "Elisa_Model_file8";
	rename -uid "064A6E1A-4434-EAC4-4FFE-3BAFA7D95D7F";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_clothes02_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture8";
	rename -uid "BD228EDB-45AE-92C4-647E-93873FCBC69F";
createNode materialInfo -n "Elisa_Model_materialInfo21";
	rename -uid "51A07202-462B-C771-C7E9-0A9B7AE4CF74";
createNode shadingEngine -n "Elisa_Model_blinn13SG";
	rename -uid "5A4A7183-4C34-311E-8BD4-E68335DBBAB3";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Shoes1";
	rename -uid "DC79BD34-4C95-D80F-6154-9A884591C322";
createNode materialInfo -n "Elisa_Model_materialInfo16";
	rename -uid "A2922FF9-467A-A9D4-4200-179D945EF7E5";
createNode shadingEngine -n "Elisa_Model_blinn10SG";
	rename -uid "D9E2020B-4EBC-9BCF-D007-D4B587E0AB94";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth1";
	rename -uid "D0B306AE-48A3-60EC-ED6D-F883E6DE4672";
createNode file -n "Elisa_Model_Elisa_Duncan_file1";
	rename -uid "8DD8CF63-4446-D857-4EEA-0891C6D44E13";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_Elisa_Duncan_place2dTexture1";
	rename -uid "BA4C9E6E-4C3A-8068-B7A6-A98782C7AC34";
createNode materialInfo -n "Elisa_Model_materialInfo8";
	rename -uid "0FB5E9C8-4CBB-B813-2CA6-D6A9FB90F7D8";
createNode shadingEngine -n "Elisa_Model_blinn2SG";
	rename -uid "5D67D278-4911-32BF-C760-638D120C7531";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye";
	rename -uid "C2F898D2-46E7-9139-456D-768D176F2EA2";
createNode file -n "Elisa_Model_file5";
	rename -uid "B62C5F15-435C-4181-F449-C49653FD5D0A";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa_Duncan_eye_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture5";
	rename -uid "45899224-4728-1B5D-B3B9-179F4068B4D4";
createNode shadingEngine -n "Elisa_Model_polySurface846SG";
	rename -uid "D5D04D3C-4510-9621-18DF-77851304B867";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo7";
	rename -uid "3A6914E8-489C-93DD-3E19-D8A2BEE10B2F";
createNode lambert -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar";
	rename -uid "BB4FD91D-49D4-7ABC-6F55-AA8AAEC3269C";
	addAttr -is true -ci true -k true -sn "GMHMaterial" -ln "GMHMaterial" -smn 1 -smx 
		1 -at "double";
	setAttr -k on ".GMHMaterial" 1;
createNode file -n "Elisa_Model_file4";
	rename -uid "4B185CFD-4714-E0A6-9379-2B90D5CDCCB2";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_hair_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture4";
	rename -uid "1073A1D4-46E3-6995-9F20-DFB8C52FFB2E";
createNode materialInfo -n "Elisa_Model_materialInfo20";
	rename -uid "1D4B3E07-453F-07A8-4CB4-EE8CF77E7D3A";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_head_SG";
	rename -uid "8062D6FA-4404-EF20-5172-5EAD0BDA0DF9";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_head";
	rename -uid "16885F4D-497B-0E29-25F8-208C8D742584";
	setAttr ".sc" -type "float3" 0.18064517 0.18064517 0.18064517 ;
createNode file -n "Elisa_Model_file7";
	rename -uid "01442995-4595-4DB0-F2C9-839D80C96A07";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture7";
	rename -uid "2B3E3969-4CBD-1FA8-412F-92BF26F8C9F6";
createNode shadingEngine -n "Elisa_Model_blinn3SG";
	rename -uid "0EAD1725-49FA-0160-1749-7AA7284A0DB3";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo9";
	rename -uid "C2401F65-433B-58A0-5ECA-7C89E5F635DE";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows1";
	rename -uid "98596C1C-4E7A-58D8-C663-FA943FBCCE17";
	setAttr ".c" -type "float3" 0.077200003 0.0605 0.0605 ;
createNode shadingEngine -n "Elisa_Model_blinn11SG";
	rename -uid "78F56D02-451A-C6C3-895A-0597913CD31B";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo17";
	rename -uid "A518D46A-4D63-7427-3D8C-95A20D2C63D3";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash1";
	rename -uid "902225C1-483E-2B4E-4C28-BEB437BD8F4A";
	setAttr ".c" -type "float3" 0.068400003 0.045600001 0.045600001 ;
createNode shadingEngine -n "Elisa_Model_blinn8SG";
	rename -uid "55502A13-489E-ACA4-42B2-8DA299DEDC01";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo14";
	rename -uid "7EDE1686-4B23-DBC7-BD14-22908F2C8B95";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow2";
	rename -uid "C24F5726-434D-D133-DAD2-41AA32D22308";
	setAttr ".it" -type "float3" 1 1 1 ;
createNode shadingEngine -n "Elisa_Model_blinn12SG";
	rename -uid "A954ECBD-4E56-8B77-93F6-AE97E287A14E";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo18";
	rename -uid "763A01DC-49B5-41F6-7873-12878521B526";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears1";
	rename -uid "3AD26A37-4ADD-FC27-6B2B-7E93F2D9A789";
	setAttr ".c" -type "float3" 0.3581 0.17550001 0.17550001 ;
	setAttr ".it" -type "float3" 0.43225807 0.43225807 0.43225807 ;
createNode shadingEngine -n "Elisa_Model_blinn5SG";
	rename -uid "9E475481-4B0B-4CDA-EB6B-ACB9CC4A127E";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo11";
	rename -uid "6ADA3456-46AE-9778-B422-B6B236AAB82F";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside1";
	rename -uid "D0E2C47D-4CAE-B209-F070-AAADF40B3FAE";
	setAttr ".c" -type "float3" 0.41069999 0.18520001 0.18520001 ;
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_bodySG1";
	rename -uid "D67AC2DD-4DA2-B2D3-22B9-4F904213578D";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo34";
	rename -uid "E0CE9B75-4885-B8F3-A3D7-B0B1BFC90340";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body1";
	rename -uid "5108BE9E-4727-1EB4-637A-97B0B6016833";
	setAttr ".sc" -type "float3" 0.18099999 0.18099999 0.18099999 ;
createNode file -n "Elisa_Model_file12";
	rename -uid "AE0F430B-460F-759E-C9F1-9D96DFF84FA7";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture12";
	rename -uid "EC936F19-469E-23F6-B8AA-A89D23017544";
createNode materialInfo -n "Elisa_Model_materialInfo37";
	rename -uid "4ABDE086-47AB-4242-450E-C0BB6E81427E";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_clothes01_SG1";
	rename -uid "67F05A24-4C2B-E938-0BDE-FC960A1ED8AD";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_clothes05";
	rename -uid "9C58DA1B-4817-35B2-5821-AB812F761699";
	setAttr ".sc" -type "float3" 0.066265061 0.066265061 0.066265061 ;
	setAttr ".ec" 0.58703804016113281;
	setAttr ".sro" 0.27710843086242676;
createNode file -n "Elisa_Model_file15";
	rename -uid "C4051F04-4A97-6328-AD13-489EA135BEF5";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_clothes01_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture15";
	rename -uid "92F28985-4FF4-74DA-296D-0BA1E5183B6F";
createNode materialInfo -n "Elisa_Model_materialInfo38";
	rename -uid "3D1C742E-46CF-139B-555D-4D9B735280A2";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_clothes02_SG1";
	rename -uid "642B2DF3-47D6-CF41-E6DE-BC8810C3CF68";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_clothes06";
	rename -uid "C14D925F-499E-E9F9-A4B8-A2B17A6FE811";
	setAttr ".sc" -type "float3" 0.48795182 0.48795182 0.48795182 ;
	setAttr ".rfl" 0.41935482621192932;
	setAttr ".ec" 0.49027353525161743;
	setAttr ".sro" 0.17469879984855652;
createNode file -n "Elisa_Model_file14";
	rename -uid "E9A918BB-4428-D0C4-236C-7B8A99A1B2A6";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_clothes02_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture14";
	rename -uid "06CE0658-49D4-9511-A8CE-1FBD807BA10C";
createNode materialInfo -n "Elisa_Model_materialInfo36";
	rename -uid "B415A4C4-4CD1-B133-3E47-46BF3928593C";
createNode shadingEngine -n "Elisa_Model_blinn13SG1";
	rename -uid "05E84682-49EA-1D9D-2A48-9CAD23B5820A";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Shoes2";
	rename -uid "3D31D25C-40DF-4EDC-BE97-58B2870003A7";
createNode materialInfo -n "Elisa_Model_materialInfo31";
	rename -uid "EA74563A-40BA-DD3E-3888-619511BF7AE5";
createNode shadingEngine -n "Elisa_Model_blinn10SG1";
	rename -uid "402D1400-4C59-BF28-621C-5D9FE34DE592";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth2";
	rename -uid "524A84D0-4596-5715-3613-AF99B04A0FDB";
createNode file -n "Elisa_Model_Elisa_Duncan_file2";
	rename -uid "E1E2878C-4C65-7458-2E63-23B8F1BB2646";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_Elisa_Duncan_place2dTexture2";
	rename -uid "89B367C0-406D-2ADB-751C-ED91D3F1E3C3";
createNode materialInfo -n "Elisa_Model_materialInfo27";
	rename -uid "6444E960-444E-D755-2870-B4A2C92D7BD9";
createNode shadingEngine -n "Elisa_Model_blinn2SG1";
	rename -uid "A3469617-43B8-CE4B-0B18-4E985CC95339";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye1";
	rename -uid "9F0D6B60-4425-98E1-171E-2C9E99624E08";
createNode file -n "Elisa_Model_file11";
	rename -uid "14EA3F7D-49A4-1338-388F-7C9D18EB7048";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa_Duncan_eye_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture11";
	rename -uid "C3408509-48F6-8954-7B9F-868E2C1FD071";
createNode shadingEngine -n "Elisa_Model_polySurface846SG1";
	rename -uid "9BEDE86E-4796-4C5C-924B-C690B4DE53E2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo26";
	rename -uid "B89619AC-4CF4-89C3-A47E-27BCC44B10FA";
createNode lambert -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar1";
	rename -uid "721E8C86-4DA8-A1D7-F8F0-7B9BC7FD3404";
	addAttr -is true -ci true -k true -sn "GMHMaterial" -ln "GMHMaterial" -smn 1 -smx 
		1 -at "double";
	setAttr -k on ".GMHMaterial" 1;
createNode file -n "Elisa_Model_file10";
	rename -uid "8A6DFE57-4918-0C81-140F-08A4303E866E";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_hair_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture10";
	rename -uid "70E4BF6D-4541-7511-E9CF-1997C254CAFE";
createNode materialInfo -n "Elisa_Model_materialInfo35";
	rename -uid "2C710179-41A1-98C5-EAF1-78B0C1697D80";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_head_SG1";
	rename -uid "6E7E10BB-48D8-9F9F-9373-D9B03A81E50F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_head1";
	rename -uid "562C1F17-4F4E-0E64-3694-51B5C712CE9E";
	setAttr ".sc" -type "float3" 0.18064517 0.18064517 0.18064517 ;
createNode file -n "Elisa_Model_file13";
	rename -uid "C83B9F4B-4B1C-49DE-C183-D6A1960BCE2A";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture13";
	rename -uid "9B9C1776-49B2-9D99-0DCA-DD8BC5C24BC8";
createNode shadingEngine -n "Elisa_Model_blinn3SG1";
	rename -uid "1D4B732F-4A76-C645-EAA7-9F9C753FE522";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo28";
	rename -uid "0108A9B0-491F-661C-7D36-F486E11D4634";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows2";
	rename -uid "7DBABB53-4EDE-0333-8573-4B84510F910F";
	setAttr ".c" -type "float3" 0.077200003 0.0605 0.0605 ;
createNode shadingEngine -n "Elisa_Model_blinn11SG1";
	rename -uid "3231AFE4-43D6-9CA5-567C-3EAA835E5AB5";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo32";
	rename -uid "00162E23-4285-72ED-885B-8EA0901F86EB";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash2";
	rename -uid "2B44FA19-4AE1-750A-51EE-9193AD6EB379";
	setAttr ".c" -type "float3" 0.068400003 0.045600001 0.045600001 ;
createNode shadingEngine -n "Elisa_Model_blinn8SG1";
	rename -uid "E036334B-44FD-DE48-0119-5AB4A4DB503D";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo30";
	rename -uid "B2A937D5-40CC-BF39-B6CD-FA8D947A1F4E";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow3";
	rename -uid "440FE577-47E3-2DB7-C840-40A14F170278";
	setAttr ".it" -type "float3" 1 1 1 ;
createNode shadingEngine -n "Elisa_Model_blinn12SG1";
	rename -uid "64A6915E-43EB-1096-920F-7A8EBC8C3E80";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo33";
	rename -uid "C8C4173E-4E26-DC1A-7C13-E3818275CB38";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears2";
	rename -uid "6AC76F02-4B84-53D7-54FA-5483F8F5A6C5";
	setAttr ".c" -type "float3" 0.3581 0.17550001 0.17550001 ;
	setAttr ".it" -type "float3" 0.43225807 0.43225807 0.43225807 ;
createNode shadingEngine -n "Elisa_Model_blinn5SG1";
	rename -uid "48F4EF28-4B68-3A2F-7A9C-ADB4CF2C07A9";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo29";
	rename -uid "B98621CB-40AB-7E03-F395-E48656E51385";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside2";
	rename -uid "6D04744D-4651-BF86-4B6B-B08FD13524DE";
	setAttr ".c" -type "float3" 0.41069999 0.18520001 0.18520001 ;
createNode renderLayerManager -n "Elisa_Model_renderLayerManager2";
	rename -uid "3D877521-40A8-3E11-FDDD-0CBE873A71B8";
createNode renderLayer -n "Elisa_Model_defaultRenderLayer2";
	rename -uid "4426B0E2-459C-6E0D-C521-9291DE25B27B";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager3";
	rename -uid "75F74550-4839-B4E0-83F7-AC9A0B6C63D4";
createNode renderLayer -n "defaultRenderLayer3";
	rename -uid "AF03F2C6-43EB-4610-0F7B-1FB7E9282681";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager4";
	rename -uid "69733C38-43D1-6C8C-4F5A-EF89E176A21E";
createNode renderLayer -n "defaultRenderLayer4";
	rename -uid "89686440-40C1-D533-BE43-6B8BA2DA2BFF";
	setAttr ".g" yes;
createNode renderLayerManager -n "Elisa_Model_renderLayerManager1";
	rename -uid "BB0C3421-4CF0-5989-2888-B2974878F231";
createNode renderLayer -n "Elisa_Model_defaultRenderLayer1";
	rename -uid "081ED2EF-4244-44D1-1AF9-42B480DB1429";
	setAttr ".g" yes;
createNode lambert -n "lambert6";
	rename -uid "5D419B2D-423C-F223-1377-6A8A018244C5";
	setAttr ".c" -type "float3" 0.2071 0.1015 0.1015 ;
createNode shadingEngine -n "lambert5SG1";
	rename -uid "44178415-4FC8-04FE-B7C9-0B9D59BD5778";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "0DE61596-48BB-9ED1-3CED-B08C0F526F7F";
createNode groupId -n "groupId2";
	rename -uid "92C0C9DC-49C0-E15D-FF72-648810456A28";
	setAttr ".ihi" 0;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "62D27176-4D2F-C4A7-0137-D08DD1D783A2";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -705.71428571428578 194.28571428571431 ;
	setAttr ".tgi[0].vh" -type "double2" 801.90476190476181 473.33333333333331 ;
createNode aiOptions -s -n "defaultArnoldRenderOptions";
	rename -uid "66CAC2F7-4494-87A3-96D7-12ABAB13E87D";
	addAttr -ci true -sn "ARV_options" -ln "ARV_options" -dt "string";
	setAttr ".AA_samples" 5;
	setAttr ".version" -type "string" "1.4.2.0";
	setAttr ".ARV_options" -type "string" "Display Settings=0;Show Status Bar=1;Display Pixel Information=0;3D Manipulation=0;Show AOVs list=1;Show Cameras list=1;Show RGBA icon=1;Show Crop Region icon=1;Show 3D Manipulation icon=0;Show Debug Shading icon=0;Show Exposure icon=1;Show Gamma icon=0;Darken Out-Of-Region=0;Show Render Tiles=0;AOVs=Beauty;Test Resolution=100%;Log=Last Progressive Step;Camera=frontShape;Save UI Threads=1;Debug Shading=Disabled;Color Management.Gamma=1;Color Management.Exposure=0;Background.BG=BG Color;Background.Color=0 0 0;Background.Image=;Background.Scale=1       1;Background.Offset=0       0;Background.Apply Color Management=1;Foreground.Enable FG=0;Foreground.Image=;Foreground.Scale=1       1;Foreground.Offset=0       0;Foreground.Apply Color Management=1;";
createNode aiAOVFilter -s -n "defaultArnoldFilter";
	rename -uid "8DD7C818-4D4F-DAD0-322A-68A82388266C";
	setAttr ".ai_translator" -type "string" "gaussian";
createNode aiAOVDriver -s -n "defaultArnoldDriver";
	rename -uid "B934DF38-4931-4195-CCF3-40849CE317F2";
	setAttr ".ai_translator" -type "string" "exr";
createNode aiAOVDriver -s -n "defaultArnoldDisplayDriver";
	rename -uid "2A02677E-4C44-4E5D-A5A2-1B9F937CE9B4";
	setAttr ".output_mode" 0;
	setAttr ".ai_translator" -type "string" "maya";
createNode expression -n "xgmRefreshPreview1";
	rename -uid "896A868A-43DC-FF55-B3F4-A18A2353CEDB";
	setAttr -k on ".nds";
	setAttr ".ixp" -type "string" "xgmPreview -r";
	setAttr ".uno" 1;
createNode renderLayerManager -n "renderLayerManager1";
	rename -uid "377B9714-4B2C-021D-9B4F-6A9CA72E94C7";
createNode renderLayer -n "defaultRenderLayer1";
	rename -uid "B8785580-49C3-638E-906B-D09D87B9E160";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager2";
	rename -uid "882D81D8-4BF3-E34C-1663-2AA74C20A4A6";
createNode renderLayer -n "defaultRenderLayer2";
	rename -uid "CCA42EE3-46F4-558E-3589-099782D1A904";
	setAttr ".g" yes;
createNode renderLayerManager -n "Elisa_Model_renderLayerManager";
	rename -uid "7E552153-4AF6-CC5C-F56D-80B55B768C8C";
createNode renderLayer -n "Elisa_Model_defaultRenderLayer";
	rename -uid "D0C76B00-4C42-E9A4-9B3E-ECB4FC6E0146";
	setAttr ".g" yes;
createNode lambert -n "lambert5";
	rename -uid "00BFD6B6-4C37-9F67-0B3D-238BFED316A3";
	setAttr ".c" -type "float3" 0.2071 0.1015 0.1015 ;
createNode shadingEngine -n "lambert5SG";
	rename -uid "633800D1-4E0E-7CE0-91C8-7187BAC00439";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "47252088-48D3-4A3C-B636-CAA3517958C9";
createNode groupId -n "groupId1";
	rename -uid "88523633-4E3A-6DB9-E3DC-65ADA60A72BD";
	setAttr ".ihi" 0;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "C6452811-4576-8A99-FE8F-85A87383B5F8";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -705.71428571428578 194.28571428571431 ;
	setAttr ".tgi[0].vh" -type "double2" 801.90476190476181 473.33333333333331 ;
createNode expression -n "xgmRefreshPreview";
	rename -uid "84DC64F0-43A2-0C60-083D-48B7788FAA29";
	setAttr -k on ".nds";
	setAttr ".ixp" -type "string" "xgmPreview -r";
	setAttr ".uno" 1;
createNode shadingEngine -n "yuheng_Model_lambert2SG";
	rename -uid "8CF584C1-49F6-B1E0-4DC5-929FBF1DF3C6";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr ".aal" -type "attributeAlias" {"ai_aov_diffuse_color","aiCustomAOVs[0]","ai_aov_direct_specular"
		,"aiCustomAOVs[1]","ai_aov_AO","aiCustomAOVs[2]","ai_aov_id_1","aiCustomAOVs[3]"} ;
createNode materialInfo -n "yuheng_Model_materialInfo17";
	rename -uid "F367D267-423B-5400-9C69-3E8F36574A48";
createNode lambert -n "yuheng_Model_head1";
	rename -uid "44966194-432A-0538-CD30-D69686BBAB87";
createNode file -n "yuheng_Model_file2";
	rename -uid "36A11E45-4AEB-33DD-E499-8AB2984985AC";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Yuheng/TEX/head_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "yuheng_Model_place2dTexture2";
	rename -uid "380327C7-48B9-F99F-4303-71B9FF5A5708";
createNode shadingEngine -n "yuheng_Model_lambert16SG";
	rename -uid "7E2281F6-49CB-0DD8-30DB-318B7BE67C60";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "yuheng_Model_materialInfo18";
	rename -uid "3F02E9E3-4E2E-A998-955A-16AF7DE523E7";
createNode lambert -n "yuheng_Model_lambert16";
	rename -uid "0B3560EB-404E-45BC-7E80-7B8550C9A474";
createNode shadingEngine -n "yuheng_Model_lambert10SG";
	rename -uid "6C9A94B4-4D5F-3B91-B9B1-358368164DAF";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr ".aal" -type "attributeAlias" {"ai_aov_diffuse_color","aiCustomAOVs[0]","ai_aov_direct_specular"
		,"aiCustomAOVs[1]","ai_aov_AO","aiCustomAOVs[2]","ai_aov_id_1","aiCustomAOVs[3]"} ;
createNode materialInfo -n "yuheng_Model_materialInfo11";
	rename -uid "AAD8795A-4F16-2B53-FEB9-C7B1D3DF2109";
createNode lambert -n "yuheng_Model_eye_occlusion_L1";
	rename -uid "09C362BD-4EF1-0BFA-E310-C89691036A5D";
createNode shadingEngine -n "yuheng_Model_lambert11SG";
	rename -uid "1DC886A2-4870-F858-85E0-F7B3B1C68D51";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr ".aal" -type "attributeAlias" {"ai_aov_diffuse_color","aiCustomAOVs[0]","ai_aov_direct_specular"
		,"aiCustomAOVs[1]","ai_aov_AO","aiCustomAOVs[2]","ai_aov_id_1","aiCustomAOVs[3]"} ;
createNode materialInfo -n "yuheng_Model_materialInfo12";
	rename -uid "008A9274-4077-9081-BB5F-E8A26351BC63";
createNode lambert -n "yuheng_Model_eye_occlusion_R1";
	rename -uid "0349E144-4F5B-DA28-8DD1-10B090192572";
createNode renderLayerManager -n "yuheng_Model_renderLayerManager";
	rename -uid "060FAE52-4919-F403-D499-15B01EB4EEA7";
createNode renderLayer -n "yuheng_Model_defaultRenderLayer";
	rename -uid "4FE0D616-4AFC-D30C-1AAB-4A9FF888DE38";
	setAttr ".g" yes;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 36 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 38 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 17 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 13 ".r";
select -ne :defaultTextureList1;
	setAttr -s 17 ".tx";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "Root.s" "C_Pelvis.is";
connectAttr "C_Pelvis.s" "C_Spine_0.is";
connectAttr "C_Spine_0.s" "C_Spine_1.is";
connectAttr "C_Spine_1.s" "C_Spine_2.is";
connectAttr "C_Spine_2.s" "C_Spine_3.is";
connectAttr "C_Spine_3.s" "C_ChestBegin.is";
connectAttr "C_ChestBegin.s" "C_ChestEnd.is";
connectAttr "C_ChestBegin.s" "C_Neck_0.is";
connectAttr "C_Neck_0.s" "C_Neck_1.is";
connectAttr "C_Neck_1.s" "C_Head.is";
connectAttr "C_Head.s" "C_FacialRoot.is";
connectAttr "C_FacialRoot.s" "R_Eye.is";
connectAttr "C_FacialRoot.s" "C_UpperTeeth.is";
connectAttr "C_FacialRoot.s" "R_EyelidUpper.is";
connectAttr "C_FacialRoot.s" "R_EyelidLower.is";
connectAttr "C_FacialRoot.s" "C_Jaw.is";
connectAttr "C_Jaw.s" "C_JawEnd.is";
connectAttr "C_Jaw.s" "C_LowerTeeth.is";
connectAttr "C_FacialRoot.s" "L_EyelidUpper.is";
connectAttr "C_FacialRoot.s" "L_Eye.is";
connectAttr "C_FacialRoot.s" "L_EyelidLower.is";
connectAttr "C_ChestBegin.s" "L_Breast.is";
connectAttr "C_ChestBegin.s" "L_Clav.is";
connectAttr "L_Clav.s" "L_Shoulder.is";
connectAttr "L_Shoulder.s" "L_Elbow.is";
connectAttr "L_Elbow.s" "L_Wrist.is";
connectAttr "L_Wrist.s" "L_Thumb_0.is";
connectAttr "L_Thumb_0.s" "L_Thumb_1.is";
connectAttr "L_Thumb_1.s" "L_Thumb_2.is";
connectAttr "L_Thumb_2.s" "L_Thumb_3.is";
connectAttr "L_Wrist.s" "L_Index_0.is";
connectAttr "L_Index_0.s" "L_Index_1.is";
connectAttr "L_Index_1.s" "L_Index_2.is";
connectAttr "L_Index_2.s" "L_Index_3.is";
connectAttr "L_Index_3.s" "L_Index_4.is";
connectAttr "L_Wrist.s" "L_Middle_0.is";
connectAttr "L_Middle_0.s" "L_Middle_1.is";
connectAttr "L_Middle_1.s" "L_Middle_2.is";
connectAttr "L_Middle_2.s" "L_Middle_3.is";
connectAttr "L_Middle_3.s" "L_Middle_4.is";
connectAttr "L_Wrist.s" "L_Ring_0.is";
connectAttr "L_Ring_0.s" "L_Ring_1.is";
connectAttr "L_Ring_1.s" "L_Ring_2.is";
connectAttr "L_Ring_2.s" "L_Ring_3.is";
connectAttr "L_Ring_3.s" "L_Ring_4.is";
connectAttr "L_Wrist.s" "L_Pinky_0.is";
connectAttr "L_Pinky_0.s" "L_Pinky_1.is";
connectAttr "L_Pinky_1.s" "L_Pinky_2.is";
connectAttr "L_Pinky_2.s" "L_Pinky_3.is";
connectAttr "L_Pinky_3.s" "L_Pinky_4.is";
connectAttr "C_ChestBegin.s" "R_Breast.is";
connectAttr "C_ChestBegin.s" "R_Clav.is";
connectAttr "R_Clav.s" "R_Shoulder.is";
connectAttr "R_Shoulder.s" "R_Elbow.is";
connectAttr "R_Elbow.s" "R_Wrist.is";
connectAttr "R_Wrist.s" "R_Thumb_0.is";
connectAttr "R_Thumb_0.s" "R_Thumb_1.is";
connectAttr "R_Thumb_1.s" "R_Thumb_2.is";
connectAttr "R_Thumb_2.s" "R_Thumb_3.is";
connectAttr "R_Wrist.s" "R_Index_0.is";
connectAttr "R_Index_0.s" "R_Index_1.is";
connectAttr "R_Index_1.s" "R_Index_2.is";
connectAttr "R_Index_2.s" "R_Index_3.is";
connectAttr "R_Index_3.s" "R_Index_4.is";
connectAttr "R_Wrist.s" "R_Middle_0.is";
connectAttr "R_Middle_0.s" "R_Middle_1.is";
connectAttr "R_Middle_1.s" "R_Middle_2.is";
connectAttr "R_Middle_2.s" "R_Middle_3.is";
connectAttr "R_Middle_3.s" "R_Middle_4.is";
connectAttr "R_Wrist.s" "R_Ring_0.is";
connectAttr "R_Ring_0.s" "R_Ring_1.is";
connectAttr "R_Ring_1.s" "R_Ring_2.is";
connectAttr "R_Ring_2.s" "R_Ring_3.is";
connectAttr "R_Ring_3.s" "R_Ring_4.is";
connectAttr "R_Wrist.s" "R_Pinky_0.is";
connectAttr "R_Pinky_0.s" "R_Pinky_1.is";
connectAttr "R_Pinky_1.s" "R_Pinky_2.is";
connectAttr "R_Pinky_2.s" "R_Pinky_3.is";
connectAttr "R_Pinky_3.s" "R_Pinky_4.is";
connectAttr "C_Pelvis.s" "L_Hip.is";
connectAttr "L_Hip.s" "L_Knee.is";
connectAttr "L_Knee.s" "L_Ankle.is";
connectAttr "L_Ankle.s" "L_Ball.is";
connectAttr "L_Ball.s" "L_Toe.is";
connectAttr "C_Pelvis.s" "R_Hip.is";
connectAttr "R_Hip.s" "R_Knee.is";
connectAttr "R_Knee.s" "R_Ankle.is";
connectAttr "R_Ankle.s" "R_Ball.is";
connectAttr "R_Ball.s" "R_Toe.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_polySurface846SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn8SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn10SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn11SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn12SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_bodySG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_head_SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn13SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes02_SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes01_SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_polySurface846SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn2SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn3SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn5SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn8SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn10SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn11SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn12SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_bodySG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_head_SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_blinn13SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes02_SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes01_SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert5SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert10SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert11SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert16SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_polySurface846SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn8SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn10SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn11SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn12SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_bodySG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_head_SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn13SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes02_SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes01_SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_polySurface846SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn2SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn3SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn5SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn8SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn10SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn11SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn12SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_bodySG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_head_SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_blinn13SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes02_SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Elisa_Model_Elisa_Duncan_clothes01_SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert10SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert11SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert16SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "file2.oc" "blinn1.c";
connectAttr "blinn1.oc" "blinn1SG.ss";
connectAttr "blinn1SG.msg" "materialInfo1.sg";
connectAttr "blinn1.msg" "materialInfo1.m";
connectAttr "file2.msg" "materialInfo1.t" -na;
connectAttr "file1.oc" "blinn2.c";
connectAttr "blinn2.oc" "blinn2SG.ss";
connectAttr "blinn2SG.msg" "materialInfo2.sg";
connectAttr "blinn2.msg" "materialInfo2.m";
connectAttr "file1.msg" "materialInfo2.t" -na;
connectAttr ":defaultColorMgtGlobals.cme" "file1.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file1.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file1.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file1.ws";
connectAttr "place2dTexture1.c" "file1.c";
connectAttr "place2dTexture1.tf" "file1.tf";
connectAttr "place2dTexture1.rf" "file1.rf";
connectAttr "place2dTexture1.mu" "file1.mu";
connectAttr "place2dTexture1.mv" "file1.mv";
connectAttr "place2dTexture1.s" "file1.s";
connectAttr "place2dTexture1.wu" "file1.wu";
connectAttr "place2dTexture1.wv" "file1.wv";
connectAttr "place2dTexture1.re" "file1.re";
connectAttr "place2dTexture1.of" "file1.of";
connectAttr "place2dTexture1.r" "file1.ro";
connectAttr "place2dTexture1.n" "file1.n";
connectAttr "place2dTexture1.vt1" "file1.vt1";
connectAttr "place2dTexture1.vt2" "file1.vt2";
connectAttr "place2dTexture1.vt3" "file1.vt3";
connectAttr "place2dTexture1.vc1" "file1.vc1";
connectAttr "place2dTexture1.o" "file1.uv";
connectAttr "place2dTexture1.ofs" "file1.fs";
connectAttr ":defaultColorMgtGlobals.cme" "file2.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file2.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file2.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file2.ws";
connectAttr "place2dTexture2.c" "file2.c";
connectAttr "place2dTexture2.tf" "file2.tf";
connectAttr "place2dTexture2.rf" "file2.rf";
connectAttr "place2dTexture2.mu" "file2.mu";
connectAttr "place2dTexture2.mv" "file2.mv";
connectAttr "place2dTexture2.s" "file2.s";
connectAttr "place2dTexture2.wu" "file2.wu";
connectAttr "place2dTexture2.wv" "file2.wv";
connectAttr "place2dTexture2.re" "file2.re";
connectAttr "place2dTexture2.of" "file2.of";
connectAttr "place2dTexture2.r" "file2.ro";
connectAttr "place2dTexture2.n" "file2.n";
connectAttr "place2dTexture2.vt1" "file2.vt1";
connectAttr "place2dTexture2.vt2" "file2.vt2";
connectAttr "place2dTexture2.vt3" "file2.vt3";
connectAttr "place2dTexture2.vc1" "file2.vc1";
connectAttr "place2dTexture2.o" "file2.uv";
connectAttr "place2dTexture2.ofs" "file2.fs";
connectAttr "pasted__renderLayerManager.rlmi[0]" "pasted__defaultRenderLayer.rlid"
		;
connectAttr "pasted__renderLayerManager1.rlmi[0]" "pasted__defaultRenderLayer1.rlid"
		;
connectAttr "pasted__pasted__renderLayerManager.rlmi[0]" "pasted__pasted__defaultRenderLayer.rlid"
		;
connectAttr "file2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "place2dTexture2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "renderLayerManager5.rlmi[0]" "defaultRenderLayer5.rlid";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body.oc" "Elisa_Model_Elisa_Duncan_bodySG.ss"
		;
connectAttr "Elisa_Model_Elisa_Duncan_bodySG.msg" "Elisa_Model_materialInfo19.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body.msg" "Elisa_Model_materialInfo19.m"
		;
connectAttr "Elisa_Model_file6.msg" "Elisa_Model_materialInfo19.t" -na;
connectAttr "Elisa_Model_file6.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body.c"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file6.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file6.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file6.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file6.ws";
connectAttr "Elisa_Model_place2dTexture6.c" "Elisa_Model_file6.c";
connectAttr "Elisa_Model_place2dTexture6.tf" "Elisa_Model_file6.tf";
connectAttr "Elisa_Model_place2dTexture6.rf" "Elisa_Model_file6.rf";
connectAttr "Elisa_Model_place2dTexture6.mu" "Elisa_Model_file6.mu";
connectAttr "Elisa_Model_place2dTexture6.mv" "Elisa_Model_file6.mv";
connectAttr "Elisa_Model_place2dTexture6.s" "Elisa_Model_file6.s";
connectAttr "Elisa_Model_place2dTexture6.wu" "Elisa_Model_file6.wu";
connectAttr "Elisa_Model_place2dTexture6.wv" "Elisa_Model_file6.wv";
connectAttr "Elisa_Model_place2dTexture6.re" "Elisa_Model_file6.re";
connectAttr "Elisa_Model_place2dTexture6.of" "Elisa_Model_file6.of";
connectAttr "Elisa_Model_place2dTexture6.r" "Elisa_Model_file6.ro";
connectAttr "Elisa_Model_place2dTexture6.n" "Elisa_Model_file6.n";
connectAttr "Elisa_Model_place2dTexture6.vt1" "Elisa_Model_file6.vt1";
connectAttr "Elisa_Model_place2dTexture6.vt2" "Elisa_Model_file6.vt2";
connectAttr "Elisa_Model_place2dTexture6.vt3" "Elisa_Model_file6.vt3";
connectAttr "Elisa_Model_place2dTexture6.vc1" "Elisa_Model_file6.vc1";
connectAttr "Elisa_Model_place2dTexture6.o" "Elisa_Model_file6.uv";
connectAttr "Elisa_Model_place2dTexture6.ofs" "Elisa_Model_file6.fs";
connectAttr "Elisa_Model_Elisa_Duncan_clothes01_SG.msg" "Elisa_Model_materialInfo24.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes03.msg" "Elisa_Model_materialInfo24.m"
		;
connectAttr "Elisa_Model_file9.msg" "Elisa_Model_materialInfo24.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes03.oc" "Elisa_Model_Elisa_Duncan_clothes01_SG.ss"
		;
connectAttr "Elisa_Model_file9.oc" "Elisa_Model_Elisa_Duncan_clothes03.c";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file9.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file9.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file9.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file9.ws";
connectAttr "Elisa_Model_place2dTexture9.c" "Elisa_Model_file9.c";
connectAttr "Elisa_Model_place2dTexture9.tf" "Elisa_Model_file9.tf";
connectAttr "Elisa_Model_place2dTexture9.rf" "Elisa_Model_file9.rf";
connectAttr "Elisa_Model_place2dTexture9.mu" "Elisa_Model_file9.mu";
connectAttr "Elisa_Model_place2dTexture9.mv" "Elisa_Model_file9.mv";
connectAttr "Elisa_Model_place2dTexture9.s" "Elisa_Model_file9.s";
connectAttr "Elisa_Model_place2dTexture9.wu" "Elisa_Model_file9.wu";
connectAttr "Elisa_Model_place2dTexture9.wv" "Elisa_Model_file9.wv";
connectAttr "Elisa_Model_place2dTexture9.re" "Elisa_Model_file9.re";
connectAttr "Elisa_Model_place2dTexture9.of" "Elisa_Model_file9.of";
connectAttr "Elisa_Model_place2dTexture9.r" "Elisa_Model_file9.ro";
connectAttr "Elisa_Model_place2dTexture9.n" "Elisa_Model_file9.n";
connectAttr "Elisa_Model_place2dTexture9.vt1" "Elisa_Model_file9.vt1";
connectAttr "Elisa_Model_place2dTexture9.vt2" "Elisa_Model_file9.vt2";
connectAttr "Elisa_Model_place2dTexture9.vt3" "Elisa_Model_file9.vt3";
connectAttr "Elisa_Model_place2dTexture9.vc1" "Elisa_Model_file9.vc1";
connectAttr "Elisa_Model_place2dTexture9.o" "Elisa_Model_file9.uv";
connectAttr "Elisa_Model_place2dTexture9.ofs" "Elisa_Model_file9.fs";
connectAttr "Elisa_Model_Elisa_Duncan_clothes02_SG.msg" "Elisa_Model_materialInfo25.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes04.msg" "Elisa_Model_materialInfo25.m"
		;
connectAttr "Elisa_Model_file8.msg" "Elisa_Model_materialInfo25.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes04.oc" "Elisa_Model_Elisa_Duncan_clothes02_SG.ss"
		;
connectAttr "Elisa_Model_file8.oc" "Elisa_Model_Elisa_Duncan_clothes04.c";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file8.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file8.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file8.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file8.ws";
connectAttr "Elisa_Model_place2dTexture8.c" "Elisa_Model_file8.c";
connectAttr "Elisa_Model_place2dTexture8.tf" "Elisa_Model_file8.tf";
connectAttr "Elisa_Model_place2dTexture8.rf" "Elisa_Model_file8.rf";
connectAttr "Elisa_Model_place2dTexture8.mu" "Elisa_Model_file8.mu";
connectAttr "Elisa_Model_place2dTexture8.mv" "Elisa_Model_file8.mv";
connectAttr "Elisa_Model_place2dTexture8.s" "Elisa_Model_file8.s";
connectAttr "Elisa_Model_place2dTexture8.wu" "Elisa_Model_file8.wu";
connectAttr "Elisa_Model_place2dTexture8.wv" "Elisa_Model_file8.wv";
connectAttr "Elisa_Model_place2dTexture8.re" "Elisa_Model_file8.re";
connectAttr "Elisa_Model_place2dTexture8.of" "Elisa_Model_file8.of";
connectAttr "Elisa_Model_place2dTexture8.r" "Elisa_Model_file8.ro";
connectAttr "Elisa_Model_place2dTexture8.n" "Elisa_Model_file8.n";
connectAttr "Elisa_Model_place2dTexture8.vt1" "Elisa_Model_file8.vt1";
connectAttr "Elisa_Model_place2dTexture8.vt2" "Elisa_Model_file8.vt2";
connectAttr "Elisa_Model_place2dTexture8.vt3" "Elisa_Model_file8.vt3";
connectAttr "Elisa_Model_place2dTexture8.vc1" "Elisa_Model_file8.vc1";
connectAttr "Elisa_Model_place2dTexture8.o" "Elisa_Model_file8.uv";
connectAttr "Elisa_Model_place2dTexture8.ofs" "Elisa_Model_file8.fs";
connectAttr "Elisa_Model_blinn13SG.msg" "Elisa_Model_materialInfo21.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Shoes1.msg" "Elisa_Model_materialInfo21.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Shoes1.oc" "Elisa_Model_blinn13SG.ss";
connectAttr "Elisa_Model_blinn10SG.msg" "Elisa_Model_materialInfo16.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth1.msg" "Elisa_Model_materialInfo16.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_file1.msg" "Elisa_Model_materialInfo16.t" 
		-na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth1.oc" "Elisa_Model_blinn10SG.ss"
		;
connectAttr "Elisa_Model_Elisa_Duncan_file1.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth1.c"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_Elisa_Duncan_file1.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_Elisa_Duncan_file1.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_Elisa_Duncan_file1.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_Elisa_Duncan_file1.ws";
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.c" "Elisa_Model_Elisa_Duncan_file1.c"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.tf" "Elisa_Model_Elisa_Duncan_file1.tf"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.rf" "Elisa_Model_Elisa_Duncan_file1.rf"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.mu" "Elisa_Model_Elisa_Duncan_file1.mu"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.mv" "Elisa_Model_Elisa_Duncan_file1.mv"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.s" "Elisa_Model_Elisa_Duncan_file1.s"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.wu" "Elisa_Model_Elisa_Duncan_file1.wu"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.wv" "Elisa_Model_Elisa_Duncan_file1.wv"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.re" "Elisa_Model_Elisa_Duncan_file1.re"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.of" "Elisa_Model_Elisa_Duncan_file1.of"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.r" "Elisa_Model_Elisa_Duncan_file1.ro"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.n" "Elisa_Model_Elisa_Duncan_file1.n"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.vt1" "Elisa_Model_Elisa_Duncan_file1.vt1"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.vt2" "Elisa_Model_Elisa_Duncan_file1.vt2"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.vt3" "Elisa_Model_Elisa_Duncan_file1.vt3"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.vc1" "Elisa_Model_Elisa_Duncan_file1.vc1"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.o" "Elisa_Model_Elisa_Duncan_file1.uv"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.ofs" "Elisa_Model_Elisa_Duncan_file1.fs"
		;
connectAttr "Elisa_Model_blinn2SG.msg" "Elisa_Model_materialInfo8.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye.msg" "Elisa_Model_materialInfo8.m"
		;
connectAttr "Elisa_Model_file5.msg" "Elisa_Model_materialInfo8.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye.oc" "Elisa_Model_blinn2SG.ss"
		;
connectAttr "Elisa_Model_file5.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye.c"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file5.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file5.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file5.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file5.ws";
connectAttr "Elisa_Model_place2dTexture5.c" "Elisa_Model_file5.c";
connectAttr "Elisa_Model_place2dTexture5.tf" "Elisa_Model_file5.tf";
connectAttr "Elisa_Model_place2dTexture5.rf" "Elisa_Model_file5.rf";
connectAttr "Elisa_Model_place2dTexture5.mu" "Elisa_Model_file5.mu";
connectAttr "Elisa_Model_place2dTexture5.mv" "Elisa_Model_file5.mv";
connectAttr "Elisa_Model_place2dTexture5.s" "Elisa_Model_file5.s";
connectAttr "Elisa_Model_place2dTexture5.wu" "Elisa_Model_file5.wu";
connectAttr "Elisa_Model_place2dTexture5.wv" "Elisa_Model_file5.wv";
connectAttr "Elisa_Model_place2dTexture5.re" "Elisa_Model_file5.re";
connectAttr "Elisa_Model_place2dTexture5.of" "Elisa_Model_file5.of";
connectAttr "Elisa_Model_place2dTexture5.r" "Elisa_Model_file5.ro";
connectAttr "Elisa_Model_place2dTexture5.n" "Elisa_Model_file5.n";
connectAttr "Elisa_Model_place2dTexture5.vt1" "Elisa_Model_file5.vt1";
connectAttr "Elisa_Model_place2dTexture5.vt2" "Elisa_Model_file5.vt2";
connectAttr "Elisa_Model_place2dTexture5.vt3" "Elisa_Model_file5.vt3";
connectAttr "Elisa_Model_place2dTexture5.vc1" "Elisa_Model_file5.vc1";
connectAttr "Elisa_Model_place2dTexture5.o" "Elisa_Model_file5.uv";
connectAttr "Elisa_Model_place2dTexture5.ofs" "Elisa_Model_file5.fs";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar.oc" "Elisa_Model_polySurface846SG.ss"
		;
connectAttr "Elisa_Model_polySurface846SG.msg" "Elisa_Model_materialInfo7.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar.msg" "Elisa_Model_materialInfo7.m"
		;
connectAttr "Elisa_Model_file4.msg" "Elisa_Model_materialInfo7.t" -na;
connectAttr "Elisa_Model_file4.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar.c"
		;
connectAttr "Elisa_Model_file4.ot" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar.it"
		;
connectAttr "Elisa_Model_place2dTexture4.o" "Elisa_Model_file4.uv";
connectAttr "Elisa_Model_place2dTexture4.ofu" "Elisa_Model_file4.ofu";
connectAttr "Elisa_Model_place2dTexture4.ofv" "Elisa_Model_file4.ofv";
connectAttr "Elisa_Model_place2dTexture4.rf" "Elisa_Model_file4.rf";
connectAttr "Elisa_Model_place2dTexture4.reu" "Elisa_Model_file4.reu";
connectAttr "Elisa_Model_place2dTexture4.rev" "Elisa_Model_file4.rev";
connectAttr "Elisa_Model_place2dTexture4.vt1" "Elisa_Model_file4.vt1";
connectAttr "Elisa_Model_place2dTexture4.vt2" "Elisa_Model_file4.vt2";
connectAttr "Elisa_Model_place2dTexture4.vt3" "Elisa_Model_file4.vt3";
connectAttr "Elisa_Model_place2dTexture4.vc1" "Elisa_Model_file4.vc1";
connectAttr "Elisa_Model_place2dTexture4.ofs" "Elisa_Model_file4.fs";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file4.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file4.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file4.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file4.ws";
connectAttr "Elisa_Model_Elisa_Duncan_head_SG.msg" "Elisa_Model_materialInfo20.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_head.msg" "Elisa_Model_materialInfo20.m";
connectAttr "Elisa_Model_file7.msg" "Elisa_Model_materialInfo20.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_head.oc" "Elisa_Model_Elisa_Duncan_head_SG.ss"
		;
connectAttr "Elisa_Model_file7.oc" "Elisa_Model_Elisa_Duncan_head.c";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file7.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file7.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file7.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file7.ws";
connectAttr "Elisa_Model_place2dTexture7.c" "Elisa_Model_file7.c";
connectAttr "Elisa_Model_place2dTexture7.tf" "Elisa_Model_file7.tf";
connectAttr "Elisa_Model_place2dTexture7.rf" "Elisa_Model_file7.rf";
connectAttr "Elisa_Model_place2dTexture7.mu" "Elisa_Model_file7.mu";
connectAttr "Elisa_Model_place2dTexture7.mv" "Elisa_Model_file7.mv";
connectAttr "Elisa_Model_place2dTexture7.s" "Elisa_Model_file7.s";
connectAttr "Elisa_Model_place2dTexture7.wu" "Elisa_Model_file7.wu";
connectAttr "Elisa_Model_place2dTexture7.wv" "Elisa_Model_file7.wv";
connectAttr "Elisa_Model_place2dTexture7.re" "Elisa_Model_file7.re";
connectAttr "Elisa_Model_place2dTexture7.of" "Elisa_Model_file7.of";
connectAttr "Elisa_Model_place2dTexture7.r" "Elisa_Model_file7.ro";
connectAttr "Elisa_Model_place2dTexture7.n" "Elisa_Model_file7.n";
connectAttr "Elisa_Model_place2dTexture7.vt1" "Elisa_Model_file7.vt1";
connectAttr "Elisa_Model_place2dTexture7.vt2" "Elisa_Model_file7.vt2";
connectAttr "Elisa_Model_place2dTexture7.vt3" "Elisa_Model_file7.vt3";
connectAttr "Elisa_Model_place2dTexture7.vc1" "Elisa_Model_file7.vc1";
connectAttr "Elisa_Model_place2dTexture7.o" "Elisa_Model_file7.uv";
connectAttr "Elisa_Model_place2dTexture7.ofs" "Elisa_Model_file7.fs";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows1.oc" "Elisa_Model_blinn3SG.ss"
		;
connectAttr "Elisa_Model_blinn3SG.msg" "Elisa_Model_materialInfo9.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows1.msg" "Elisa_Model_materialInfo9.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash1.oc" "Elisa_Model_blinn11SG.ss"
		;
connectAttr "Elisa_Model_blinn11SG.msg" "Elisa_Model_materialInfo17.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash1.msg" "Elisa_Model_materialInfo17.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow2.oc" "Elisa_Model_blinn8SG.ss"
		;
connectAttr "Elisa_Model_blinn8SG.msg" "Elisa_Model_materialInfo14.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow2.msg" "Elisa_Model_materialInfo14.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears1.oc" "Elisa_Model_blinn12SG.ss"
		;
connectAttr "Elisa_Model_blinn12SG.msg" "Elisa_Model_materialInfo18.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears1.msg" "Elisa_Model_materialInfo18.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside1.oc" "Elisa_Model_blinn5SG.ss"
		;
connectAttr "Elisa_Model_blinn5SG.msg" "Elisa_Model_materialInfo11.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside1.msg" "Elisa_Model_materialInfo11.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body1.oc" "Elisa_Model_Elisa_Duncan_bodySG1.ss"
		;
connectAttr "Elisa_Model_Elisa_Duncan_bodySG1.msg" "Elisa_Model_materialInfo34.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body1.msg" "Elisa_Model_materialInfo34.m"
		;
connectAttr "Elisa_Model_file12.msg" "Elisa_Model_materialInfo34.t" -na;
connectAttr "Elisa_Model_file12.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body1.c"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file12.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file12.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file12.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file12.ws";
connectAttr "Elisa_Model_place2dTexture12.c" "Elisa_Model_file12.c";
connectAttr "Elisa_Model_place2dTexture12.tf" "Elisa_Model_file12.tf";
connectAttr "Elisa_Model_place2dTexture12.rf" "Elisa_Model_file12.rf";
connectAttr "Elisa_Model_place2dTexture12.mu" "Elisa_Model_file12.mu";
connectAttr "Elisa_Model_place2dTexture12.mv" "Elisa_Model_file12.mv";
connectAttr "Elisa_Model_place2dTexture12.s" "Elisa_Model_file12.s";
connectAttr "Elisa_Model_place2dTexture12.wu" "Elisa_Model_file12.wu";
connectAttr "Elisa_Model_place2dTexture12.wv" "Elisa_Model_file12.wv";
connectAttr "Elisa_Model_place2dTexture12.re" "Elisa_Model_file12.re";
connectAttr "Elisa_Model_place2dTexture12.of" "Elisa_Model_file12.of";
connectAttr "Elisa_Model_place2dTexture12.r" "Elisa_Model_file12.ro";
connectAttr "Elisa_Model_place2dTexture12.n" "Elisa_Model_file12.n";
connectAttr "Elisa_Model_place2dTexture12.vt1" "Elisa_Model_file12.vt1";
connectAttr "Elisa_Model_place2dTexture12.vt2" "Elisa_Model_file12.vt2";
connectAttr "Elisa_Model_place2dTexture12.vt3" "Elisa_Model_file12.vt3";
connectAttr "Elisa_Model_place2dTexture12.vc1" "Elisa_Model_file12.vc1";
connectAttr "Elisa_Model_place2dTexture12.o" "Elisa_Model_file12.uv";
connectAttr "Elisa_Model_place2dTexture12.ofs" "Elisa_Model_file12.fs";
connectAttr "Elisa_Model_Elisa_Duncan_clothes01_SG1.msg" "Elisa_Model_materialInfo37.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes05.msg" "Elisa_Model_materialInfo37.m"
		;
connectAttr "Elisa_Model_file15.msg" "Elisa_Model_materialInfo37.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes05.oc" "Elisa_Model_Elisa_Duncan_clothes01_SG1.ss"
		;
connectAttr "Elisa_Model_file15.oc" "Elisa_Model_Elisa_Duncan_clothes05.c";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file15.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file15.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file15.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file15.ws";
connectAttr "Elisa_Model_place2dTexture15.c" "Elisa_Model_file15.c";
connectAttr "Elisa_Model_place2dTexture15.tf" "Elisa_Model_file15.tf";
connectAttr "Elisa_Model_place2dTexture15.rf" "Elisa_Model_file15.rf";
connectAttr "Elisa_Model_place2dTexture15.mu" "Elisa_Model_file15.mu";
connectAttr "Elisa_Model_place2dTexture15.mv" "Elisa_Model_file15.mv";
connectAttr "Elisa_Model_place2dTexture15.s" "Elisa_Model_file15.s";
connectAttr "Elisa_Model_place2dTexture15.wu" "Elisa_Model_file15.wu";
connectAttr "Elisa_Model_place2dTexture15.wv" "Elisa_Model_file15.wv";
connectAttr "Elisa_Model_place2dTexture15.re" "Elisa_Model_file15.re";
connectAttr "Elisa_Model_place2dTexture15.of" "Elisa_Model_file15.of";
connectAttr "Elisa_Model_place2dTexture15.r" "Elisa_Model_file15.ro";
connectAttr "Elisa_Model_place2dTexture15.n" "Elisa_Model_file15.n";
connectAttr "Elisa_Model_place2dTexture15.vt1" "Elisa_Model_file15.vt1";
connectAttr "Elisa_Model_place2dTexture15.vt2" "Elisa_Model_file15.vt2";
connectAttr "Elisa_Model_place2dTexture15.vt3" "Elisa_Model_file15.vt3";
connectAttr "Elisa_Model_place2dTexture15.vc1" "Elisa_Model_file15.vc1";
connectAttr "Elisa_Model_place2dTexture15.o" "Elisa_Model_file15.uv";
connectAttr "Elisa_Model_place2dTexture15.ofs" "Elisa_Model_file15.fs";
connectAttr "Elisa_Model_Elisa_Duncan_clothes02_SG1.msg" "Elisa_Model_materialInfo38.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes06.msg" "Elisa_Model_materialInfo38.m"
		;
connectAttr "Elisa_Model_file14.msg" "Elisa_Model_materialInfo38.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes06.oc" "Elisa_Model_Elisa_Duncan_clothes02_SG1.ss"
		;
connectAttr "Elisa_Model_file14.oc" "Elisa_Model_Elisa_Duncan_clothes06.c";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file14.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file14.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file14.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file14.ws";
connectAttr "Elisa_Model_place2dTexture14.c" "Elisa_Model_file14.c";
connectAttr "Elisa_Model_place2dTexture14.tf" "Elisa_Model_file14.tf";
connectAttr "Elisa_Model_place2dTexture14.rf" "Elisa_Model_file14.rf";
connectAttr "Elisa_Model_place2dTexture14.mu" "Elisa_Model_file14.mu";
connectAttr "Elisa_Model_place2dTexture14.mv" "Elisa_Model_file14.mv";
connectAttr "Elisa_Model_place2dTexture14.s" "Elisa_Model_file14.s";
connectAttr "Elisa_Model_place2dTexture14.wu" "Elisa_Model_file14.wu";
connectAttr "Elisa_Model_place2dTexture14.wv" "Elisa_Model_file14.wv";
connectAttr "Elisa_Model_place2dTexture14.re" "Elisa_Model_file14.re";
connectAttr "Elisa_Model_place2dTexture14.of" "Elisa_Model_file14.of";
connectAttr "Elisa_Model_place2dTexture14.r" "Elisa_Model_file14.ro";
connectAttr "Elisa_Model_place2dTexture14.n" "Elisa_Model_file14.n";
connectAttr "Elisa_Model_place2dTexture14.vt1" "Elisa_Model_file14.vt1";
connectAttr "Elisa_Model_place2dTexture14.vt2" "Elisa_Model_file14.vt2";
connectAttr "Elisa_Model_place2dTexture14.vt3" "Elisa_Model_file14.vt3";
connectAttr "Elisa_Model_place2dTexture14.vc1" "Elisa_Model_file14.vc1";
connectAttr "Elisa_Model_place2dTexture14.o" "Elisa_Model_file14.uv";
connectAttr "Elisa_Model_place2dTexture14.ofs" "Elisa_Model_file14.fs";
connectAttr "Elisa_Model_blinn13SG1.msg" "Elisa_Model_materialInfo36.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Shoes2.msg" "Elisa_Model_materialInfo36.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Shoes2.oc" "Elisa_Model_blinn13SG1.ss";
connectAttr "Elisa_Model_blinn10SG1.msg" "Elisa_Model_materialInfo31.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth2.msg" "Elisa_Model_materialInfo31.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_file2.msg" "Elisa_Model_materialInfo31.t" 
		-na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth2.oc" "Elisa_Model_blinn10SG1.ss"
		;
connectAttr "Elisa_Model_Elisa_Duncan_file2.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth2.c"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_Elisa_Duncan_file2.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_Elisa_Duncan_file2.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_Elisa_Duncan_file2.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_Elisa_Duncan_file2.ws";
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.c" "Elisa_Model_Elisa_Duncan_file2.c"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.tf" "Elisa_Model_Elisa_Duncan_file2.tf"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.rf" "Elisa_Model_Elisa_Duncan_file2.rf"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.mu" "Elisa_Model_Elisa_Duncan_file2.mu"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.mv" "Elisa_Model_Elisa_Duncan_file2.mv"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.s" "Elisa_Model_Elisa_Duncan_file2.s"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.wu" "Elisa_Model_Elisa_Duncan_file2.wu"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.wv" "Elisa_Model_Elisa_Duncan_file2.wv"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.re" "Elisa_Model_Elisa_Duncan_file2.re"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.of" "Elisa_Model_Elisa_Duncan_file2.of"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.r" "Elisa_Model_Elisa_Duncan_file2.ro"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.n" "Elisa_Model_Elisa_Duncan_file2.n"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.vt1" "Elisa_Model_Elisa_Duncan_file2.vt1"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.vt2" "Elisa_Model_Elisa_Duncan_file2.vt2"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.vt3" "Elisa_Model_Elisa_Duncan_file2.vt3"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.vc1" "Elisa_Model_Elisa_Duncan_file2.vc1"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.o" "Elisa_Model_Elisa_Duncan_file2.uv"
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.ofs" "Elisa_Model_Elisa_Duncan_file2.fs"
		;
connectAttr "Elisa_Model_blinn2SG1.msg" "Elisa_Model_materialInfo27.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye1.msg" "Elisa_Model_materialInfo27.m"
		;
connectAttr "Elisa_Model_file11.msg" "Elisa_Model_materialInfo27.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye1.oc" "Elisa_Model_blinn2SG1.ss"
		;
connectAttr "Elisa_Model_file11.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye1.c"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file11.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file11.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file11.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file11.ws";
connectAttr "Elisa_Model_place2dTexture11.c" "Elisa_Model_file11.c";
connectAttr "Elisa_Model_place2dTexture11.tf" "Elisa_Model_file11.tf";
connectAttr "Elisa_Model_place2dTexture11.rf" "Elisa_Model_file11.rf";
connectAttr "Elisa_Model_place2dTexture11.mu" "Elisa_Model_file11.mu";
connectAttr "Elisa_Model_place2dTexture11.mv" "Elisa_Model_file11.mv";
connectAttr "Elisa_Model_place2dTexture11.s" "Elisa_Model_file11.s";
connectAttr "Elisa_Model_place2dTexture11.wu" "Elisa_Model_file11.wu";
connectAttr "Elisa_Model_place2dTexture11.wv" "Elisa_Model_file11.wv";
connectAttr "Elisa_Model_place2dTexture11.re" "Elisa_Model_file11.re";
connectAttr "Elisa_Model_place2dTexture11.of" "Elisa_Model_file11.of";
connectAttr "Elisa_Model_place2dTexture11.r" "Elisa_Model_file11.ro";
connectAttr "Elisa_Model_place2dTexture11.n" "Elisa_Model_file11.n";
connectAttr "Elisa_Model_place2dTexture11.vt1" "Elisa_Model_file11.vt1";
connectAttr "Elisa_Model_place2dTexture11.vt2" "Elisa_Model_file11.vt2";
connectAttr "Elisa_Model_place2dTexture11.vt3" "Elisa_Model_file11.vt3";
connectAttr "Elisa_Model_place2dTexture11.vc1" "Elisa_Model_file11.vc1";
connectAttr "Elisa_Model_place2dTexture11.o" "Elisa_Model_file11.uv";
connectAttr "Elisa_Model_place2dTexture11.ofs" "Elisa_Model_file11.fs";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar1.oc" "Elisa_Model_polySurface846SG1.ss"
		;
connectAttr "Elisa_Model_polySurface846SG1.msg" "Elisa_Model_materialInfo26.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar1.msg" "Elisa_Model_materialInfo26.m"
		;
connectAttr "Elisa_Model_file10.msg" "Elisa_Model_materialInfo26.t" -na;
connectAttr "Elisa_Model_file10.oc" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar1.c"
		;
connectAttr "Elisa_Model_file10.ot" "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar1.it"
		;
connectAttr "Elisa_Model_place2dTexture10.o" "Elisa_Model_file10.uv";
connectAttr "Elisa_Model_place2dTexture10.ofu" "Elisa_Model_file10.ofu";
connectAttr "Elisa_Model_place2dTexture10.ofv" "Elisa_Model_file10.ofv";
connectAttr "Elisa_Model_place2dTexture10.rf" "Elisa_Model_file10.rf";
connectAttr "Elisa_Model_place2dTexture10.reu" "Elisa_Model_file10.reu";
connectAttr "Elisa_Model_place2dTexture10.rev" "Elisa_Model_file10.rev";
connectAttr "Elisa_Model_place2dTexture10.vt1" "Elisa_Model_file10.vt1";
connectAttr "Elisa_Model_place2dTexture10.vt2" "Elisa_Model_file10.vt2";
connectAttr "Elisa_Model_place2dTexture10.vt3" "Elisa_Model_file10.vt3";
connectAttr "Elisa_Model_place2dTexture10.vc1" "Elisa_Model_file10.vc1";
connectAttr "Elisa_Model_place2dTexture10.ofs" "Elisa_Model_file10.fs";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file10.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file10.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file10.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file10.ws";
connectAttr "Elisa_Model_Elisa_Duncan_head_SG1.msg" "Elisa_Model_materialInfo35.sg"
		;
connectAttr "Elisa_Model_Elisa_Duncan_head1.msg" "Elisa_Model_materialInfo35.m";
connectAttr "Elisa_Model_file13.msg" "Elisa_Model_materialInfo35.t" -na;
connectAttr "Elisa_Model_Elisa_Duncan_head1.oc" "Elisa_Model_Elisa_Duncan_head_SG1.ss"
		;
connectAttr "Elisa_Model_file13.oc" "Elisa_Model_Elisa_Duncan_head1.c";
connectAttr ":defaultColorMgtGlobals.cme" "Elisa_Model_file13.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "Elisa_Model_file13.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "Elisa_Model_file13.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "Elisa_Model_file13.ws";
connectAttr "Elisa_Model_place2dTexture13.c" "Elisa_Model_file13.c";
connectAttr "Elisa_Model_place2dTexture13.tf" "Elisa_Model_file13.tf";
connectAttr "Elisa_Model_place2dTexture13.rf" "Elisa_Model_file13.rf";
connectAttr "Elisa_Model_place2dTexture13.mu" "Elisa_Model_file13.mu";
connectAttr "Elisa_Model_place2dTexture13.mv" "Elisa_Model_file13.mv";
connectAttr "Elisa_Model_place2dTexture13.s" "Elisa_Model_file13.s";
connectAttr "Elisa_Model_place2dTexture13.wu" "Elisa_Model_file13.wu";
connectAttr "Elisa_Model_place2dTexture13.wv" "Elisa_Model_file13.wv";
connectAttr "Elisa_Model_place2dTexture13.re" "Elisa_Model_file13.re";
connectAttr "Elisa_Model_place2dTexture13.of" "Elisa_Model_file13.of";
connectAttr "Elisa_Model_place2dTexture13.r" "Elisa_Model_file13.ro";
connectAttr "Elisa_Model_place2dTexture13.n" "Elisa_Model_file13.n";
connectAttr "Elisa_Model_place2dTexture13.vt1" "Elisa_Model_file13.vt1";
connectAttr "Elisa_Model_place2dTexture13.vt2" "Elisa_Model_file13.vt2";
connectAttr "Elisa_Model_place2dTexture13.vt3" "Elisa_Model_file13.vt3";
connectAttr "Elisa_Model_place2dTexture13.vc1" "Elisa_Model_file13.vc1";
connectAttr "Elisa_Model_place2dTexture13.o" "Elisa_Model_file13.uv";
connectAttr "Elisa_Model_place2dTexture13.ofs" "Elisa_Model_file13.fs";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows2.oc" "Elisa_Model_blinn3SG1.ss"
		;
connectAttr "Elisa_Model_blinn3SG1.msg" "Elisa_Model_materialInfo28.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows2.msg" "Elisa_Model_materialInfo28.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash2.oc" "Elisa_Model_blinn11SG1.ss"
		;
connectAttr "Elisa_Model_blinn11SG1.msg" "Elisa_Model_materialInfo32.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash2.msg" "Elisa_Model_materialInfo32.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow3.oc" "Elisa_Model_blinn8SG1.ss"
		;
connectAttr "Elisa_Model_blinn8SG1.msg" "Elisa_Model_materialInfo30.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow3.msg" "Elisa_Model_materialInfo30.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears2.oc" "Elisa_Model_blinn12SG1.ss"
		;
connectAttr "Elisa_Model_blinn12SG1.msg" "Elisa_Model_materialInfo33.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears2.msg" "Elisa_Model_materialInfo33.m"
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside2.oc" "Elisa_Model_blinn5SG1.ss"
		;
connectAttr "Elisa_Model_blinn5SG1.msg" "Elisa_Model_materialInfo29.sg";
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside2.msg" "Elisa_Model_materialInfo29.m"
		;
connectAttr "Elisa_Model_renderLayerManager2.rlmi[0]" "Elisa_Model_defaultRenderLayer2.rlid"
		;
connectAttr "renderLayerManager3.rlmi[0]" "defaultRenderLayer3.rlid";
connectAttr "renderLayerManager4.rlmi[0]" "defaultRenderLayer4.rlid";
connectAttr "Elisa_Model_renderLayerManager1.rlmi[0]" "Elisa_Model_defaultRenderLayer1.rlid"
		;
connectAttr "lambert6.oc" "lambert5SG1.ss";
connectAttr "groupId2.msg" "lambert5SG1.gn" -na;
connectAttr "lambert5SG1.msg" "materialInfo5.sg";
connectAttr "lambert6.msg" "materialInfo5.m";
connectAttr ":time1.o" "xgmRefreshPreview1.tim";
connectAttr "renderLayerManager1.rlmi[0]" "defaultRenderLayer1.rlid";
connectAttr "renderLayerManager2.rlmi[0]" "defaultRenderLayer2.rlid";
connectAttr "Elisa_Model_renderLayerManager.rlmi[0]" "Elisa_Model_defaultRenderLayer.rlid"
		;
connectAttr "lambert5.oc" "lambert5SG.ss";
connectAttr "groupId1.msg" "lambert5SG.gn" -na;
connectAttr "lambert5SG.msg" "materialInfo4.sg";
connectAttr "lambert5.msg" "materialInfo4.m";
connectAttr ":time1.o" "xgmRefreshPreview.tim";
connectAttr "yuheng_Model_head1.oc" "yuheng_Model_lambert2SG.ss";
connectAttr "yuheng_Model_lambert2SG.msg" "yuheng_Model_materialInfo17.sg";
connectAttr "yuheng_Model_head1.msg" "yuheng_Model_materialInfo17.m";
connectAttr "yuheng_Model_file2.msg" "yuheng_Model_materialInfo17.t" -na;
connectAttr "yuheng_Model_file2.oc" "yuheng_Model_head1.c";
connectAttr ":defaultColorMgtGlobals.cme" "yuheng_Model_file2.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "yuheng_Model_file2.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "yuheng_Model_file2.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "yuheng_Model_file2.ws";
connectAttr "yuheng_Model_place2dTexture2.c" "yuheng_Model_file2.c";
connectAttr "yuheng_Model_place2dTexture2.tf" "yuheng_Model_file2.tf";
connectAttr "yuheng_Model_place2dTexture2.rf" "yuheng_Model_file2.rf";
connectAttr "yuheng_Model_place2dTexture2.mu" "yuheng_Model_file2.mu";
connectAttr "yuheng_Model_place2dTexture2.mv" "yuheng_Model_file2.mv";
connectAttr "yuheng_Model_place2dTexture2.s" "yuheng_Model_file2.s";
connectAttr "yuheng_Model_place2dTexture2.wu" "yuheng_Model_file2.wu";
connectAttr "yuheng_Model_place2dTexture2.wv" "yuheng_Model_file2.wv";
connectAttr "yuheng_Model_place2dTexture2.re" "yuheng_Model_file2.re";
connectAttr "yuheng_Model_place2dTexture2.of" "yuheng_Model_file2.of";
connectAttr "yuheng_Model_place2dTexture2.r" "yuheng_Model_file2.ro";
connectAttr "yuheng_Model_place2dTexture2.n" "yuheng_Model_file2.n";
connectAttr "yuheng_Model_place2dTexture2.vt1" "yuheng_Model_file2.vt1";
connectAttr "yuheng_Model_place2dTexture2.vt2" "yuheng_Model_file2.vt2";
connectAttr "yuheng_Model_place2dTexture2.vt3" "yuheng_Model_file2.vt3";
connectAttr "yuheng_Model_place2dTexture2.vc1" "yuheng_Model_file2.vc1";
connectAttr "yuheng_Model_place2dTexture2.o" "yuheng_Model_file2.uv";
connectAttr "yuheng_Model_place2dTexture2.ofs" "yuheng_Model_file2.fs";
connectAttr "yuheng_Model_lambert16.oc" "yuheng_Model_lambert16SG.ss";
connectAttr "yuheng_Model_lambert16SG.msg" "yuheng_Model_materialInfo18.sg";
connectAttr "yuheng_Model_lambert16.msg" "yuheng_Model_materialInfo18.m";
connectAttr "yuheng_Model_eye_occlusion_L1.oc" "yuheng_Model_lambert10SG.ss";
connectAttr "yuheng_Model_lambert10SG.msg" "yuheng_Model_materialInfo11.sg";
connectAttr "yuheng_Model_eye_occlusion_L1.msg" "yuheng_Model_materialInfo11.m";
connectAttr "yuheng_Model_eye_occlusion_R1.oc" "yuheng_Model_lambert11SG.ss";
connectAttr "yuheng_Model_lambert11SG.msg" "yuheng_Model_materialInfo12.sg";
connectAttr "yuheng_Model_eye_occlusion_R1.msg" "yuheng_Model_materialInfo12.m";
connectAttr "yuheng_Model_renderLayerManager.rlmi[0]" "yuheng_Model_defaultRenderLayer.rlid"
		;
connectAttr "blinn1SG.pa" ":renderPartition.st" -na;
connectAttr "blinn2SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_polySurface846SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn2SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn3SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn5SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn8SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn10SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn11SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn12SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_Elisa_Duncan_bodySG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_Elisa_Duncan_head_SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn13SG.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes01_SG.pa" ":renderPartition.st" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes02_SG.pa" ":renderPartition.st" -na
		;
connectAttr "Elisa_Model_polySurface846SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn2SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn3SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn5SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn8SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn10SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn11SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn12SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_Elisa_Duncan_bodySG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_Elisa_Duncan_head_SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_blinn13SG1.pa" ":renderPartition.st" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes01_SG1.pa" ":renderPartition.st" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes02_SG1.pa" ":renderPartition.st" -na
		;
connectAttr "lambert5SG1.pa" ":renderPartition.st" -na;
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert10SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert11SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert16SG.pa" ":renderPartition.st" -na;
connectAttr "blinn1.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn2.msg" ":defaultShaderList1.s" -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow2.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_head.msg" ":defaultShaderList1.s" -na;
connectAttr "Elisa_Model_Elisa_Duncan_Shoes1.msg" ":defaultShaderList1.s" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes03.msg" ":defaultShaderList1.s" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes04.msg" ":defaultShaderList1.s" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows2.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside2.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow3.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth2.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash2.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears2.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body1.msg" ":defaultShaderList1.s"
		 -na;
connectAttr "Elisa_Model_Elisa_Duncan_head1.msg" ":defaultShaderList1.s" -na;
connectAttr "Elisa_Model_Elisa_Duncan_Shoes2.msg" ":defaultShaderList1.s" -na;
connectAttr "Elisa_Model_Elisa_Duncan_clothes05.msg" ":defaultShaderList1.s" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_clothes06.msg" ":defaultShaderList1.s" -na
		;
connectAttr "lambert6.msg" ":defaultShaderList1.s" -na;
connectAttr "lambert5.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_head1.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_eye_occlusion_L1.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_eye_occlusion_R1.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_lambert16.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Elisa_Model_place2dTexture4.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture5.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture6.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "Elisa_Model_place2dTexture7.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture8.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture9.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture10.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture11.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture12.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_Elisa_Duncan_place2dTexture2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "Elisa_Model_place2dTexture13.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture14.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "Elisa_Model_place2dTexture15.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "yuheng_Model_place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pasted__defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pasted__defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na;
connectAttr "pasted__pasted__defaultRenderLayer.msg" ":defaultRenderingList1.r" 
		-na;
connectAttr "defaultRenderLayer5.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_defaultRenderLayer2.msg" ":defaultRenderingList1.r" -na
		;
connectAttr "defaultRenderLayer3.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer4.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na
		;
connectAttr "defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer2.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "yuheng_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na
		;
connectAttr "file1.msg" ":defaultTextureList1.tx" -na;
connectAttr "file2.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file4.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file5.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file6.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_Elisa_Duncan_file1.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file7.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file8.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file9.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file10.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file11.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file12.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_Elisa_Duncan_file2.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file13.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file14.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file15.msg" ":defaultTextureList1.tx" -na;
connectAttr "yuheng_Model_file2.msg" ":defaultTextureList1.tx" -na;
// End of Danli_Builder.ma
