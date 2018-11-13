//Maya ASCII 2017ff04 scene
//Name: yuheng_Builder.ma
//Last modified: Tue, Nov 13, 2018 12:25:54 PM
//Codeset: 936
requires maya "2017ff04";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" "mtoa" "1.4.2.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "07AB0971-4B77-B354-F149-63B57479E140";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 93.795952114604944 245.74997998893457 413.5977211882394 ;
	setAttr ".r" -type "double3" -739.53835272913295 1450.9999999971474 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "37E79B49-4D88-AD95-3176-7AAB2D8B48DF";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 453.56981934767481;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 32.845392227172852 119.70576477050781 0.83054208755493164 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "E15EF9D6-4A06-1194-5582-73BBEB3636EF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 19.6347370176473 1000.1 7.6540462355225891 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "84DC2AAB-4460-DB72-509B-38A020E2F34F";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 160.26012844058255;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "28AA9790-450E-B0EE-A2A2-8D9A51DE304F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 34.732106557699289 117.44564366081045 1005.7264074867893 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "4F79D5EA-4741-7C4C-C1E4-878A9E3356B4";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1004.8958653992344;
	setAttr ".ow" 38.363504625112995;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 32.845392227172852 119.70576477050781 0.83054208755493164 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "DF59D432-4FBC-002C-4A72-D192C08455C0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1015.9954989408004 114.1778965735118 2.5129271366540125 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "69D84B1C-4344-0BC2-378D-8EBEF417377A";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 966.49097643806306;
	setAttr ".ow" 351.80979913152743;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 49.504522502737089 130.51192296176129 0 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "yuheng_BuilderGrp";
	rename -uid "A58DDA76-4DFA-1588-B990-85A888C0BD76";
createNode joint -n "Root" -p "yuheng_BuilderGrp";
	rename -uid "4E6FE928-44B3-2C60-646E-DCAD55CE8C63";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ds" 2;
	setAttr ".sd" 2;
	setAttr ".radi" 0.5;
createNode joint -n "C_Pelvis" -p "Root";
	rename -uid "47DD0C9B-4841-11E6-0FFA-EB8365772456";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".t" -type "double3" -6.4402427417810059e-015 93.398086968732912 0.59933287275722091 ;
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
	rename -uid "9BBF47BC-4C06-7247-E405-7595A52809FE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.3787305403828327 0.60942047346264872 1.5843296013841049e-015 ;
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
	rename -uid "0DA7792C-4C7B-D767-9631-75A1810B937D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 6.4203603642199027 0.38715298980249457 1.0470039788961871e-015 ;
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
	rename -uid "61C576FF-41F5-A9C8-37E1-32ABFEE9C34B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 6.3864127027999018 0.32010932412675475 1.7895599235603263e-015 ;
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
	rename -uid "BBB65849-4380-11CB-212B-109D3A9E9589";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 6.3906709693811479 0.42026509836729353 9.7197115565775901e-016 ;
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
	rename -uid "5A7E57C9-47CD-CD74-E7F1-BA8647E0A41B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 6.3197135745372321 0.16150953442166482 2.7961066435461745e-015 ;
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
	rename -uid "8852447C-4F5C-387A-8D13-B285B29DACCD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 24.982799786620689 0.56312315721186224 6.2001349847919442e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 6.0480597069556706e-017 0.98017587611435708 -0.19812938167634997 0
		 -3.957012367318657e-016 -0.19812938167635016 -0.9801758761143573 0 -1.0000000000000002 2.2204460492503136e-016 3.3306690738754696e-016 0
		 -1.360977951735926e-014 150.15467294050094 -5.3054764838503967 1;
	setAttr ".radi" 0.65517241379310198;
createNode joint -n "C_Neck_0" -p "C_ChestBegin";
	rename -uid "260459C7-4970-990B-0949-39B95AB258CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 21.286880880813925 -0.8166567793168813 8.5511916488399301e-015 ;
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
	rename -uid "9F87F5D6-4EC5-D622-7663-E7B149E79D6E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 6.2677104264477066 0.0032338366333561908 -9.3882819426884017e-017 ;
	setAttr ".r" -type "double3" 0 0 4.1744780194208675e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 1.7369994155771411 ;
	setAttr ".bps" -type "matrix" 3.9774202365524855e-016 0.99420750314017159 0.10747762883403142 0
		 -3.8723387470698558e-016 0.10747762883403147 -0.99420750314017159 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -3.2692166900159024e-015 156.60143909637154 -5.0157247189066902 1;
	setAttr ".typ" 7;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Head" -p "C_Neck_1";
	rename -uid "354E3E5C-4EF4-3056-AAC5-32853150E261";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 6.9690010031211784 0.18505591415991063 1.7995867559365028e-016 ;
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
	rename -uid "F7BDD0DB-4059-F737-4FDF-1A8250576489";
	setAttr ".t" -type "double3" 3.898190029754744 -0.4066310958194812 -9.4046668144994989e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.9837095073778706 27.927043278189814 -63.230731446679862 ;
	setAttr ".radi" 1.169502703832018;
createNode joint -n "R_Eye" -p "C_FacialRoot";
	rename -uid "D96F951A-4B27-4E11-BE1E-56ADA417778B";
	setAttr ".t" -type "double3" 5.9305218822887582 0.62872820600398427 6.7464823535338168 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_UpperTeeth" -p "C_FacialRoot";
	rename -uid "53B4410E-4BB8-4A61-36B6-ABA350C449AE";
	setAttr ".t" -type "double3" 3.1649558235444957 -5.6585343358166824 2.6995598859721417 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidUpper" -p "C_FacialRoot";
	rename -uid "28C14202-4144-D2F4-193C-7B898ECF1A94";
	setAttr ".t" -type "double3" 6.2601165037496997 1.287114638225006 6.811720469259698 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidLower" -p "C_FacialRoot";
	rename -uid "26532AF3-46D8-68BF-DBAD-5D952D536807";
	setAttr ".t" -type "double3" 5.6486796363346201 0.2200399705023699 6.6652246566720406 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_Jaw" -p "C_FacialRoot";
	rename -uid "E076E946-47FD-0BDE-025D-58AE7B75A16F";
	setAttr ".t" -type "double3" -0.014036996024344717 -2.4693314836871991 0.42744138140171284 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 13.071002108670072 60.477845958002632 -18.110959232148456 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_JawEnd" -p "C_Jaw";
	rename -uid "7D1BE41E-42D6-7673-8912-9F878BFF89D5";
	setAttr ".t" -type "double3" 1.5602265573261276e-014 -2.3690434981274109 8.255964691108904 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_LowerTeeth" -p "C_Jaw";
	rename -uid "D5AE60C6-4A37-2134-21D4-539F7FA8ADFC";
	setAttr ".t" -type "double3" 1.2961799602390078e-014 -1.9100451628799817 5.0176723933428136 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -7.5549687203861124e-014 -9.5416640443905503e-015 
		-2.1946285137169665e-017 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidUpper" -p "C_FacialRoot";
	rename -uid "5EBA17CE-4340-F7D7-7420-C098B1C80588";
	setAttr ".t" -type "double3" 9.250531793931728 0.30903034378306415 1.2555673209580673 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_Eye" -p "C_FacialRoot";
	rename -uid "E115AC65-41C2-FF98-F685-50B96B5513B9";
	setAttr ".t" -type "double3" 8.9178462520961688 -0.34863292938521795 1.1960127083801586 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidLower" -p "C_FacialRoot";
	rename -uid "E642C18F-4435-09DD-2FB5-C4B2053E1FFC";
	setAttr ".t" -type "double3" 8.6348596503930821 -0.75673026627671902 1.1170459243598527 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_Breast" -p "C_ChestBegin";
	rename -uid "A3738DC7-44CB-34D6-FA14-86997475DC0F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.98408701652054731 -10.184152160165752 11.288697328051672 ;
	setAttr ".r" -type "double3" 1.2424041724466862e-017 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -78.57240836108889 89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" 1 1.1542575317290093e-016 -4.5543866415314589e-016 0
		 8.9978394366786654e-017 -0.99999976735171558 -0.00068212646580104175 0 -4.2749774439139096e-016 0.00068212646580120828 -0.99999976735171558 0
		 -7.8906599999999987 133.34433177133462 7.0608686229479503 1;
	setAttr ".radi" 0.5;
createNode joint -n "L_Breast" -p "C_ChestBegin";
	rename -uid "D50B3A22-458B-00FC-EA00-838DDB908DD0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.98374068365887979 -10.184124897518728 -11.288700000000018 ;
	setAttr ".r" -type "double3" 1.2424041724466862e-017 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 101.42759163891114 89.999999999999972 0 ;
	setAttr ".bps" -type "matrix" 1 1.1542575317290093e-016 -4.5543866415314589e-016 0
		 8.9978394366786654e-017 -0.99999976735171558 -0.00068212646580104175 0 -4.2749774439139096e-016 0.00068212646580120828 -0.99999976735171558 0
		 -7.8906599999999987 133.34433177133462 7.0608686229479503 1;
	setAttr ".radi" 0.5;
createNode joint -n "L_Clav" -p "C_ChestBegin";
	rename -uid "1241B52E-425A-71AA-7E51-2590E54B10B0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 16.780734928456468 -1.8864758942646755 -3.4306400000000163 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -155.63744465115934 83.689332346217242 103.06608621941091 ;
	setAttr ".bps" -type "matrix" 0.97096663178489051 0.21828050916169012 0.097864290118605174 0
		 0.21724984896944344 -0.97588583281488517 0.021197745963948203 0 0.10013142904732321 0.00067869824772238128 -0.99497398774321211 0
		 -1.5920100000000004 148.55822219678041 -4.5013362696721906 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "L_Shoulder" -p "L_Clav";
	rename -uid "EE362B46-49D9-CF69-C122-4B800F1FFFEF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 11.59277376097323 -0.4472884611886343 -2.9729541150490988 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.8354150615638596 -11.293643790753313 -47.495974843215336 ;
	setAttr ".bps" -type "matrix" 0.26235226505945086 0.96470156178127819 -0.022851383217186154 0
		 0.96011801640670313 -0.26333161408024858 -0.093967311322336461 0 -0.096667903615593617 0.0027125122403274561 -0.99531299533760365 0
		 -15.337299999999994 145.46816650143637 -5.8867444007556049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "L_Elbow" -p "L_Shoulder";
	rename -uid "6A9548DC-478D-9CC4-5202-16B5E8DEB6F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 31.978322010787195 -2.8421709430404007e-014 1.7763568394002505e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -15.150734866123553 0 ;
	setAttr ".bps" -type "matrix" 0.43389320214860133 0.85690266771633017 -0.27830649864828944 0
		 0.46157048511156973 -0.47669839186407365 -0.74813857704844777 0 -0.77375020284527474 0.19615417725565557 -0.60235717173621639 0
		 -22.884002750078423 117.71811015626857 -5.2294136802891966 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "L_Wrist" -p "L_Elbow";
	rename -uid "B7492F34-46F6-817A-4BC3-D992478721D6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 26.190019445345882 1.4210854715202004e-014 3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.64018042213233828 -3.4169433382744234 -16.056435375520909 ;
	setAttr ".bps" -type "matrix" 0.42895584361388206 0.86277461858135351 -0.26761323166335294 0
		 0.46607536049615472 -0.46516195703129459 -0.75259425460814888 0 -0.77380271553405833 0.19810176996336093 -0.60165193107768 0
		 -33.622499955472293 96.510213366543951 1.6584548023795049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "L_Index_0" -p "L_Wrist";
	rename -uid "BAB337A4-4E55-5832-EA95-168372550254";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.9873017743315771 -0.43101485137687234 1.0572581567876185 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -165.73014377735865 -12.922429796688402 2.2526707268111621 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_1" -p "L_Index_0";
	rename -uid "75AF5B46-400B-18E2-504A-D5B39115F831";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.6731106918370671 -0.10393275778352518 0.2493095648453334 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.1408133517827731 -1.0849562550793492 14.469913880452955 ;
	setAttr ".bps" -type "matrix" 0.070409717061975116 0.99555393555438121 -0.062568627485633771 0
		 -0.98388301355159469 0.058975043043975897 -0.1688080565097374 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.526199955645332 87.643111883799548 6.0556173428662277 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_2" -p "L_Index_1";
	rename -uid "235D2369-4EB6-BFE5-B4DF-439A1BE85BD7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.3962821853800449 -0.12523026995624775 -0.069097930824599807 ;
	setAttr ".r" -type "double3" 0 0 -1.5902773407317584e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075475167936065e-006 2.4172215589075463e-012 10.602423120057887 ;
	setAttr ".bps" -type "matrix" -0.11181985677680931 0.98940839977785855 -0.092559916159378919 0
		 -0.98004062785301338 -0.12520668012878922 -0.15441390808019673 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.848899955890239 83.080615224110034 6.3423652107990893 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_3" -p "L_Index_2";
	rename -uid "CC83C95C-4CED-C428-2E94-CE9E4B4E9489";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.6265682108442689 -0.060375131158281192 -0.027581716154965186 ;
	setAttr ".r" -type "double3" 0 0 1.6697912077683464e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4184753380935306e-006 1.114179776505247e-007 3.7411148802044685 ;
	setAttr ".bps" -type "matrix" -0.17552764371641655 0.97913048973488204 -0.10243793419867887 0
		 -0.97065614864558369 -0.18949717246277237 -0.14804547519305628 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.54449995602824 80.387542747408176 6.5942982539178967 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Index_4" -p "L_Index_3";
	rename -uid "D65D03FB-404D-169C-5D49-F2950D6121CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.9999487889167256 -9.5583433548540597e-005 5.073568233537884e-005 ;
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
	rename -uid "A49A57D8-4348-C103-7519-8D814B7FA707";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.2134785721357275 -0.012152688581295479 -0.28361831301206308 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.34258175717687 0.62796571739196139 -4.3003635789242285 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_1" -p "L_Middle_0";
	rename -uid "7AD3A36B-44BE-05B4-7630-9BBD9B63FA87";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.448032288873776 -0.28671969097413808 -0.24542006309361142 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.0816030219549297 -0.98478532917936401 9.2733107384517854 ;
	setAttr ".bps" -type "matrix" 0.10395166297972064 0.9916543542235956 -0.076260694418124136 0
		 -0.97763766959898024 0.087786495698780886 -0.19109714323873037 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -37.576399955864808 87.488331567080024 3.3879011425116676 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_2" -p "L_Middle_1";
	rename -uid "729192B1-41C3-8604-D1BB-F1AC0D705A94";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.8476063139272298 -0.014833285998804513 -0.02526448648499624 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.0913097838706637e-006 -4.9298597704866393e-014 12.229208181143044 ;
	setAttr ".bps" -type "matrix" -0.34213987638704557 0.92704975369059783 -0.15335924872031434 0
		 -0.92169499631984086 -0.36285476607024247 -0.13716687828728594 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -38.072799956113705 82.753082069150992 3.7520511892174429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_3" -p "L_Middle_2";
	rename -uid "01E64255-4A24-9F78-8858-C096CCEE1DEB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.7818302872171614 -0.094705804041964825 0.0019025264274041831 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4231603136943348e-006 1.8640247401522494e-007 5.1136715350965511 ;
	setAttr ".bps" -type "matrix" -0.4647814717253399 0.86882465116624141 -0.17065142562160487 0
		 -0.86634839689122833 -0.48603348917903533 -0.11494304067864308 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -36.918399956256252 79.6253283979663 4.2694677865740021 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Middle_4" -p "L_Middle_3";
	rename -uid "AE030FAE-406D-9CF4-7ED3-0D98BB961AA4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.3070211180663307 4.8744769785002973e-006 -2.7786433985710346e-005 ;
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
	rename -uid "50E82B17-437D-ED0F-B589-65A95F8F2DF0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.26667504435121 -0.31293516968719359 -1.5044377631214552 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 164.03591863448679 10.073235800660122 0.29817893780033355 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_1" -p "L_Ring_0";
	rename -uid "67EA57FC-48C6-1201-4426-538D0F56C072";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.9419624529280597 0.37975299810477736 -0.14403569629808999 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.2608413222005197 -3.9270558582583468 13.880797026208295 ;
	setAttr ".bps" -type "matrix" -0.048874618441212436 0.99701866515257287 -0.059708064862364088 0
		 -0.93751071452645818 -0.066412347386439724 -0.34155974625636643 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.878599956028665 87.318262414793537 1.436814679904429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_2" -p "L_Ring_1";
	rename -uid "F7430972-45D3-B132-9F7A-CDB6E92C3ACA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.0406239289366397 0.060318631271812251 -0.0022122274203972836 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.5122662475342308e-016 1.2722218725854015e-014 8.5519751351837439 ;
	setAttr ".bps" -type "matrix" -0.5992120192045679 0.7599241105944099 -0.25191328305208532 0
		 -0.72267560095831995 -0.64882367765463878 -0.23825996536187455 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.671399956256458 83.091888787317785 1.6899118183151796 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_3" -p "L_Ring_2";
	rename -uid "13429393-4DF9-1051-57C3-F98393617ACA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.8167040176379743 0.031987342542755925 0.013243913646084238 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9090959104585593e-006 1.2722230932760373e-014 0.37953028054157478 ;
	setAttr ".bps" -type "matrix" -0.65072860768519603 0.71015866795716542 -0.26875071249280685 0
		 -0.67665895938779275 -0.70294486616896223 -0.21909168812835048 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -34.734899956336264 80.636032872997248 2.504046803748186 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Ring_4" -p "L_Ring_3";
	rename -uid "7C83A2DC-494A-0963-2356-6EAE3978D0A5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.4799326019100505 -7.9379589777772708e-005 -9.0800624477083147e-006 ;
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
	rename -uid "B67D0FE4-462E-A335-33D4-CD8521257B01";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.0016654606328217 -0.93336891938980671 -2.8525688875602562 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 163.27819291549932 18.880976272515078 0.3679191689797438 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_1" -p "L_Pinky_0";
	rename -uid "DD5CEE0E-45B4-70C7-866F-70BFFAFA68BE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.6989584167467484 0.33645533789204762 -0.00071124668469479957 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.212706485275667 -7.1521486105678314 21.000260753196642 ;
	setAttr ".bps" -type "matrix" -0.15484431070880841 0.98623547281342838 -0.057989926759633319 0
		 -0.80131607645459935 -0.15971042023289406 -0.57652851385203763 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -35.020399956122709 87.931386935486174 -0.21152847538694763 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_2" -p "L_Pinky_1";
	rename -uid "F4EA443F-40E9-926F-BE17-4D931289F212";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.7440679606859675 -0.083083538462695117 0.0047633167220189065 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472925988586e-006 1.5902787151565399e-015 6.8855114422302188 ;
	setAttr ".bps" -type "matrix" -0.47969722470878084 0.82573243661521722 -0.29674318143504091 0
		 -0.66028386891561475 -0.56243556901034497 -0.49768608897761768 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -34.468499956312485 84.416245127431338 -0.0048361978950919871 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_3" -p "L_Pinky_2";
	rename -uid "D911B775-4145-9B04-681E-76A4C26024E2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.1342338029796082 0.073998869434475978 0.01913510818653652 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4242564105554578e-006 1.7911174576888958e-007 6.0210688115630857 ;
	setAttr ".bps" -type "matrix" -0.54631084569401323 0.76218098590756578 -0.34731053050269445 0
		 -0.60632390256410917 -0.64594734374209284 -0.46381392205491606 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -33.628699956356272 82.970590433278744 0.51465380386059834 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Pinky_4" -p "L_Pinky_3";
	rename -uid "D649D8D5-42A1-A4E4-27E6-66A74D836FD6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.1986903450876554 3.6254112707467812e-005 -1.9891313227660135e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 4.3534084824281436e-006 -1.3558656975045113e-021 -1.3609145324450959e-014 ;
	setAttr ".bps" -type "matrix" -0.54631084571130817 0.76194389892066949 -0.3478303534135051 0
		 -0.60632390248966272 -0.64626357315736116 -0.46337319654851244 0 -0.57785446708310706 -0.042247945600334832 0.81504559747577898 0
		 -32.290600000000055 80.994700000000023 1.2117299999999669 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Thumb_0" -p "L_Wrist";
	rename -uid "EC9190F5-4EFE-128D-9AB9-53BFA7B0297E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.1216113968383183 -1.297098675036267 2.0927862851982191 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -106.32732483646947 -51.37121795161238 -23.569510962496242 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_1" -p "L_Thumb_0";
	rename -uid "BE9C3BC1-4A78-B007-1029-C6B11792AC78";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.3098160274219879 -0.20986386494278975 -0.044042231667663856 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.0524004023769572e-016 -7.9513867036588187e-015 
		7.2715006906401332 ;
	setAttr ".bps" -type "matrix" 0.055315044616028729 0.85188961445670097 -0.5207920224234821 0
		 -0.066970927679814024 0.52358150699809647 0.84933933170159248 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.392099955341656 90.343855173995593 7.8988800193043414 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_2" -p "L_Thumb_1";
	rename -uid "9DE7B179-47BA-FD08-AECA-57A7226F0ED9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 3.4674112101615009 -0.0080513364498528972 -0.047032100924536024 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182695930376e-006 -7.9513874826969763e-015 1.9121667007214815 ;
	setAttr ".bps" -type "matrix" 0.02538865761252548 0.98757423772182551 -0.15508881665932572 0
		 -0.08306789620426222 0.15668642148488737 0.98414891654792691 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.5844999553725 87.380918895272671 9.7102593440773521 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_3" -p "L_Thumb_2";
	rename -uid "75426E56-4D00-F9DA-E9A7-CFBA9E1FBD19";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.7209765953392306 -0.28166741017848551 8.7519273119340824e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472935639464e-006 -1.272221889173292e-014 -9.5324154644603887 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Clav" -p "C_ChestBegin";
	rename -uid "43D78285-4293-16FB-3B07-08B9357A0E29";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 16.780734928456468 -1.8864758942646773 3.4306399999999928 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 24.362555348840477 96.310667653782787 103.06608621941082 ;
	setAttr ".bps" -type "matrix" 0.97096663178489051 0.21828050916169012 0.097864290118605174 0
		 0.21724984896944344 -0.97588583281488517 0.021197745963948203 0 0.10013142904732321 0.00067869824772238128 -0.99497398774321211 0
		 -1.5920100000000004 148.55822219678041 -4.5013362696721906 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "R_Shoulder" -p "R_Clav";
	rename -uid "39D98366-4A65-A872-59FE-5CA3D7FFBDBE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -11.592773760973227 0.44728846118852061 2.9729541150491041 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.8354150615637645 -11.293643790753251 -47.495974843215365 ;
	setAttr ".bps" -type "matrix" 0.26235226505945086 0.96470156178127819 -0.022851383217186154 0
		 0.96011801640670313 -0.26333161408024858 -0.093967311322336461 0 -0.096667903615593617 0.0027125122403274561 -0.99531299533760365 0
		 -15.337299999999994 145.46816650143637 -5.8867444007556049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "R_Elbow" -p "R_Shoulder";
	rename -uid "880AE662-4C7D-91FE-B662-2AB6B05C567E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -31.978011357513623 -0.00020067064706097426 -7.6583393955331758e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.9025490431606179e-015 -15.150734866123534 -3.6863782398770268e-014 ;
	setAttr ".bps" -type "matrix" 0.43389320214860133 0.85690266771633017 -0.27830649864828944 0
		 0.46157048511156973 -0.47669839186407365 -0.74813857704844777 0 -0.77375020284527474 0.19615417725565557 -0.60235717173621639 0
		 -22.884002750078423 117.71811015626857 -5.2294136802891966 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "R_Wrist" -p "R_Elbow";
	rename -uid "A9C1DB2D-47A3-7932-4028-E09A7073F428";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -26.190354653074017 0.00021330747112813242 0.0001034576337524129 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.64018042213178394 -3.4169433382743883 -16.056435375520927 ;
	setAttr ".bps" -type "matrix" 0.42895584361388206 0.86277461858135351 -0.26761323166335294 0
		 0.46607536049615472 -0.46516195703129459 -0.75259425460814888 0 -0.77380271553405833 0.19810176996336093 -0.60165193107768 0
		 -33.622499955472293 96.510213366543951 1.6584548023795049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "R_Index_0" -p "R_Wrist";
	rename -uid "34868EAC-4EE1-DEE9-815E-C59D1FBD3B7A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.9872615428194749 0.43101374070040777 -1.0572761306864464 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -165.73014377735896 -12.922429796688403 2.252670726811226 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_1" -p "R_Index_0";
	rename -uid "27DE298C-4E16-F91E-10BA-259714436BC4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.6731150892365818 0.10393149591236295 -0.24931253279163101 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.14081335178800805 -1.0849562550793417 14.469913880452927 ;
	setAttr ".bps" -type "matrix" 0.070409717061975116 0.99555393555438121 -0.062568627485633771 0
		 -0.98388301355159469 0.058975043043975897 -0.1688080565097374 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.526199955645332 87.643111883799548 6.0556173428662277 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_2" -p "R_Index_1";
	rename -uid "A8B55319-4C7B-EA6F-B6FF-BEB8253F9F36";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.3962763405690737 0.12523078588336034 0.069101809814435811 ;
	setAttr ".r" -type "double3" 0 0 -1.5902773407317584e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.2588728339338362e-006 9.7006917879425188e-013 10.602423120057887 ;
	setAttr ".bps" -type "matrix" -0.11181985677680931 0.98940839977785855 -0.092559916159378919 0
		 -0.98004062785301338 -0.12520668012878922 -0.15441390808019673 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.848899955890239 83.080615224110034 6.3423652107990893 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_3" -p "R_Index_2";
	rename -uid "31B52620-4071-0425-FF04-AB998F7DCF8D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.6265723626165993 0.060376938428646554 0.02757805730310281 ;
	setAttr ".r" -type "double3" 0 0 1.6697912077683464e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.0924846766264094e-006 3.5974396842550451e-008 3.741114880204373 ;
	setAttr ".bps" -type "matrix" -0.17552764371641655 0.97913048973488204 -0.10243793419867887 0
		 -0.97065614864558369 -0.18949717246277237 -0.14804547519305628 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.54449995602824 80.387542747408176 6.5942982539178967 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Index_4" -p "R_Index_3";
	rename -uid "459C7A16-4CD7-5B03-65B9-2994CEEE2ADE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.9999104164787127 0.00012549872273126539 -1.7607609970937688e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.4150945850063746e-006 7.1729970621998529e-021 -2.14424105002083e-015 ;
	setAttr ".bps" -type "matrix" -0.17552764376574126 0.97906038632627457 -0.10310580100408247 0
		 -0.97065615208658595 -0.1895981125786585 -0.14791615910060019 0 -0.16436751713921696 0.074116905178621365 0.98361069721523109 0
		 -37.193500000000043 78.323900000000023 6.6473899999999677 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Middle_0" -p "R_Wrist";
	rename -uid "42E1283B-4C9E-2A54-853C-6AA8979D05A0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.213437979741677 0.012149451495574226 0.28360058829635548 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.34258175717468 0.62796571739193652 -4.3003635789242818 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_1" -p "R_Middle_0";
	rename -uid "9B57176C-4EB9-7040-7E95-389A6674347F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.4480340473825635 0.28671754240654934 0.24541977976908314 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.0816030219530068 -0.98478532917965067 9.2733107384517126 ;
	setAttr ".bps" -type "matrix" 0.10395166297972064 0.9916543542235956 -0.076260694418124136 0
		 -0.97763766959898024 0.087786495698780886 -0.19109714323873037 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -37.576399955864808 87.488331567080024 3.3879011425116676 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_2" -p "R_Middle_1";
	rename -uid "4A59E6E6-47D4-864B-0392-C991F50869E3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.847605109922668 0.014835353129186046 0.025264206875352357 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182719404348e-006 2.0673605453209845e-014 12.229208181143072 ;
	setAttr ".bps" -type "matrix" -0.34213987638704557 0.92704975369059783 -0.15335924872031434 0
		 -0.92169499631984086 -0.36285476607024247 -0.13716687828728594 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -38.072799956113705 82.753082069150992 3.7520511892174429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_3" -p "R_Middle_2";
	rename -uid "5D473A2E-4F97-AE23-34E2-1FAC2C0E8693";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7818332839123201 0.094704914787378414 -0.0019031639002839995 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.954040626237515e-006 -7.878295012634566e-008 5.1136715350964828 ;
	setAttr ".bps" -type "matrix" -0.4647814717253399 0.86882465116624141 -0.17065142562160487 0
		 -0.86634839689122833 -0.48603348917903533 -0.11494304067864308 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -36.918399956256252 79.6253283979663 4.2694677865740021 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Middle_4" -p "R_Middle_3";
	rename -uid "AE3907C5-40EF-FFB4-469A-39B806ECB93F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.3070481976334207 -3.9047498290756266e-005 4.7661481641370074e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 4.9783130603797145e-006 5.7478109700102366e-021 6.8452896306875772e-015 ;
	setAttr ".bps" -type "matrix" -0.46478147176281848 0.86870804318900663 -0.17124403407043384 0
		 -0.86634839685366949 -0.48611178182206682 -0.11461147779717742 0 -0.18280765513256333 0.095087703056191936 0.97853956994718994 0
		 -35.846200000000053 77.514099999999985 4.5119399999999752 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Ring_0" -p "R_Wrist";
	rename -uid "49F72EDB-43CF-1443-C297-EF94485B4B2F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.266639489141582 0.31293341478760794 1.5044214389226482 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 164.03591863448636 10.073235800660152 0.29817893780023008 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_1" -p "R_Ring_0";
	rename -uid "005018FD-44A9-BB2E-0AFF-E6B3499699D2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.9419589041846095 -0.37975161518184564 0.14403651233838133 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.2608413222006725 -3.9270558582583024 13.880797026208251 ;
	setAttr ".bps" -type "matrix" -0.048874618441212436 0.99701866515257287 -0.059708064862364088 0
		 -0.93751071452645818 -0.066412347386439724 -0.34155974625636643 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.878599956028665 87.318262414793537 1.436814679904429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_2" -p "R_Ring_1";
	rename -uid "EE652DC4-4AF1-70FA-1240-A1B6DEBD7C81";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.0406276288918264 -0.060321644236111638 0.0022116674773613454 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.4787793338872601e-006 5.5659716404403158e-015 8.5519751351837439 ;
	setAttr ".bps" -type "matrix" -0.5992120192045679 0.7599241105944099 -0.25191328305208532 0
		 -0.72267560095831995 -0.64882367765463878 -0.23825996536187455 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.671399956256458 83.091888787317785 1.6899118183151796 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_3" -p "R_Ring_2";
	rename -uid "30A772F3-4F74-F646-9E51-60A31A980D42";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.8166988265812876 -0.031986378616714717 -0.013243395279911141 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.2442900884164103e-011 9.7954476586468025e-009 0.37953028054061438 ;
	setAttr ".bps" -type "matrix" -0.65072860768519603 0.71015866795716542 -0.26875071249280685 0
		 -0.67665895938779275 -0.70294486616896223 -0.21909168812835048 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -34.734899956336264 80.636032872997248 2.504046803748186 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Ring_4" -p "R_Ring_3";
	rename -uid "360685C5-4AD0-C2CF-8D45-92B43402575D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.479953779844891 0.00011799885930230403 3.0356916784768373e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.909095910416422e-006 3.3258754395470345e-020 -3.2638438130634571e-016 ;
	setAttr ".bps" -type "matrix" -0.65072860770563634 0.70997518078224808 -0.26923506789922219 0
		 -0.67665896822087535 -0.70309414983428609 -0.21861211584691231 0 -0.34450677763978116 0.039923165480920647 0.93793455049818775 0
		 -33.121200000000037 78.766999999999967 3.0184399999999769 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Pinky_0" -p "R_Wrist";
	rename -uid "F9E546F1-4C15-C6DC-1B0A-62AA5771F2D4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.0016289352819427 0.9333673062632073 2.8525523512421547 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 163.27819291549886 18.880976272515095 0.36791916897958371 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_1" -p "R_Pinky_0";
	rename -uid "08496EB4-4B01-791A-C836-1EB7B6C39A25";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.6989554411630081 -0.33645390195725611 0.00071144112819254701 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.212706485275781 -7.1521486105678411 21.000260753196638 ;
	setAttr ".bps" -type "matrix" -0.15484431070880841 0.98623547281342838 -0.057989926759633319 0
		 -0.80131607645459935 -0.15971042023289406 -0.57652851385203763 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -35.020399956122709 87.931386935486174 -0.21152847538694763 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_2" -p "R_Pinky_1";
	rename -uid "05AEFE2E-41E2-D0C6-F958-4CB6BD2DD278";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.744070874225315 0.083083618684760552 -0.0047630278679147153 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9090959110382831e-006 1.0336802572574556e-014 6.8855114422302188 ;
	setAttr ".bps" -type "matrix" -0.47969722470878084 0.82573243661521722 -0.29674318143504091 0
		 -0.66028386891561475 -0.56243556901034497 -0.49768608897761768 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -34.468499956312485 84.416245127431338 -0.0048361978950919871 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_3" -p "R_Pinky_2";
	rename -uid "78F25C15-4BDB-C720-A695-BB96527D0355";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.1342338422073936 -0.073999777451504656 -0.019135114681751553 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.7009811941994807e-006 2.1141290092648266e-008 6.0210688115630902 ;
	setAttr ".bps" -type "matrix" -0.54631084569401323 0.76218098590756578 -0.34731053050269445 0
		 -0.60632390256410917 -0.64594734374209284 -0.46381392205491606 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -33.628699956356272 82.970590433278744 0.51465380386059834 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Pinky_4" -p "R_Pinky_3";
	rename -uid "FF16B18D-4836-4F98-8ED9-2A999273C446";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.1986796412624017 -3.4402227129248786e-005 3.8116658664932856e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 4.0945545664670365e-006 -5.8882969550409755e-022 -1.5108297090206272e-015 ;
	setAttr ".bps" -type "matrix" -0.54631084571130817 0.76194389892066949 -0.3478303534135051 0
		 -0.60632390248966272 -0.64626357315736116 -0.46337319654851244 0 -0.57785446708310706 -0.042247945600334832 0.81504559747577898 0
		 -32.290600000000055 80.994700000000023 1.2117299999999669 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Thumb_0" -p "R_Wrist";
	rename -uid "45D4091E-4EAA-87A8-09B9-5F960D3C55C2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.1215717774366567 1.2970944318277446 -2.0928039794031754 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -106.32732483647007 -51.371217951612536 -23.569510962495819 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_1" -p "R_Thumb_0";
	rename -uid "C1D1F53E-4F69-0A9F-A232-3D905606F6F8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.3098157979305753 0.20986480113026573 0.04404381813221292 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.5262002011884668e-016 3.975693351829392e-015 7.2715006906401332 ;
	setAttr ".bps" -type "matrix" 0.055315044616028729 0.85188961445670097 -0.5207920224234821 0
		 -0.066970927679814024 0.52358150699809647 0.84933933170159248 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.392099955341656 90.343855173995593 7.8988800193043414 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_2" -p "R_Thumb_1";
	rename -uid "4B8640DB-4FEF-AD08-5CAA-29BFE3A2E80F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.46741277953668 0.0080487572840866051 0.047032795069693378 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.3269553518708216e-017 7.9513867036579685e-016 1.9121667007212906 ;
	setAttr ".bps" -type "matrix" 0.02538865761252548 0.98757423772182551 -0.15508881665932572 0
		 -0.08306789620426222 0.15668642148488737 0.98414891654792691 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.5844999553725 87.380918895272671 9.7102593440773521 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_3" -p "R_Thumb_2";
	rename -uid "B43523DD-47B6-25EF-5619-1CBECF2DED49";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7209768695333167 0.28167690540301749 -8.0169923659667575e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377364598640437e-007 3.1805543497058109e-015 -9.5324154644601595 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Hip" -p "C_Pelvis";
	rename -uid "2EB04C85-4244-36F8-F622-51B4BD810584";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -5.1093103503544626 -0.82277863371729509 -7.2107900000000091 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 168.54708099488485 8.1975146413132478 -172.52490098427037 ;
	setAttr ".bps" -type "matrix" 0.04367621427123513 0.99879915221154247 -0.022195536678289766 0
		 -1.3006955835555549e-012 0.022216737247664126 0.999753177832443 0 0.99904573884629189 -0.043665434013329021 0.00097034297773582754 0
		 -8.2375200000000035 99.635493474825282 -2.2160409616281522 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "L_Knee" -p "L_Hip";
	rename -uid "74E7D895-4C7E-31BE-B364-59B8514FCB80";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 38.709705096841738 -0.12596703155597355 -0.12268008366458716 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.5862166555727496 -0.0041968062665369938 2.4732599614511686 ;
	setAttr ".bps" -type "matrix" 0.043710370994654441 0.99896923390645309 0.012242270045389339 0
		 3.5294000512962886e-010 -0.012253981865253649 0.99992491714550569 0 0.99904424499994482 -0.043707089090908237 -0.00053562644606822672 0
		 -10.096999562900118 57.112293455685503 -1.2710809628003075 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "L_Ankle" -p "L_Knee";
	rename -uid "534293E9-4153-59B1-0CAC-4CA75748D77D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 42.277894442571622 0.10738330076219427 0.25688592542582001 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -11.648793612157837 -9.1969564819585372 -74.314013207050536 ;
	setAttr ".bps" -type "matrix" 0.089586411029085211 0.82001406268021293 -0.56528860944266346 0
		 -0.078021190938231205 0.57160461050695421 0.81681139990316831 0 0.99291840990260016 -0.029070711272434359 0.11518647933940374 0
		 -11.971399122896578 14.273993436447512 -1.7960609639808891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "L_Ball" -p "L_Ankle";
	rename -uid "0B886800-4896-D6E4-487C-D191CE8C8D1A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 14.896624012950056 3.1974423109204508e-014 -1.4210854715202004e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -8.7198046459577263 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "L_Toe" -p "L_Ball";
	rename -uid "E3D1F95C-4AFB-1D58-177F-6984AA27A0DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 8.7017316428972986 4.4408920985006262e-015 -7.1054273576010019e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Hip" -p "C_Pelvis";
	rename -uid "9218A93D-43DC-7750-DC2F-7D8D61CE9E7F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -5.1093103503544199 -0.82277863371731286 7.2107899999999914 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 168.54708099488488 8.1975146413132602 7.4750990157296462 ;
	setAttr ".bps" -type "matrix" 0.04367621427123513 0.99879915221154247 -0.022195536678289766 0
		 -1.3006955835555549e-012 0.022216737247664126 0.999753177832443 0 0.99904573884629189 -0.043665434013329021 0.00097034297773582754 0
		 -8.2375200000000035 99.635493474825282 -2.2160409616281522 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "R_Knee" -p "R_Hip";
	rename -uid "D07ECF3F-400B-C141-9E2D-E6936CC281FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -38.70970509684178 0.1259670315559358 0.12268008366459426 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.58621665557461466 -0.0041968062665342165 2.4732599614511677 ;
	setAttr ".bps" -type "matrix" 0.043710370994654441 0.99896923390645309 0.012242270045389339 0
		 3.5294000512962886e-010 -0.012253981865253649 0.99992491714550569 0 0.99904424499994482 -0.043707089090908237 -0.00053562644606822672 0
		 -10.096999562900118 57.112293455685503 -1.2710809628003075 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "R_Ankle" -p "R_Knee";
	rename -uid "5E86640A-4820-7B80-5295-33966B7B1295";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -42.277894442571679 -0.10738330076219693 -0.25688592542579514 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -11.648793612158315 -9.1969564819603367 -74.314013207050451 ;
	setAttr ".bps" -type "matrix" 0.089586411029085211 0.82001406268021293 -0.56528860944266346 0
		 -0.078021190938231205 0.57160461050695421 0.81681139990316831 0 0.99291840990260016 -0.029070711272434359 0.11518647933940374 0
		 -11.971399122896578 14.273993436447512 -1.7960609639808891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "R_Ball" -p "R_Ankle";
	rename -uid "27549E50-40E9-1F5A-C2D9-698A50C38E2B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -14.896602264751635 -7.2648652125195667e-006 4.2939176495337961e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 2.4249141841433817e-016 -3.1805546814635093e-015 -8.7198046459577121 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Toe" -p "R_Ball";
	rename -uid "A75DFD3D-4AB7-0FD9-4CA9-0391F3B79878";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -8.7017087224093732 3.5072579418482519e-007 -5.4263283175259858e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode transform -n "locator_L_Foot_Ext" -p "yuheng_BuilderGrp";
	rename -uid "F1E1C203-4973-41F7-75B4-CC8A8AE82D4B";
	setAttr ".t" -type "double3" 28.494337329551218 0.14341159317586971 2.2329580024170923 ;
	setAttr ".r" -type "double3" 0 24.31003746756657 0 ;
createNode locator -n "locator_L_Foot_ExtShape" -p "locator_L_Foot_Ext";
	rename -uid "F8725828-4B21-7760-A87C-33B3C4D2A1D7";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -3.5527136788005009e-015 -2.7755575615628914e-017 
		0 ;
createNode transform -n "locator_L_Foot_Int" -p "yuheng_BuilderGrp";
	rename -uid "3D5F2C98-4E0A-90F2-19CA-71B0AE5DC5AE";
	setAttr ".t" -type "double3" 18.172580587150449 0 6.432998998723555 ;
	setAttr ".r" -type "double3" 0 19.527551479126259 0 ;
createNode locator -n "locator_L_Foot_IntShape" -p "locator_L_Foot_Int";
	rename -uid "3A17AD31-4C55-2B46-3CE7-51AD849A9844";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -1.572007826684607e-015 0 5.8882639917960951e-016 ;
createNode transform -n "locator_L_Foot_Base" -p "yuheng_BuilderGrp";
	rename -uid "3191AFB1-4576-0396-9D2B-80AD2649A0E3";
	setAttr ".t" -type "double3" 17.126727565741071 0.87666600942611694 -12.941733892444205 ;
	setAttr ".r" -type "double3" 0 17.726921192996482 0 ;
createNode locator -n "locator_L_Foot_BaseShape" -p "locator_L_Foot_Base";
	rename -uid "7367A51B-4AE6-00C8-719A-5ABD930B9C88";
	setAttr -k off ".v";
createNode transform -n "locator_L_Foot_BaseSwive" -p "yuheng_BuilderGrp";
	rename -uid "C97CB8AC-426B-CF03-EF3B-A281B37733E2";
	setAttr ".t" -type "double3" 18.835947901097406 0.86427691328901979 -7.9156431985422966 ;
	setAttr ".r" -type "double3" 0 20.397642226450419 0 ;
createNode locator -n "locator_L_Foot_BaseSwiveShape" -p "locator_L_Foot_BaseSwive";
	rename -uid "D27A97AA-4AA3-F185-634B-82A4F290D8B0";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 1.1102230246251565e-016 -5.5511151231257827e-016 ;
createNode transform -n "locator_L_Foot_ToeSwive" -p "yuheng_BuilderGrp";
	rename -uid "FEFB7D2E-4614-5305-49B9-EDA0CDE0A169";
	setAttr ".t" -type "double3" 23.103343485638323 0.11554945879680645 4.3556402479563463 ;
	setAttr ".r" -type "double3" 0 19.148939780023536 0 ;
createNode locator -n "locator_L_Foot_ToeSwiveShape" -p "locator_L_Foot_ToeSwive";
	rename -uid "4B41E436-438C-70BA-C585-518E50B640D8";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 2.7755575615628914e-017 0 ;
createNode transform -n "locator_L_LegPV" -p "yuheng_BuilderGrp";
	rename -uid "33F93F0E-4D10-7EAA-1DAF-E2A639F57D14";
	setAttr ".t" -type "double3" 13.374038696289063 44.839851379394531 35.837547302246094 ;
createNode locator -n "locator_L_LegPVShape" -p "locator_L_LegPV";
	rename -uid "E9F85FC8-43DC-2305-5CD9-818845E2A6AA";
	setAttr -k off ".v";
createNode transform -n "locator_R_LegPV" -p "yuheng_BuilderGrp";
	rename -uid "C523A705-45A0-174A-88D7-74944830925C";
	setAttr ".t" -type "double3" -13.374038696289063 44.839851379394531 35.837547302246094 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode locator -n "locator_R_LegPVShape" -p "locator_R_LegPV";
	rename -uid "87F813C1-4996-AFFB-7C06-94AC9ED62B8B";
	setAttr -k off ".v";
createNode transform -n "locator_L_ArmPV" -p "yuheng_BuilderGrp";
	rename -uid "7A20E7AA-4EB2-40F4-55A3-41A2D6DF3320";
	setAttr ".t" -type "double3" 41.495792388916016 113.43680572509766 -40.671066284179687 ;
createNode locator -n "locator_L_ArmPVShape" -p "locator_L_ArmPV";
	rename -uid "C1C529B0-453A-F7C1-BFB5-47A20D33DE51";
	setAttr -k off ".v";
createNode transform -n "locator_R_ArmPV" -p "yuheng_BuilderGrp";
	rename -uid "FABE8161-4EEF-0EA6-8678-92B4ABD1287E";
	setAttr ".t" -type "double3" -41.495792388916016 113.43680572509766 -40.671066284179687 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode locator -n "locator_R_ArmPVShape" -p "locator_R_ArmPV";
	rename -uid "9AAE0F62-41D8-A126-6B0F-CDAAD1BBD9BC";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "86B83CA2-4627-2F75-5C34-63B3225E90C1";
	setAttr -s 8 ".lnk";
	setAttr -s 8 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "E1BD1945-4616-6C89-5A35-7E80297E634D";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "203AA1BA-4901-E4E1-EF07-75AE7F99B058";
createNode displayLayerManager -n "layerManager";
	rename -uid "2B5C5037-4C81-F268-A320-FE8D2C5CA9D1";
	setAttr -s 3 ".dli[1:2]"  1 2;
	setAttr -s 3 ".dli";
createNode displayLayer -n "defaultLayer";
	rename -uid "85F25CCF-46DC-85D2-2094-1AB96562B425";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "13DCA915-4E3F-F087-BE12-EC9ABA77EAA1";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "02373C42-40FA-6C99-1E09-479B29ED0D98";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "C909B1FF-4F50-4D5A-00DC-6389EC7C0DD8";
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
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1690\n            -height 1054\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n"
		+ "            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n"
		+ "            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n"
		+ "            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n"
		+ "            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n"
		+ "                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n"
		+ "                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1690\\n    -height 1054\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1690\\n    -height 1054\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 100 -size 500 -divisions 8 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "788B171A-4A09-50D6-0F34-839D57103207";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 100 -ast 0 -aet 250 ";
	setAttr ".st" 6;
createNode renderLayerManager -n "renderLayerManager1";
	rename -uid "3D86C526-462A-EA25-84F7-36A80D3825BE";
createNode renderLayer -n "defaultRenderLayer1";
	rename -uid "DE13D4DC-476A-73B2-6EE8-B2B73A5A57CD";
	setAttr ".g" yes;
createNode renderLayerManager -n "Elisa_Model_renderLayerManager";
	rename -uid "DBE23B35-4DBF-957F-A936-C7AB16FD46EE";
createNode renderLayer -n "Elisa_Model_defaultRenderLayer";
	rename -uid "9D346483-45C2-312B-3A8A-49A5DA677912";
	setAttr ".g" yes;
createNode lambert -n "lambert5";
	rename -uid "1F8D4332-439E-2F04-4250-6697410ACB51";
	setAttr ".c" -type "float3" 0.2071 0.1015 0.1015 ;
createNode shadingEngine -n "lambert5SG";
	rename -uid "CAD57E4F-4AD9-044C-6BDE-66B8A3CBF53B";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "81467413-45B4-370D-3F69-CF8886B07BA6";
createNode groupId -n "groupId1";
	rename -uid "D84D6840-4E10-D758-E93C-96AC42EB4112";
	setAttr ".ihi" 0;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "55FB5511-4DEC-C787-5104-C39606AFB8E0";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -705.71428571428578 194.28571428571431 ;
	setAttr ".tgi[0].vh" -type "double2" 801.90476190476181 473.33333333333331 ;
createNode aiOptions -s -n "defaultArnoldRenderOptions";
	rename -uid "2556C1EE-4D2B-191B-06E8-4791F163243D";
	addAttr -ci true -sn "ARV_options" -ln "ARV_options" -dt "string";
	setAttr ".AA_samples" 5;
	setAttr ".version" -type "string" "1.4.2.0";
	setAttr ".ARV_options" -type "string" "Display Settings=0;Show Status Bar=1;Display Pixel Information=0;3D Manipulation=0;Show AOVs list=1;Show Cameras list=1;Show RGBA icon=1;Show Crop Region icon=1;Show 3D Manipulation icon=0;Show Debug Shading icon=0;Show Exposure icon=1;Show Gamma icon=0;Darken Out-Of-Region=0;Show Render Tiles=0;AOVs=Beauty;Test Resolution=100%;Log=Last Progressive Step;Camera=frontShape;Save UI Threads=1;Debug Shading=Disabled;Color Management.Gamma=1;Color Management.Exposure=0;Background.BG=BG Color;Background.Color=0 0 0;Background.Image=;Background.Scale=1       1;Background.Offset=0       0;Background.Apply Color Management=1;Foreground.Enable FG=0;Foreground.Image=;Foreground.Scale=1       1;Foreground.Offset=0       0;Foreground.Apply Color Management=1;";
createNode aiAOVFilter -s -n "defaultArnoldFilter";
	rename -uid "CE939482-4B1F-9C16-D4D9-DC92BBEC4F2B";
	setAttr ".ai_translator" -type "string" "gaussian";
createNode aiAOVDriver -s -n "defaultArnoldDriver";
	rename -uid "6F877B46-445D-BC76-6F2C-E9A8B752882A";
	setAttr ".ai_translator" -type "string" "exr";
createNode aiAOVDriver -s -n "defaultArnoldDisplayDriver";
	rename -uid "4A3B8ADA-4059-5E07-6FE1-D4A7CB924101";
	setAttr ".output_mode" 0;
	setAttr ".ai_translator" -type "string" "maya";
createNode expression -n "xgmRefreshPreview";
	rename -uid "55802880-4BEC-4671-159F-0CAA70877831";
	setAttr -k on ".nds";
	setAttr ".ixp" -type "string" "xgmPreview -r";
	setAttr ".uno" 1;
createNode renderLayerManager -n "yuheng_Builder:renderLayerManager";
	rename -uid "B55EA208-4CC0-5E56-8073-4F84A5185A23";
createNode renderLayer -n "yuheng_Builder:defaultRenderLayer";
	rename -uid "2216D2FF-40C3-A1D9-9C4F-58B6D658A321";
	setAttr ".g" yes;
createNode renderLayerManager -n "yuheng_Builder:renderLayerManager1";
	rename -uid "99754511-4C7E-5A95-2E81-8DBA1B23E4C9";
createNode renderLayer -n "yuheng_Builder:defaultRenderLayer1";
	rename -uid "3537BF32-4BDE-B88E-060E-EF899A0918F2";
	setAttr ".g" yes;
createNode renderLayerManager -n "yuheng_Builder:Elisa_Model_renderLayerManager";
	rename -uid "C5FAE781-40ED-AA93-36F4-8F88696A2FBA";
createNode renderLayer -n "yuheng_Builder:Elisa_Model_defaultRenderLayer";
	rename -uid "B1C7B12A-4480-E453-0FE8-D995F0EF0E8F";
	setAttr ".g" yes;
createNode lambert -n "yuheng_Builder:lambert5";
	rename -uid "580FA6E7-4543-339A-4F0A-45B40B453127";
	setAttr ".c" -type "float3" 0.2071 0.1015 0.1015 ;
createNode shadingEngine -n "yuheng_Builder:lambert5SG";
	rename -uid "2F3D2395-4E70-9792-4E20-AA94F7A1AD52";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "yuheng_Builder:materialInfo4";
	rename -uid "FAD115F0-4A6C-4100-6054-19A39A45350A";
createNode groupId -n "yuheng_Builder:groupId1";
	rename -uid "98FB8F54-47F2-9B5E-5F06-77B88442EBC0";
	setAttr ".ihi" 0;
createNode nodeGraphEditorInfo -n "yuheng_Builder:hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "181BD85F-420F-D6A6-F3C7-7B8C77AB482D";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -705.71428571428578 194.28571428571431 ;
	setAttr ".tgi[0].vh" -type "double2" 801.90476190476181 473.33333333333331 ;
createNode expression -n "yuheng_Builder:xgmRefreshPreview";
	rename -uid "81CA50B6-4C37-5E53-2785-0A8B153C06BD";
	setAttr -k on ".nds";
	setAttr ".ixp" -type "string" "xgmPreview -r";
	setAttr ".uno" 1;
createNode displayLayer -n "layer1";
	rename -uid "C4919765-4DEA-2DCE-A911-4EBBBE603699";
	setAttr ".dt" 1;
	setAttr ".do" 1;
createNode shadingEngine -n "yuheng_Model_lambert2SG";
	rename -uid "0C647E29-4156-A181-74A2-A8AA4EC933CC";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr ".aal" -type "attributeAlias" {"ai_aov_diffuse_color","aiCustomAOVs[0]","ai_aov_direct_specular"
		,"aiCustomAOVs[1]","ai_aov_AO","aiCustomAOVs[2]","ai_aov_id_1","aiCustomAOVs[3]"} ;
createNode materialInfo -n "yuheng_Model_materialInfo17";
	rename -uid "FF50C7CA-4EC2-6ABD-A8A4-2A923CA3FB35";
createNode lambert -n "yuheng_Model_head1";
	rename -uid "CBA5F2BB-4CCE-B449-CB51-F78D087D59EA";
createNode file -n "yuheng_Model_file2";
	rename -uid "8FD42517-465B-1C8A-77AF-13B91CFAC11E";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Yuheng/TEX/head_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "yuheng_Model_place2dTexture2";
	rename -uid "F43AF442-470E-B87B-7294-A982E16EE53F";
createNode shadingEngine -n "yuheng_Model_lambert16SG";
	rename -uid "6FFF52C1-4AA6-D888-ACFD-1FBEDB0A2897";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "yuheng_Model_materialInfo18";
	rename -uid "5D73C54E-4958-557E-48EC-839FF1EA2405";
createNode lambert -n "yuheng_Model_lambert16";
	rename -uid "A62B623B-4799-4379-BEB6-CC968EF778DB";
createNode shadingEngine -n "yuheng_Model_lambert10SG";
	rename -uid "C0356312-4C24-06F8-E3DD-9C9B9FB8F9E1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr ".aal" -type "attributeAlias" {"ai_aov_diffuse_color","aiCustomAOVs[0]","ai_aov_direct_specular"
		,"aiCustomAOVs[1]","ai_aov_AO","aiCustomAOVs[2]","ai_aov_id_1","aiCustomAOVs[3]"} ;
createNode materialInfo -n "yuheng_Model_materialInfo11";
	rename -uid "3D28F013-4678-1788-2685-2A9601E9F697";
createNode lambert -n "yuheng_Model_eye_occlusion_L1";
	rename -uid "7FEAE240-42D1-52EE-5B59-7583B03DA4AF";
createNode shadingEngine -n "yuheng_Model_lambert11SG";
	rename -uid "C017B96E-4E2B-1576-D635-97A664A452C8";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr ".aal" -type "attributeAlias" {"ai_aov_diffuse_color","aiCustomAOVs[0]","ai_aov_direct_specular"
		,"aiCustomAOVs[1]","ai_aov_AO","aiCustomAOVs[2]","ai_aov_id_1","aiCustomAOVs[3]"} ;
createNode materialInfo -n "yuheng_Model_materialInfo12";
	rename -uid "56130CEF-4D12-FE4A-A297-3E96086B381C";
createNode lambert -n "yuheng_Model_eye_occlusion_R1";
	rename -uid "6F6C4830-4E40-E330-E1FF-E0BBAFBD9A0F";
createNode renderLayerManager -n "yuheng_Model_renderLayerManager";
	rename -uid "4F457D4E-43C0-5344-BA0C-B3BD77BDABCA";
createNode renderLayer -n "yuheng_Model_defaultRenderLayer";
	rename -uid "8599AF32-426B-8983-8F89-498D77FE1318";
	setAttr ".g" yes;
createNode displayLayer -n "layer2";
	rename -uid "210A8D57-49BE-9E67-CFB7-1C8EF1E23C16";
	setAttr ".dt" 2;
	setAttr ".do" 2;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 8 ".st";
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
	setAttr -s 10 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :defaultRenderingList1;
	setAttr -s 7 ".r";
select -ne :defaultTextureList1;
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
connectAttr "C_ChestBegin.s" "R_Breast.is";
connectAttr "C_ChestBegin.s" "L_Breast.is";
connectAttr "C_ChestBegin.s" "L_Clav.is";
connectAttr "L_Clav.s" "L_Shoulder.is";
connectAttr "L_Shoulder.s" "L_Elbow.is";
connectAttr "L_Elbow.s" "L_Wrist.is";
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
connectAttr "L_Wrist.s" "L_Thumb_0.is";
connectAttr "L_Thumb_0.s" "L_Thumb_1.is";
connectAttr "L_Thumb_1.s" "L_Thumb_2.is";
connectAttr "L_Thumb_2.s" "L_Thumb_3.is";
connectAttr "C_ChestBegin.s" "R_Clav.is";
connectAttr "R_Clav.s" "R_Shoulder.is";
connectAttr "R_Shoulder.s" "R_Elbow.is";
connectAttr "R_Elbow.s" "R_Wrist.is";
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
connectAttr "R_Wrist.s" "R_Thumb_0.is";
connectAttr "R_Thumb_0.s" "R_Thumb_1.is";
connectAttr "R_Thumb_1.s" "R_Thumb_2.is";
connectAttr "R_Thumb_2.s" "R_Thumb_3.is";
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
relationship "link" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Builder:lambert5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert10SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert11SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "yuheng_Model_lambert16SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Builder:lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert10SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert11SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "yuheng_Model_lambert16SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "renderLayerManager1.rlmi[0]" "defaultRenderLayer1.rlid";
connectAttr "Elisa_Model_renderLayerManager.rlmi[0]" "Elisa_Model_defaultRenderLayer.rlid"
		;
connectAttr "lambert5.oc" "lambert5SG.ss";
connectAttr "groupId1.msg" "lambert5SG.gn" -na;
connectAttr "lambert5SG.msg" "materialInfo4.sg";
connectAttr "lambert5.msg" "materialInfo4.m";
connectAttr ":time1.o" "xgmRefreshPreview.tim";
connectAttr "yuheng_Builder:renderLayerManager.rlmi[0]" "yuheng_Builder:defaultRenderLayer.rlid"
		;
connectAttr "yuheng_Builder:renderLayerManager1.rlmi[0]" "yuheng_Builder:defaultRenderLayer1.rlid"
		;
connectAttr "yuheng_Builder:Elisa_Model_renderLayerManager.rlmi[0]" "yuheng_Builder:Elisa_Model_defaultRenderLayer.rlid"
		;
connectAttr "yuheng_Builder:lambert5.oc" "yuheng_Builder:lambert5SG.ss";
connectAttr "yuheng_Builder:groupId1.msg" "yuheng_Builder:lambert5SG.gn" -na;
connectAttr "yuheng_Builder:lambert5SG.msg" "yuheng_Builder:materialInfo4.sg";
connectAttr "yuheng_Builder:lambert5.msg" "yuheng_Builder:materialInfo4.m";
connectAttr ":time1.o" "yuheng_Builder:xgmRefreshPreview.tim";
connectAttr "layerManager.dli[1]" "layer1.id";
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
connectAttr "layerManager.dli[2]" "layer2.id";
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Builder:lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert10SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert11SG.pa" ":renderPartition.st" -na;
connectAttr "yuheng_Model_lambert16SG.pa" ":renderPartition.st" -na;
connectAttr "lambert5.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Builder:lambert5.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_head1.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_eye_occlusion_L1.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_eye_occlusion_R1.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_lambert16.msg" ":defaultShaderList1.s" -na;
connectAttr "yuheng_Model_place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "yuheng_Builder:defaultRenderLayer.msg" ":defaultRenderingList1.r" -na
		;
connectAttr "yuheng_Builder:defaultRenderLayer1.msg" ":defaultRenderingList1.r" 
		-na;
connectAttr "yuheng_Builder:Elisa_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "yuheng_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na
		;
connectAttr "yuheng_Model_file2.msg" ":defaultTextureList1.tx" -na;
// End of yuheng_Builder.ma
