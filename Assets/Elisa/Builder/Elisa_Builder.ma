//Maya ASCII 2017ff04 scene
//Name: Elisa_Builder.ma
//Last modified: Fri, Aug 03, 2018 12:02:54 PM
//Codeset: 936
requires maya "2017ff04";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "2507076C-485C-4D9E-6935-64AF7B6F76FF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 211.92728849902525 174.38056561371965 218.29934420235855 ;
	setAttr ".r" -type "double3" -9.3383527295853241 402.59999999986979 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "FE873ED0-4D62-874C-B800-B8874E234E17";
	setAttr -k off ".v" no;
	setAttr ".fl" 85;
	setAttr ".coi" 308.9478207197003;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -6.4392935428259079e-015 100.97468777030899 -1.9155815877663294 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "FF2092AB-45CA-E71D-10FD-529331E7BAC9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "5A6CA9B1-4D84-9F36-D576-3EB84C0C7841";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "F30C9614-4F5F-5FE8-19DC-94B9564C53C1";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9322B862-422A-AEC8-1CF2-578AF98C07D5";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "1E0B2365-4396-7E1C-9774-B287A6729515";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "F622784D-4EDA-F624-8C79-B5B2527F1E42";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Elisa_BuilderGrp";
	rename -uid "BCC1975D-4BA7-88B8-C5EA-9AB6171D28A4";
createNode joint -n "Root" -p "Elisa_BuilderGrp";
	rename -uid "67025C7D-4227-C59B-C525-7185E20A996D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ds" 2;
	setAttr ".sd" 2;
	setAttr ".radi" 0.5;
createNode joint -n "C_Pelvis" -p "Root";
	rename -uid "C602E770-4D02-122A-8D80-CCB8F6AB8658";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -6.4455392890319055e-015 100.97468777030899 -1.9155815877663294 ;
	setAttr ".r" -type "double3" -8.0512616689363416e-018 2.4928266815948801e-016 0.036618413472465881 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -90 -13.533085405026004 90 ;
	setAttr ".bps" -type "matrix" 4.4408920985006262e-016 0.97223495543719041 0.23400681918705785 0
		 -3.3306690738754696e-016 0.2340068191870579 -0.97223495543719041 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -6.4455392890319039e-015 100.97468777030896 -1.9155815877663289 1;
	setAttr ".typ" 1;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "C_Spine_0" -p "C_Pelvis";
	rename -uid "7F3EC54D-461B-4230-6CDD-179942CE8F8A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 4.9999999999999574 -1.0658141036401503e-014 1.1102230246251629e-015 ;
	setAttr ".r" -type "double3" 2.1222660974001147e-017 6.0295672759978503e-015 -0.084029666165203298 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 4.9091621920272743 ;
	setAttr ".bps" -type "matrix" 4.1395750754731127e-016 0.98869385804653387 0.14994817458395523 0
		 -3.6984858124261542e-016 0.14994817458395529 -0.98869385804653387 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -5.3353162644067695e-015 105.83586254749487 -0.74554749183103919 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "C_Spine_1" -p "C_Spine_0";
	rename -uid "05667D6F-49F7-38A6-66BF-29954DC8EA66";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.0000000000000284 7.1054273576010019e-015 1.5258969225993073e-015 ;
	setAttr ".r" -type "double3" -1.1052494311875609e-017 7.5340731396439421e-015 0.047619022632650838 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 5.0516930573191647 ;
	setAttr ".bps" -type "matrix" 3.7978272818216287e-016 0.99805704421244823 0.062306793352821133 0
		 -4.0486277981122344e-016 0.062306793352821188 -0.99805704421244823 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -4.7914256492695083e-015 110.77933183772758 0.0041933810887363476 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Spine_2" -p "C_Spine_1";
	rename -uid "9595DE26-45AE-575A-8A5F-90986F228BF8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.9999999999999716 -4.4408920985006262e-015 1.4892484008161127e-015 ;
	setAttr ".r" -type "double3" -1.1203004736840574e-017 6.1185605885910957e-015 0.047564153761668268 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 5.0518070665797223 ;
	setAttr ".bps" -type "matrix" 3.4265666894241041e-016 0.99966659224587928 -0.025820618650819249 0
		 -4.3673241044288111e-016 -0.025820618650819194 -0.99966659224587928 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -4.3817604091748187e-015 115.76961705878978 0.31572734785284201 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Spine_3" -p "C_Spine_2";
	rename -uid "71714EE1-452B-AB04-B469-478503F8361A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 5.0000000000000284 -8.8817841970012523e-016 1.4446455865051974e-015 ;
	setAttr ".r" -type "double3" 1.7919181709645365e-017 7.5082286307770891e-015 -0.084141846756406749 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 4.9089317573934581 ;
	setAttr ".bps" -type "matrix" 3.0402762245271328e-016 0.99379025555777634 -0.11126961830800715 0
		 -4.6445236126830941e-016 -0.11126961830800709 -0.99379025555777634 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -4.1131226509679485e-015 120.76795002001921 0.18662425459874643 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_ChestBegin" -p "C_Spine_3";
	rename -uid "2C25ABE3-435E-9E66-74D4-8690B0E96688";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 5.0000000000000568 -3.5527136788005009e-015 1.3924279340154764e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 5 ;
	setAttr ".bps" -type "matrix" 2.6239101504358873e-016 0.98031079737301496 -0.19746073167565195 0
		 -4.8918273306235261e-016 -0.1974607316756519 -0.98031079737301496 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -3.9854124727198454e-015 125.73690129780813 -0.36972383694129407 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.65517241379310198;
createNode joint -n "C_ChestEnd" -p "C_ChestBegin";
	rename -uid "24325C6C-4944-1852-CED6-E385F6CDF502";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 24.912029405115021 -1.4210854715202004e-014 5.6988077785042318e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 6.0480597069556706e-017 0.98017587611435708 -0.19812938167634997 0
		 -3.957012367318657e-016 -0.19812938167635016 -0.9801758761143573 0 -1.0000000000000002 2.2204460492503136e-016 3.3306690738754696e-016 0
		 -1.360977951735926e-014 150.15467294050094 -5.3054764838503967 1;
	setAttr ".radi" 0.65517241379310198;
createNode joint -n "L_Clav" -p "C_ChestBegin";
	rename -uid "1EB1FF0B-4ACA-7073-3BCD-2A8EF768306F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 23.187386247869398 -0.45595805285650215 -1.592009249416614 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -155.63744465116028 83.689332346217171 103.06608621941064 ;
	setAttr ".bps" -type "matrix" 0.97096663178489029 -0.2182805091616899 -0.097864290118605063 0
		 0.21724984896944244 0.97588583281488528 -0.021197745963959305 0 0.10013142904732562 -0.00067869824771151779 0.99497398774321189 0
		 1.5920092494166163 148.55778021018349 -4.5013414887271281 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "L_Shoulder" -p "L_Clav";
	rename -uid "A8BCA1A6-4342-D0BF-5413-D99271F5EFA0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 14.156335756500543 -5.6843418860808015e-014 1.2434497875801753e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.8318010869040746 -4.0255041696906355 -1.7751227472604272 ;
	setAttr ".bps" -type "matrix" 0.2666003241590032 -0.96346582504763489 0.025648998491068199 0
		 0.95879185923477384 0.26783043732062622 0.094789385005749988 0 -0.098195915513021717 -0.00067882981860458499 0.99516687111591351 0
		 15.337338897321946 145.4677280333907 -5.886741238217672 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "L_Elbow" -p "L_Shoulder";
	rename -uid "2A102F9F-4C97-F2BF-BC9C-5E8DADD69E03";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 28.765225070072546 5.6843418860808015e-014 8.8817841970012523e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 46.601122260938908 -10.818013126092209 10.064211981515268 ;
	setAttr ".bps" -type "matrix" 0.42895584358440458 -0.86277461866033289 0.26761323145597482 0
		 0.46607536058277577 0.46516195685258321 0.7525942546649631 0 -0.77380271549822566 -0.19810177003902046 0.60165193109885373 0
		 23.006157225510016 117.75341672857235 -5.148942023800136 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "L_Wrist" -p "L_Elbow";
	rename -uid "FC3037B9-495D-4861-4820-72AD9C3ED993";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 24.749212695744731 1.4210854715202004e-014 -1.4210854715202004e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.49999999612681695 0 0.49999999612681695 ;
	setAttr ".bps" -type "matrix" 0.42895584358440458 -0.86277461866033289 0.26761323145597482 0
		 0.46607536058277577 0.46516195685258321 0.7525942546649631 0 -0.77380271549822566 -0.19810177003902046 0.60165193109885373 0
		 33.622476635463073 96.400424182857748 1.4742747616993492 1;
	setAttr ".sd" 1;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "L_Index_0" -p "L_Wrist";
	rename -uid "86078738-4D05-A9BB-98F3-21970821E854";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.1738375533686138 0.97436429998380447 1.202889792915613 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 127.78225929582563 -1.3956301735703993 0.23245950081782774 ;
	setAttr ".bps" -type "matrix" 0.41186876465116534 -0.86544984892921928 0.28523793522796859 0
		 -0.90416128294366405 -0.42708011939710511 0.0097440259350527469 0 0.11338648566029086 -0.26191435738452062 -0.95840720691440073 0
		 34.507240604818904 93.877060305389605 3.7806576263978822 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_1" -p "L_Index_0";
	rename -uid "EAEF5586-49F6-397E-7439-3A916ABDF697";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 7.3299559333269286 -2.8421709430404007e-014 -3.5527136788005009e-014 ;
	setAttr ".r" -type "double3" 1.3914926731402885e-014 -2.7829853462805791e-015 1.7691835415640811e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.290329191703636 -12.050114242915191 21.733404124073679 ;
	setAttr ".bps" -type "matrix" 0.070409717008542899 -0.99555393557109495 0.062568627279821931 0
		 -0.98388301354174001 -0.058975043020250723 0.16880805657546372 0 -0.1643675375942652 -0.073445937053481514 -0.98366102236265041 0
		 37.526220500025737 87.533351050233975 5.871439122132065 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_2" -p "L_Index_1";
	rename -uid "1A265582-46DF-8DA6-B105-72B49BFA4C47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.5828818255349191 2.8421709430404007e-014 2.1316282072803006e-014 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 10.602423120057919 ;
	setAttr ".bps" -type "matrix" -0.11181985682751612 -0.98940839978992168 0.09255991596917397 0
		 -0.98004062783349577 0.12520668015518457 0.15441390818266887 0 -0.1643675375942652 -0.073445937053481514 -0.98366102236265041 0
		 37.848899912445233 82.970845012565491 6.15818374694142 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_3" -p "L_Index_2";
	rename -uid "1B1E3184-404E-AF58-0556-F28322DEC2C5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.7218692266728324 2.8421709430404007e-014 7.1054273576010019e-015 ;
	setAttr ".r" -type "double3" 0 0 3.975693351829396e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 3.7411148802045662 ;
	setAttr ".bps" -type "matrix" -0.17552764376574342 -0.9791304897451969 0.10243793401556563 0
		 -0.97065614862279892 0.18949717248990022 0.14804547530772044 0 -0.1643675375942652 -0.073445937053481514 -0.98366102236265041 0
		 37.544540885215433 80.27780473656567 6.4101197338413458 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Index_4" -p "L_Index_3";
	rename -uid "B219649E-4DA0-6CB3-2085-CEA1D3CB11E1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.9999999999999714 2.8421709430404007e-014 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.1755276437657432 -0.97906038632627412 0.10310580100408367 0
		 -0.97065614862279881 0.18959811414055766 0.14791617982864455 0 -0.1643675375942652 -0.07411690118314071 -0.98361069409813107 0
		 37.193485597683932 78.323920645375111 6.6473909468357233 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Middle_0" -p "L_Wrist";
	rename -uid "AD434EEE-4BF4-0C49-4287-C8A912E8A147";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.2075331031474974 -0.097778705709373526 0.52409217628962779 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 124.48443189000257 6.3404489497649115 -8.0658391393389834 ;
	setAttr ".bps" -type "matrix" 0.44257473503976497 -0.89200495251460643 0.091949815627311748 0
		 -0.89657007562281144 -0.43821634605744064 0.064253665621286038 0 -0.01702067572654864 -0.11087650218815649 -0.99368843097840864 0
		 34.547250508843504 93.483739511076408 2.5743864382276556 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_1" -p "L_Middle_0";
	rename -uid "53DC7332-4E56-BCA0-EB50-0B8C33F71A38";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 6.8443709563816952 2.8421709430404007e-014 -3.5527136788005009e-014 ;
	setAttr ".r" -type "double3" 2.1568136433674469e-014 -1.9878466759147091e-016 6.0629323615398278e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.4161136110103119 -1.8568497434327778 20.269793279669827 ;
	setAttr ".bps" -type "matrix" 0.10395166292759697 -0.9916543542450299 0.076260694210451674 0
		 -0.97763766958905673 -0.087786495679905499 0.19109714329816851 0 -0.18280765513256275 -0.094420193195707297 -0.97860420413046445 0
		 37.576396171377979 87.37852672113678 3.203725085751906 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_2" -p "L_Middle_1";
	rename -uid "928A0EA0-426F-C170-3C91-9582F21EE2DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.7750551437278048 5.6843418860808015e-014 0 ;
	setAttr ".r" -type "double3" 0 0 9.5416640443905503e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 26.434714595973528 ;
	setAttr ".bps" -type "matrix" -0.3421398764293016 -0.9270497537013882 0.15335924856081617 0
		 -0.92169499628775065 0.36285476609668638 0.13716687843296052 0 -0.18280765513256275 -0.094420193195707297 -0.97860420413046445 0
		 38.072771094139426 82.643322496098961 3.5678741059057839 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_3" -p "L_Middle_2";
	rename -uid "0F98C68A-4363-DA36-7E5D-3F9404910EF0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 3.3738546452201845 -2.8421709430404007e-014 7.1054273576010019e-015 ;
	setAttr ".r" -type "double3" 0 0 1.1131941385122309e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 7.8475247473755534 ;
	setAttr ".bps" -type "matrix" -0.46478147176281875 -0.86882465117332019 0.17065142548349047 0
		 -0.86634839685366916 0.48603348920670486 0.11494304084473086 0 -0.18280765513256275 -0.094420193195707297 -0.97860420413046445 0
		 36.918440882733378 79.515591378223291 4.0852859190501727 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Middle_4" -p "L_Middle_3";
	rename -uid "9E6C5F51-4E49-2FF1-7D55-239984600C3B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.3070561573098161 -2.8421709430404007e-014 7.1054273576010019e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.46478147176281859 -0.8687080431890063 0.17124403407043445 0
		 -0.86634839685366938 0.48611178182206727 0.11461147779717586 0 -0.18280765513256267 -0.095087703056192907 -0.97853956994718982 0
		 35.846163926499479 77.514084166395477 4.511935600014052 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Ring_0" -p "L_Wrist";
	rename -uid "B7AD9A8C-4FFE-452D-87DC-FEA9E64E3113";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.2996648197607499 -1.0541042567994339 -0.36474092397219238 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 105.16687027798419 4.2724997429357003 -17.404166132667587 ;
	setAttr ".bps" -type "matrix" 0.32680805478370734 -0.94497711469597612 -0.014654283652138236 0
		 -0.87529203898782948 -0.30848380291422528 0.37242662340937227 0 -0.35645524517534871 -0.10888524252829515 -0.92794593708175521 0
		 34.828832637612706 93.135483750106843 1.3445488380933206 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_1" -p "L_Ring_0";
	rename -uid "F2495954-41B1-859A-4B31-AD8407DF45A1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 6.272130349944689 2.8421709430404007e-014 -2.8421709430404007e-014 ;
	setAttr ".r" -type "double3" -8.2495637050459938e-015 1.7890620083232288e-015 1.3014183706379036e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.57441742890388825 -4.0470930829116609 21.932371729151974 ;
	setAttr ".bps" -type "matrix" -0.048874618494956119 -0.99701866516171789 0.059708064665664556 0
		 -0.93751071449562839 0.066412347372696537 0.34155974634365982 0 -0.34450679510405802 -0.039283348070078009 -0.93796155928243463 0
		 36.878615356627982 87.208464109019019 1.2526352608420734 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_2" -p "L_Ring_1";
	rename -uid "B3F7CAB8-49E3-880C-0840-6D829DD96A11";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.2389573518237622 2.8421709430404007e-014 1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 0 0 5.0888874903416268e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 36.679824481650378 ;
	setAttr ".bps" -type "matrix" -0.5992120192292536 -0.75992411060995335 0.25191328294647908 0
		 -0.72267560090149141 0.64882367764907944 0.23825996554937964 0 -0.34450679510405802 -0.039283348070078009 -0.93796155928243463 0
		 36.671437933241215 82.982144508426217 1.5057352005197697 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_3" -p "L_Ring_2";
	rename -uid "16622E0D-4DFE-D67A-58B0-FF9DDAC17FF2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 3.2318061069925932 2.8421709430404007e-014 -1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 0 0 2.7829853462805771e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 4.2167909545143392 ;
	setAttr ".bps" -type "matrix" -0.65072860770563679 -0.71015866797307492 0.26875071240127396 0
		 -0.67665895932930231 0.70294486616456131 0.21909168832311304 0 -0.34450679510405802 -0.039283348070078009 -0.93796155928243463 0
		 34.734900870112725 80.52621712690609 2.3198700867787529 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Ring_4" -p "L_Ring_3";
	rename -uid "61B5F2F1-4448-9F03-8833-71853F22B36B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.4799134091834532 -5.6843418860808015e-014 2.8421709430404007e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.65072860770563667 -0.70997518078224697 0.2692350678992238 0
		 -0.67665895932930253 0.70309415086468618 0.21861214005459767 0 -0.34450679510405802 -0.039923147334365028 -0.93793454485590277 0
		 33.121150270124268 78.76698671202999 3.0184408557943465 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Pinky_0" -p "L_Wrist";
	rename -uid "D691909F-45C3-E821-0CBD-869D7DA67629";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.1620220848973872 -2.3230212469970581 -0.57287282755116564 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 86.493930796355272 -0.75548219156717156 -29.184287180140856 ;
	setAttr ".bps" -type "matrix" 0.13701902190565271 -0.982599633236522 -0.12539437148241814 0
		 -0.73654920213874675 -0.18570794836406668 0.65039052171997813 0 -0.66236021956696223 0.003243251125286048 -0.74917849732713515 0
		 34.339432070581402 92.705217796446703 0.22751122284903458 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_1" -p "L_Pinky_0";
	rename -uid "796DF2AE-4941-A988-716D-4BB7B118BF74";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.9700611425120798 2.8421709430404007e-014 4.2632564145606011e-014 ;
	setAttr ".r" -type "double3" -8.4980445395353328e-015 8.3489560388417272e-015 -1.2945851476894468e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.7110016157149444 -3.2056117956273971 19.59949028800014 ;
	setAttr ".bps" -type "matrix" -0.15484431076205557 -0.9862354728160152 0.057989926573459721 0
		 -0.80131607639977176 0.15971042016390163 0.57652851394735483 0 -0.57785446708310517 0.042803899944294642 -0.81501658941500055 0
		 35.020424987139677 87.821637540651253 -0.39570647034545636 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_2" -p "L_Pinky_1";
	rename -uid "9588F872-4359-CB40-20FC-DAAFD2F4C561";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 3.5642773452594958 0 1.4210854715202004e-014 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 25.061569604295762 ;
	setAttr ".bps" -type "matrix" -0.47969722473379034 -0.82573243664678531 0.29674318130677046 0
		 -0.66028386884339407 0.56243556894894364 0.4976860891428227 0 -0.57785446708310517 0.042803899944294642 -0.81501658941500055 0
		 34.468516918248163 84.306420787801827 -0.18901428880640841 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_3" -p "L_Pinky_2";
	rename -uid "43910F3A-4D54-4CF9-7DFA-3991FB64BD3A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 1.7506404229104859 -2.8421709430404007e-014 -2.8421709430404007e-014 ;
	setAttr ".r" -type "double3" 0 0 2.5444437451708134e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.0210688115630244 ;
	setAttr ".bps" -type "matrix" -0.54631084571130917 -0.76218098594540029 0.34731053039246063 0
		 -0.60632390248966361 0.64594734368434148 0.46381392223266454 0 -0.57785446708310517 0.042803899944294642 -0.81501658941500055 0
		 33.628739565871221 82.860860205699581 0.3304763196122818 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "L_Pinky_4" -p "L_Pinky_3";
	rename -uid "A48B49CF-44EA-CD27-A275-6E830BC853D5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.449333433366931 -1.4210854715202004e-014 1.4210854715202004e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.54631084571130906 -0.76194389892066927 0.34783035341350488 0
		 -0.60632390248966372 0.64626357315736205 0.46337319654851011 0 -0.57785446708310517 0.042247945600333889 -0.81504559747578054 0
		 32.290642146459575 80.994694534566293 1.2117278882745066 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "L_Thumb_0" -p "L_Wrist";
	rename -uid "45CE8734-4525-7313-F5FC-67BEFE0C8889";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.2111527720921202 0.81958437676492224 2.4773443349515247 ;
	setAttr ".r" -type "double3" -7.1562480332929135e-015 -6.3611093629270351e-015 -2.5444437451708134e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -161.12996726222229 -29.321458134774044 10.899696023625644 ;
	setAttr ".bps" -type "matrix" 0.06515488578479478 -0.75899365338971603 0.647829819452997 0
		 -0.057443016857054358 -0.65098551735404264 -0.75691357235132795 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.035975848428933 94.38317086786796 4.1733219965685979 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_1" -p "L_Thumb_0";
	rename -uid "D838E852-4337-F9CD-7385-938FCA62F006";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 5.4665225392128818 5.3290705182007514e-015 -5.6843418860808015e-014 ;
	setAttr ".r" -type "double3" 0 0 6.3611093629270335e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 9.0441670532607468 ;
	setAttr ".bps" -type "matrix" 0.055315044607155472 -0.85188961456470313 0.52079202224775933 0
		 -0.066970927777490766 -0.52358150682332216 -0.84933933180163101 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.392146500111309 90.234114954493521 7.71469830618262 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_2" -p "L_Thumb_1";
	rename -uid "210650DD-4E9B-A24C-82D3-A788C0DD12DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.4781282901164801 -7.9936057773011271e-014 0 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 22.560097226313395 ;
	setAttr ".bps" -type "matrix" 0.025388657566857317 -0.98757423775451036 0.15508881645866962 0
		 -0.083067896291060248 -0.15668642128205185 -0.98414891657289383 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.584539321628554 87.27113358601963 9.5260797720295969 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_3" -p "L_Thumb_2";
	rename -uid "D811B7D4-477A-E856-07A9-C4B7EC34E4D2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.4126775211040403 1.4210854715202004e-014 5.6843418860808015e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.025388657566857473 -0.98746821781080185 0.15576243090203795 0
		 -0.08306789629106022 -0.15735769885150874 -0.98404180765754823 0 0.99622042775318087 0.012044643029874957 -0.086022008239475256 0
		 33.671182622597989 83.907583529576485 10.083935269972683 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Clav" -p "C_ChestBegin";
	rename -uid "17FE7018-466F-6708-FEF3-D3A7EDFAEFC4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 23.1878185015442 -0.45605044414922702 1.5920100000000026 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 24.362555348840807 96.310667653782758 103.06608621941088 ;
	setAttr ".bps" -type "matrix" 0.97096663178489051 0.21828050916169012 0.097864290118605174 0
		 0.21724984896944344 -0.97588583281488517 0.021197745963948203 0 0.10013142904732321 0.00067869824772238128 -0.99497398774321211 0
		 -1.5920100000000004 148.55822219678041 -4.5013362696721906 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "R_Shoulder" -p "R_Clav";
	rename -uid "A73324E5-4B02-418A-3AA0-778CC34613CB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -14.156298847997228 1.1869534887409827e-005 1.2307080263340708e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.8318010869034493 -4.0255041696905751 -1.7751227472604092 ;
	setAttr ".bps" -type "matrix" 0.26235226505945086 0.96470156178127819 -0.022851383217186154 0
		 0.96011801640670313 -0.26333161408024858 -0.093967311322336461 0 -0.096667903615593617 0.0027125122403274561 -0.99531299533760365 0
		 -15.337299999999994 145.46816650143637 -5.8867444007556049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "R_Elbow" -p "R_Shoulder";
	rename -uid "C32922B9-449D-BA46-CBC6-43B1575D4EC0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -28.765438172109121 -2.5747077273763352e-005 1.7582392288773008e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 46.601122260938965 -10.818013126092225 10.064211981515264 ;
	setAttr ".bps" -type "matrix" 0.43389320214860133 0.85690266771633017 -0.27830649864828944 0
		 0.46157048511156973 -0.47669839186407365 -0.74813857704844777 0 -0.77375020284527474 0.19615417725565557 -0.60235717173621639 0
		 -22.884002750078423 117.71811015626857 -5.2294136802891966 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "R_Wrist" -p "R_Elbow";
	rename -uid "8FC17B6A-4D0C-7143-AEB5-46B5B3DF6611";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -24.749402835041167 0.00011680449749462696 -6.0133695768627149e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.49999999612681695 0 0.49999999612681695 ;
	setAttr ".bps" -type "matrix" 0.42895584361388206 0.86277461858135351 -0.26761323166335294 0
		 0.46607536049615472 -0.46516195703129459 -0.75259425460814888 0 -0.77380271553405833 0.19810176996336093 -0.60165193107768 0
		 -33.622499955472293 96.510213366543951 1.6584548023795049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "R_Index_0" -p "R_Wrist";
	rename -uid "3A0F321A-41A9-3645-F50E-D79C6F6F9A88";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.1738177393680473 -0.97432715572625739 -1.2029391052280687 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 127.78225929582565 -1.3956301735704473 0.23245950081791769 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_1" -p "R_Index_0";
	rename -uid "44E2F8DC-4563-9EE5-6928-C993D4CF2E09";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -7.3299806413089641 1.0302791338290263e-005 -5.4059538125983408e-006 ;
	setAttr ".r" -type "double3" 3.9756933518293348e-016 -1.3119788061037007e-014 5.3671860249696848e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.290329191703712 -12.050114242915285 21.733404124073683 ;
	setAttr ".bps" -type "matrix" 0.070409717061975116 0.99555393555438121 -0.062568627485633771 0
		 -0.98388301355159469 0.058975043043975897 -0.1688080565097374 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.526199955645332 87.643111883799548 6.0556173428662277 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_2" -p "R_Index_1";
	rename -uid "9456B0C1-4640-644E-630D-5F84FB81D6B9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.5828741417517591 2.0261526799458807e-005 7.2619051252331701e-006 ;
	setAttr ".r" -type "double3" 0 0 -1.5902773407317584e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 10.602423120057919 ;
	setAttr ".bps" -type "matrix" -0.11181985677680931 0.98940839977785855 -0.092559916159378919 0
		 -0.98004062785301338 -0.12520668012878922 -0.15441390808019673 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.848899955890239 83.080615224110034 6.3423652107990893 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_3" -p "R_Index_2";
	rename -uid "7C172C5B-4A50-F149-947D-DDB4B5FADF82";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7219053953956811 -3.5668591692683549e-005 -1.1995798502084654e-005 ;
	setAttr ".r" -type "double3" 0 0 1.6697912077683464e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 3.7411148802044698 ;
	setAttr ".bps" -type "matrix" -0.17552764371641655 0.97913048973488204 -0.10243793419867887 0
		 -0.97065614864558369 -0.18949717246277237 -0.14804547519305628 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.54449995602824 80.387542747408176 6.5942982539178967 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Index_4" -p "R_Index_3";
	rename -uid "B7154A37-46C3-00B9-8D44-668E207D9E1F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.9999697926522744 4.9963689633614194e-005 9.0513276944648169e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.2074182697257333e-006 0 0 ;
	setAttr ".bps" -type "matrix" -0.17552764376574126 0.97906038632627457 -0.10310580100408247 0
		 -0.97065615208658595 -0.1895981125786585 -0.14791615910060019 0 -0.16436751713921696 0.074116905178621365 0.98361069721523109 0
		 -37.193500000000043 78.323900000000023 6.6473899999999677 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Middle_0" -p "R_Wrist";
	rename -uid "BA7FF566-4BA8-A5C2-B1A1-61B503AC04FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.2075150865388196 0.09775162082817701 -0.52406473860693836 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 124.48443189000264 6.3404489497649115 -8.0658391393390225 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_1" -p "R_Middle_0";
	rename -uid "A00A2B33-4449-6456-AB19-C488CCF1ED78";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -6.8443664496872572 -4.8595775979265454e-005 -5.7851356096705331e-006 ;
	setAttr ".r" -type "double3" 9.9392333795734689e-017 -2.5842006786891076e-015 9.4422717105948153e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.4161136110104025 -1.8568497434327316 20.269793279669781 ;
	setAttr ".bps" -type "matrix" 0.10395166297972064 0.9916543542235956 -0.076260694418124136 0
		 -0.97763766959898024 0.087786495698780886 -0.19109714323873037 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -37.576399955864808 87.488331567080024 3.3879011425116676 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_2" -p "R_Middle_1";
	rename -uid "AF1BAB77-4975-4065-D627-63830A355F81";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.7751027239195807 2.0346113984714975e-005 1.313243956246879e-006 ;
	setAttr ".r" -type "double3" 0 0 -9.5416640443905503e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 26.434714595973528 ;
	setAttr ".bps" -type "matrix" -0.34213987638704557 0.92704975369059783 -0.15335924872031434 0
		 -0.92169499631984086 -0.36285476607024247 -0.13716687828728594 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -38.072799956113705 82.753082069150992 3.7520511892174429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_3" -p "R_Middle_2";
	rename -uid "F54BDA8E-4722-BAB2-56F3-529160222037";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.3739001643750584 -5.6796370586198464e-005 -1.0206056913375505e-005 ;
	setAttr ".r" -type "double3" 0 0 2.0673605429512861e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 7.8475247473755489 ;
	setAttr ".bps" -type "matrix" -0.4647814717253399 0.86882465116624141 -0.17065142562160487 0
		 -0.86634839689122833 -0.48603348917903533 -0.11494304067864308 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -36.918399956256252 79.6253283979663 4.2694677865740021 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Middle_4" -p "R_Middle_3";
	rename -uid "2A2BF087-4E16-663C-FCBC-F2972AA45FA0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.3069698639193348 3.8314309790621337e-005 1.9994370980214171e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.46478147176281848 0.86870804318900663 -0.17124403407043384 0
		 -0.86634839685366949 -0.48611178182206682 -0.11461147779717742 0 -0.18280765513256333 0.095087703056191936 0.97853956994718994 0
		 -35.846200000000053 77.514099999999985 4.5119399999999752 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Ring_0" -p "R_Wrist";
	rename -uid "5904E05A-44CC-5BE3-C487-F4B35335F464";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.299616180218635 1.054118152763678 0.36470388434092627 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 105.16687027798422 4.2724997429357119 -17.404166132667598 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_1" -p "R_Ring_0";
	rename -uid "DED06599-4742-24A0-93CF-2D83F14F8047";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -6.2721539830266551 9.0411416522329091e-006 4.6116979319776874e-006 ;
	setAttr ".r" -type "double3" 7.9513867036587888e-015 1.6399735076296259e-015 -6.6530743434520031e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.57441742890395686 -4.0470930829116503 21.932371729151967 ;
	setAttr ".bps" -type "matrix" -0.048874618441212436 0.99701866515257287 -0.059708064862364088 0
		 -0.93751071452645818 -0.066412347386439724 -0.34155974625636643 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.878599956028665 87.318262414793537 1.436814679904429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_2" -p "R_Ring_1";
	rename -uid "3982859B-4BE2-3D76-863C-A98A24844A7E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.2390121537885364 -1.6620677314449495e-005 -1.2528417812518455e-005 ;
	setAttr ".r" -type "double3" 0 0 1.2722218725854067e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 36.679824481650385 ;
	setAttr ".bps" -type "matrix" -0.5992120192045679 0.7599241105944099 -0.25191328305208532 0
		 -0.72267560095831995 -0.64882367765463878 -0.23825996536187455 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.671399956256458 83.091888787317785 1.6899118183151796 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_3" -p "R_Ring_2";
	rename -uid "CD5A86AE-49E7-7DD4-0029-7C8499D754AD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.2317296136078824 -1.9608507955126697e-005 1.56686698176145e-005 ;
	setAttr ".r" -type "double3" 0 0 -2.7034714792439894e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 4.2167909545142912 ;
	setAttr ".bps" -type "matrix" -0.65072860768519603 0.71015866795716542 -0.26875071249280685 0
		 -0.67665895938779275 -0.70294486616896223 -0.21909168812835048 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -34.734899956336264 80.636032872997248 2.504046803748186 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Ring_4" -p "R_Ring_3";
	rename -uid "867F88E1-4ACA-AA60-571C-64ABB396118C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.4798969251928611 5.0355086088416101e-005 1.6836138357234631e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.4787793334710982e-006 0 0 ;
	setAttr ".bps" -type "matrix" -0.65072860770563634 0.70997518078224808 -0.26923506789922219 0
		 -0.67665896822087535 -0.70309414983428609 -0.21861211584691231 0 -0.34450677763978116 0.039923165480920647 0.93793455049818775 0
		 -33.121200000000037 78.766999999999967 3.0184399999999769 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Pinky_0" -p "R_Wrist";
	rename -uid "61E7F6D9-4B8F-FC5C-F33E-DEB1D2008953";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.162035649364924 2.3230693516059944 0.57282264253348103 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 86.493930796355272 -0.75548219156714291 -29.184287180140839 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_1" -p "R_Pinky_0";
	rename -uid "E66D5EFC-4CCF-D751-66BE-56866D8B357F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.9700579124330062 5.787581002891784e-006 4.9266030117678383e-006 ;
	setAttr ".r" -type "double3" -2.8724384466967383e-014 9.5416640443905471e-015 -6.0380842780908956e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.7110016157148298 -3.2056117956274162 19.599490288000133 ;
	setAttr ".bps" -type "matrix" -0.15484431070880841 0.98623547281342838 -0.057989926759633319 0
		 -0.80131607645459935 -0.15971042023289406 -0.57652851385203763 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -35.020399956122709 87.931386935486174 -0.21152847538694763 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_2" -p "R_Pinky_1";
	rename -uid "19A3B394-4F3D-C0A0-4523-97AF4A1E731E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5642021881575543 -5.558667623972724e-006 1.532378220758801e-006 ;
	setAttr ".r" -type "double3" 0 0 -6.3611093629270335e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 25.061569604295773 ;
	setAttr ".bps" -type "matrix" -0.47969722470878084 0.82573243661521722 -0.29674318143504091 0
		 -0.66028386891561475 -0.56243556901034497 -0.49768608897761768 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -34.468499956312485 84.416245127431338 -0.0048361978950919871 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_3" -p "R_Pinky_2";
	rename -uid "A0900186-467E-51A9-7312-ECBA7DA4A01E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.7507288182409724 3.8280174990745763e-005 -9.5532884358817682e-006 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.0210688115630289 ;
	setAttr ".bps" -type "matrix" -0.54631084569401323 0.76218098590756578 -0.34731053050269445 0
		 -0.60632390256410917 -0.64594734374209284 -0.46381392205491606 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -33.628699956356272 82.970590433278744 0.51465380386059834 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Pinky_4" -p "R_Pinky_3";
	rename -uid "8063A56F-4B1B-80DC-B47A-0CB4BD33304F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.4492940555543896 -3.8045360639671344e-005 -1.7743270888104234e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.54631084571130817 0.76194389892066949 -0.3478303534135051 0
		 -0.60632390248966272 -0.64626357315736116 -0.46337319654851244 0 -0.57785446708310706 -0.042247945600334832 0.81504559747577898 0
		 -32.290600000000055 80.994700000000023 1.2117299999999669 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Thumb_0" -p "R_Wrist";
	rename -uid "37B89FBE-4DF9-ECD8-D7F5-BE88FEE6E668";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.2111422656271884 -0.81958823959172378 -2.4773398202668204 ;
	setAttr ".r" -type "double3" 1.9083328088781101e-014 9.5416640443905503e-015 1.5890062672980573e-030 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -161.12996726222221 -29.321458134774062 10.89969602362561 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_1" -p "R_Thumb_0";
	rename -uid "0FC40A49-4E85-698C-1473-F19ADCF20718";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.466566803521431 -4.033847644180355e-005 7.1488751530068839e-005 ;
	setAttr ".r" -type "double3" 0 0 -6.3611093629270335e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 9.0441670532607343 ;
	setAttr ".bps" -type "matrix" 0.055315044616028729 0.85188961445670097 -0.5207920224234821 0
		 -0.066970927679814024 0.52358150699809647 0.84933933170159248 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.392099955341656 90.343855173995593 7.8988800193043414 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_2" -p "R_Thumb_1";
	rename -uid "D3BCF9CC-4443-EAC1-1E1E-01941773A44A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.4780891606514999 2.226969536778256e-005 -7.8812967103658593e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 22.560097226313388 ;
	setAttr ".bps" -type "matrix" 0.02538865761252548 0.98757423772182551 -0.15508881665932572 0
		 -0.08306789620426222 0.15668642148488737 0.98414891654792691 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.5844999553725 87.380918895272671 9.7102593440773521 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_3" -p "R_Thumb_2";
	rename -uid "73837C37-46EB-0795-0610-8ABE621557C7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.4126627487090673 -2.9980727042300259e-005 -5.9790500301915017e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Neck_0" -p "C_ChestBegin";
	rename -uid "83A0A31F-48DD-C923-B412-F4BF7578FA41";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 25.359253404546507 0.4958512927685419 8.2169913231499729e-015 ;
	setAttr ".r" -type "double3" 0 0 -3.1805546814635168e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -19.295440319300116 ;
	setAttr ".bps" -type "matrix" 4.0929698190886877e-016 0.99049282793029758 0.13756437699725235 0
		 -3.749996956028749e-016 0.13756437699725241 -0.99049282793029758 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -5.7909254448923091e-015 150.49894006453104 -5.8632689451436821 1;
	setAttr ".typ" 7;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Neck_1" -p "C_Neck_0";
	rename -uid "86F17D0E-47BF-CA29-8C6E-379DF6036D16";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 6.1610734169494776 -1.0658141036401503e-014 -6.3108872417680944e-030 ;
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
	rename -uid "0F949D0A-471A-349A-F4F4-2C984BC75AED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" 5.5042648571120196 0 3.8055961791890692e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 3.9774202365524855e-016 0.99420750314017159 0.10747762883403142 0
		 -3.8723387470698558e-016 0.10747762883403147 -0.99420750314017159 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -1.0072601522555171e-015 163.08851152654773 -4.3144474094236802 1;
	setAttr ".typ" 8;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_FacialRoot" -p "C_Head";
	rename -uid "2297CC3D-4CC7-1B7F-B165-F4803C6B0705";
	setAttr ".t" -type "double3" 4.3289621916327121 -0.74056241803955558 -9.3827666486746244e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.9837095073778706 27.927043278189814 -63.230731446679862 ;
	setAttr ".radi" 1.169502703832018;
createNode joint -n "L_Eye" -p "C_FacialRoot";
	rename -uid "F0F1DFD3-4B47-A705-C6C5-709C6E3D975B";
	setAttr ".t" -type "double3" 7.0146489659534126 0 -1.3322676295501878e-015 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_Eye" -p "C_FacialRoot";
	rename -uid "3C41E4A6-4D70-D2A6-F357-EE9EB08DE0A5";
	setAttr ".t" -type "double3" 3.9374744899517466 1.0064271574354109 5.717237089249763 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_UpperTeeth" -p "C_FacialRoot";
	rename -uid "C5E109B6-4178-CA58-7A45-FAAF0799FE3D";
	setAttr ".t" -type "double3" 3.6853318353755782 -4.4677636333626367 2.7700246580312458 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidUpper" -p "C_FacialRoot";
	rename -uid "FBC760A5-4750-3D6E-158B-C7A7333179FD";
	setAttr ".t" -type "double3" 7.0531250347504511 0.030000000000029559 -1.5543122344752192e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidLower" -p "C_FacialRoot";
	rename -uid "4CF8D120-4FD1-E705-6CDA-EEAD721AB958";
	setAttr ".t" -type "double3" 7.0146489659534197 -0.030000000000001137 -8.8817841970012523e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidUpper" -p "C_FacialRoot";
	rename -uid "F9C0BA30-4A63-715D-7EA6-DEA23CD021F9";
	setAttr ".t" -type "double3" 3.9374744899517466 1.0360000000000014 5.717237089249763 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidLower" -p "C_FacialRoot";
	rename -uid "5CC7BE12-4415-A1C3-99AC-DDB67BF982FF";
	setAttr ".t" -type "double3" 3.9374744899517538 0.97600000000002751 5.717237089249763 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_Jaw" -p "C_FacialRoot";
	rename -uid "90F5DFFD-421B-F522-194C-34BDB73DAB70";
	setAttr ".t" -type "double3" -3.7649999999999935 0.47400000000004638 -2.1095561452622311 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_JawEnd" -p "C_Jaw";
	rename -uid "BF51FCB3-4D3F-F0EA-B6FB-3991FF6726BA";
	setAttr ".t" -type "double3" 3.9967486785419393e-015 -6.6417099111167204 11.642997494788872 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_LowerTeeth" -p "C_Jaw";
	rename -uid "084F43C4-4801-480B-D39B-0B917D15FC4B";
	setAttr ".t" -type "double3" 1.7129852224184727e-015 -4.1610712696152916 9.4224258076384242 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -7.5549687203861124e-014 -9.5416640443905503e-015 
		-2.1946285137169665e-017 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_Breast" -p "C_ChestBegin";
	rename -uid "3F4A639A-48A1-379E-57F8-13A94A510781";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 5.9904225855234472 -8.7864674284425064 -7.8906594358327062 ;
	setAttr ".r" -type "double3" 1.2424041724466862e-017 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 101.42759163891111 90 0 ;
	setAttr ".bps" -type "matrix" 1 1.1542575317290093e-016 -4.5543866415314589e-016 0
		 -8.9978394366786753e-017 0.99999976735171558 0.00068212646580104175 0 4.2749774439139101e-016 -0.00068212646580104175 0.99999976735171558 0
		 7.8906594358327089 133.34435952648849 7.0608718271433943 1;
	setAttr ".radi" 0.5;
createNode joint -n "R_Breast" -p "C_ChestBegin";
	rename -uid "DE9FCF47-44A5-61E8-C948-0ABE45589716";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 5.9903960095492437 -8.7864588067821288 7.8906600000000013 ;
	setAttr ".r" -type "double3" 1.2424041724466862e-017 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -78.57240836108889 89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" 1 1.1542575317290093e-016 -4.5543866415314589e-016 0
		 8.9978394366786654e-017 -0.99999976735171558 -0.00068212646580104175 0 -4.2749774439139096e-016 0.00068212646580120828 -0.99999976735171558 0
		 -7.8906599999999987 133.34433177133462 7.0608686229479503 1;
	setAttr ".radi" 0.5;
createNode joint -n "L_Hip" -p "C_Pelvis";
	rename -uid "FDCC3C92-4C16-DECA-0427-1296E2AB81F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.3722824643070339 -0.021250189231771799 -8.2375185657379042 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.47814130335209315 177.49683574053523 14.344960822759923 ;
	setAttr ".bps" -type "matrix" 0.043676214271235199 -0.99879915221154247 0.022195536678289531 0
		 -1.3016897375709995e-012 -0.022216737247663959 -0.99975317783244289 0 0.99904573884629189 0.043665434013329334 -0.00097034297773684842 0
		 8.2375185657378971 99.635534100586924 -2.216044865484212 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "L_Knee" -p "L_Hip";
	rename -uid "EBA2F9A7-49FD-C8E2-FBC5-B9A557B5BE02";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 42.574412456291974 -1.3877787807814457e-014 -1.9539925233402755e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.58621665556659364 -0.0041968062664413186 2.4732599614514643 ;
	setAttr ".bps" -type "matrix" 0.043710370994654149 -0.99896923390645298 -0.012242270045392802 0
		 3.5279161363088729e-010 0.012253981865250589 -0.99992491714550547 0 0.99904424499994482 0.04370708909091002 0.00053562644591981657 0
		 10.097007726650844 57.112247033337979 -1.2710829322539472 1;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "L_Ankle" -p "L_Knee";
	rename -uid "773EF858-4239-8FAF-8E7D-868B67BA6A2F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 42.882476181269681 1.4344081478157023e-013 3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -5.4684461863108611 -3.0414879273729563 -34.681075462258875 ;
	setAttr ".bps" -type "matrix" 0.089586411029085392 -0.82001406268021293 0.5652886094426629 0
		 -0.078021190938229235 -0.57160461050695421 -0.81681139990316831 0 0.99291840990260027 0.02907071127243591 -0.11518647933940221 0
		 11.971416669703574 14.273972654523305 -1.7960617858803198 1;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "L_Ball" -p "L_Ankle";
	rename -uid "C88DA5A0-4826-BB0C-1006-24B9FC813BC5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 11.395686988248077 -3.3750779948604759e-014 -5.3290705182007514e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.81869390397467467 0.97121500689738305 -40.319578859158966 ;
	setAttr ".bps" -type "matrix" 0.10215059601859774 -0.24737070314834397 0.96352114193562921 0
		 -0.023522797391771579 -0.96891771037355545 -0.2462623571058577 0 0.99449079117702799 0.002491133950868047 -0.10479437253845231 0
		 12.992315368191564 4.9293490702579756 4.6457902653503096 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "L_Toe" -p "L_Ball";
	rename -uid "D253813E-4A98-670B-3054-6A8B2EF78F0B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 10.186729757111326 6.2172489379008766e-015 -1.7763568394002505e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0.49999999612681695 0 0.49999999612681695 ;
	setAttr ".bps" -type "matrix" 0.10215059877882557 -0.24737070206271949 0.96352114192171456 0
		 -0.023522787492969086 -0.96891771062446264 -0.24626235706419144 0 0.9944907911276446 0.002491144164384583 -0.10479437276430556 0
		 14.032896887052129 2.4096571554708217 14.460000745352577 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Hip" -p "C_Pelvis";
	rename -uid "D9C12AD8-41AC-863B-C432-048605BBBB26";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.3723210485636628 -0.021263491402351065 8.2375199999999964 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -179.52185869664791 2.5031642594647034 14.344960822759946 ;
	setAttr ".bps" -type "matrix" 0.04367621427123513 0.99879915221154247 -0.022195536678289766 0
		 -1.3006955835555549e-012 0.022216737247664126 0.999753177832443 0 0.99904573884629189 -0.043665434013329021 0.00097034297773582754 0
		 -8.2375200000000035 99.635493474825282 -2.2160409616281522 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "R_Knee" -p "R_Hip";
	rename -uid "6D77859D-42E1-9356-EB2E-5AA3B45517D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -42.574325050574338 -2.3314683517128287e-015 5.7859833226814317e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0.58621665557503799 -0.0041968062665338939 2.4732599614512805 ;
	setAttr ".bps" -type "matrix" 0.043710370994654441 0.99896923390645309 0.012242270045389339 0
		 3.5294000512962886e-010 -0.012253981865253649 0.99992491714550569 0 0.99904424499994482 -0.043707089090908237 -0.00053562644606822672 0
		 -10.096999562900118 57.112293455685503 -1.2710809628003075 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 2;
createNode joint -n "R_Ankle" -p "R_Knee";
	rename -uid "462D7223-48BA-C126-E4EE-27AF2B552CBF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -42.882501399175524 -8.3327106015218533e-007 1.0495371295604627e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -5.468446186317987 -3.0414879273777697 -34.681075462258313 ;
	setAttr ".bps" -type "matrix" 0.089586411029085211 0.82001406268021293 -0.56528860944266346 0
		 -0.078021190938231205 0.57160461050695421 0.81681139990316831 0 0.99291840990260016 -0.029070711272434359 0.11518647933940374 0
		 -11.971399122896578 14.273993436447512 -1.7960609639808891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "R_Ball" -p "R_Ankle";
	rename -uid "C161FD79-444D-CDF1-9127-46BB6C9A28E6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -11.39569940644183 -1.0971067688991809e-005 -9.5427450297336236e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -0.81869390397696495 0.97121500689750517 -40.31957885915898 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Toe" -p "R_Ball";
	rename -uid "F6C386E1-4DE4-D13C-A0DF-E4B110FE7B91";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -10.186732610927155 -8.7764594436379184e-007 -1.9291117473230202e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0.50000190515003462 0 0.49999999612681634 ;
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.97517567709196495;
createNode transform -n "locator_L_LegPV" -p "Elisa_BuilderGrp";
	rename -uid "6DD4C931-43FE-CA01-EE89-F0819556FD7B";
	setAttr ".t" -type "double3" 9.76251220703125 58.076065063476563 29.329448699951172 ;
	setAttr ".rp" -type "double3" -9.76251220703125 -58.076065063476563 -29.329448699951172 ;
	setAttr ".sp" -type "double3" -9.76251220703125 -58.076065063476563 -29.329448699951172 ;
createNode locator -n "locator_L_LegPVShape" -p "locator_L_LegPV";
	rename -uid "46946BD9-4484-E84E-0EDA-8C8CACB5FFA9";
	setAttr -k off ".v";
createNode transform -n "locator_R_LegPV" -p "Elisa_BuilderGrp";
	rename -uid "0BA223F9-4B7D-AB9C-F46D-A088AAFF4D32";
	setAttr ".t" -type "double3" 9.76251220703125 58.076065063476563 29.329448699951172 ;
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr ".rp" -type "double3" -9.76251220703125 -58.076065063476563 -29.329448699951172 ;
	setAttr ".sp" -type "double3" -9.76251220703125 -58.076065063476563 -29.329448699951172 ;
createNode locator -n "locator_R_LegPVShape" -p "locator_R_LegPV";
	rename -uid "4275D2A9-4076-3173-2665-5A832AC0E2DE";
	setAttr -k off ".v";
createNode transform -n "locator_L_ArmPV" -p "Elisa_BuilderGrp";
	rename -uid "CA238AC0-49A8-2FA9-1085-DFBDB1C18A7B";
	setAttr ".t" -type "double3" 46.183826446533203 123.22008514404297 -33.448959350585938 ;
	setAttr ".rp" -type "double3" -46.183826446533203 -123.22008514404297 33.448959350585938 ;
	setAttr ".sp" -type "double3" -46.183826446533203 -123.22008514404297 33.448959350585938 ;
createNode locator -n "locator_L_ArmPVShape" -p "locator_L_ArmPV";
	rename -uid "FE7DB08F-4E8D-67BD-940C-9B8C924EC606";
	setAttr -k off ".v";
createNode transform -n "locator_R_ArmPV" -p "Elisa_BuilderGrp";
	rename -uid "969A9A42-487D-F37D-DC93-81BD6CE1B6B1";
	setAttr ".t" -type "double3" 46.183826446533203 123.22008514404297 -33.448959350585938 ;
	setAttr ".s" -type "double3" -1 1 1 ;
	setAttr ".rp" -type "double3" -46.183826446533203 -123.22008514404297 33.448959350585938 ;
	setAttr ".sp" -type "double3" -46.183826446533203 -123.22008514404297 33.448959350585938 ;
createNode locator -n "locator_R_ArmPVShape" -p "locator_R_ArmPV";
	rename -uid "DE65AE4C-403E-CFAC-A15E-A3B0983A420E";
	setAttr -k off ".v";
createNode transform -n "locator_Chest" -p "Elisa_BuilderGrp";
	rename -uid "E5E13D33-42B8-69FB-5FF3-C5BD33810991";
	setAttr ".t" -type "double3" -1.3882724076126136e-014 125.73726990158535 -1.8611132380956943 ;
createNode locator -n "locator_ChestShape" -p "locator_Chest";
	rename -uid "911F6F4F-4ED1-7A1F-40E0-108E81A75DA9";
	setAttr -k off ".v";
createNode transform -n "locator_Pelvis" -p "Elisa_BuilderGrp";
	rename -uid "CBB9E03A-4EEA-0362-388B-A798247BD0A9";
	setAttr ".t" -type "double3" -6.4455392890319055e-015 100.97468777030899 -1.9155815877663294 ;
createNode locator -n "locator_PelvisShape" -p "locator_Pelvis";
	rename -uid "FA4DE9EC-432F-C015-FC5D-33AFD212DF75";
	setAttr -k off ".v";
createNode transform -n "locator_Body" -p "Elisa_BuilderGrp";
	rename -uid "F27A9AD2-406B-8FF8-16A1-75892B31C31E";
	setAttr ".t" -type "double3" -6.4455392890319055e-015 114.04118145894664 -1.9155815877663294 ;
createNode locator -n "locator_BodyShape" -p "locator_Body";
	rename -uid "8C7B0AA2-497F-7754-AB9B-FAAB3D27D180";
	setAttr -k off ".v";
createNode transform -n "C_Spine_Curve" -p "Elisa_BuilderGrp";
	rename -uid "6F9EEA34-4FBC-CE8D-0498-D284BD49251C";
createNode nurbsCurve -n "C_Spine_CurveShape" -p "C_Spine_Curve";
	rename -uid "65F8618E-4F60-CA14-4576-38A613EF284E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 6.2500000000000071 12.500000000000014 18.750000000000021 25.000000000000028
		 25.000000000000028 25.000000000000028
		7
		-6.4455392890319055e-015 100.97468777030899 -1.9155815877663294
		-6.4455392890319071e-015 102.98920699774412 -1.3923815851397576
		-7.1515206438728217e-015 107.04056379131249 -0.36590903988557338
		-8.641318015604662e-015 113.26565810533111 0.30119669246794711
		-9.4442976489331347e-015 119.52538473129485 0.41348572189062083
		-1.0933223438890539e-014 123.67295223146799 -0.10114174958538023
		-1.0933223438890539e-014 125.7369012978083 -0.36972383694179067
		;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "E84A1A87-4FA1-1F81-A0B9-BF8B151D91D2";
	setAttr -s 15 ".lnk";
	setAttr -s 15 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "36442F1C-4774-25EE-634C-5F90179DC1F5";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "DC98F9BC-4C9A-AF10-E346-F5AA88A4A536";
createNode displayLayerManager -n "layerManager";
	rename -uid "9EC4782A-476A-AEBC-A235-5F9C81214A08";
createNode displayLayer -n "defaultLayer";
	rename -uid "C16A99AE-484B-A128-EB09-BAA8563A353E";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "B29A5C98-4D8D-F9D8-83DC-F591539EE4B5";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "A68C85FA-460E-00D1-112B-E4B053E38E85";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "A6D7E670-4A17-9650-D198-3E8088D4D3E8";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n"
		+ "            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n"
		+ "            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n"
		+ "            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n"
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1285\n            -height 1054\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n"
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
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n"
		+ "                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n"
		+ "                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1285\\n    -height 1054\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1285\\n    -height 1054\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "8D1B5323-46C8-E467-96E1-878BD9E1C95A";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 24 -ast 0 -aet 250 ";
	setAttr ".st" 6;
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_bodySG";
	rename -uid "4F4B198B-47BE-8570-9540-AA8AE7C6E812";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo19";
	rename -uid "1A8CCEC6-49FC-A60C-2298-B19B5FC8A78D";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_body";
	rename -uid "D3869733-47AE-A37C-F662-8487E41E8CF8";
	setAttr ".sc" -type "float3" 0.18099999 0.18099999 0.18099999 ;
createNode file -n "Elisa_Model_file6";
	rename -uid "BB2A0D2D-4048-CBEF-256F-15B12CF7E531";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture6";
	rename -uid "C60CB351-4072-F656-DC05-36841F52968B";
createNode materialInfo -n "Elisa_Model_materialInfo24";
	rename -uid "1D054ABD-4DD4-20C7-C11C-C69FDBC551B2";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_clothes01_SG";
	rename -uid "B0A3FDBA-4AF5-1A13-0ED4-60A9CE0A6484";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_clothes03";
	rename -uid "71B964DC-4854-E40A-37D0-28A71F4AB6AA";
	setAttr ".sc" -type "float3" 0.066265061 0.066265061 0.066265061 ;
	setAttr ".ec" 0.58703804016113281;
	setAttr ".sro" 0.27710843086242676;
createNode file -n "Elisa_Model_file9";
	rename -uid "3CB3B637-48F1-103D-3C71-D49F97B64AF0";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_clothes01_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture9";
	rename -uid "75354054-4A8D-A350-D416-CB84A313944F";
createNode materialInfo -n "Elisa_Model_materialInfo25";
	rename -uid "FE899CB8-4A59-F072-7A51-77897AA0BE6D";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_clothes02_SG";
	rename -uid "F2EDEDBF-4F90-F2FA-51C8-1C8F2358BA1C";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_clothes04";
	rename -uid "D72087B8-4B14-BDEE-9BAC-CF871A864B15";
	setAttr ".sc" -type "float3" 0.48795182 0.48795182 0.48795182 ;
	setAttr ".rfl" 0.41935482621192932;
	setAttr ".ec" 0.49027353525161743;
	setAttr ".sro" 0.17469879984855652;
createNode file -n "Elisa_Model_file8";
	rename -uid "EFDB2ECA-44A0-24C5-F1E2-2ABF8BE9246D";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_clothes02_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture8";
	rename -uid "3A6A8958-477D-1236-025A-13B35E3DF81B";
createNode materialInfo -n "Elisa_Model_materialInfo21";
	rename -uid "3873670D-4B9B-C512-E4A8-90AC406FEEE6";
createNode shadingEngine -n "Elisa_Model_blinn13SG";
	rename -uid "D3654B11-4C27-DB45-AEE4-6BA766A5EF68";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Shoes1";
	rename -uid "44779C49-421A-9DCD-49C8-6CA09090D539";
createNode materialInfo -n "Elisa_Model_materialInfo16";
	rename -uid "7879A8D2-441E-AC99-502C-0B9083BA0CA2";
createNode shadingEngine -n "Elisa_Model_blinn10SG";
	rename -uid "C28C8B04-4373-31A0-4A3C-6B9BC41FE469";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Teeth1";
	rename -uid "176501C6-4E2B-1276-F835-13B5DE468D46";
createNode file -n "Elisa_Model_Elisa_Duncan_file1";
	rename -uid "D6470C09-4938-74E9-3D2E-FD80265711FF";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_Elisa_Duncan_place2dTexture1";
	rename -uid "AC2BCB12-468A-741C-48C4-F880510B75A2";
createNode materialInfo -n "Elisa_Model_materialInfo8";
	rename -uid "CC14695F-4EA1-381C-BE72-34A3C3BC42D8";
createNode shadingEngine -n "Elisa_Model_blinn2SG";
	rename -uid "E6F0A360-4586-1D33-68D8-6099076D9249";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye";
	rename -uid "C2E1C979-4D9D-BBB1-A96B-B6AA6B9C658D";
createNode file -n "Elisa_Model_file5";
	rename -uid "A45AF73C-47A1-F24D-3708-CC922F6B2CF1";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa_Duncan_eye_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture5";
	rename -uid "AEAD2A3A-41C1-BE46-F407-BDB952E4E442";
createNode shadingEngine -n "Elisa_Model_polySurface846SG";
	rename -uid "C50D37D4-48D4-EE17-D52E-CD8F48B08B05";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo7";
	rename -uid "8A7B1240-489B-AA9D-8F6D-CFA744EF69B0";
createNode lambert -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Hiar";
	rename -uid "745FECE7-44EF-69F5-E774-139FF73B57B7";
	addAttr -is true -ci true -k true -sn "GMHMaterial" -ln "GMHMaterial" -smn 1 -smx 
		1 -at "double";
	setAttr -k on ".GMHMaterial" 1;
createNode file -n "Elisa_Model_file4";
	rename -uid "B4C34798-4F86-D072-5FCA-E9897BBEC322";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_hair_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture4";
	rename -uid "12827C30-4067-4A59-F092-7DAF15425E21";
createNode materialInfo -n "Elisa_Model_materialInfo20";
	rename -uid "E3E8264F-4D58-237D-2D94-CDB4828602BF";
createNode shadingEngine -n "Elisa_Model_Elisa_Duncan_head_SG";
	rename -uid "73128816-47DA-3E0C-6EA7-EFAC8F18D7FD";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode blinn -n "Elisa_Model_Elisa_Duncan_head";
	rename -uid "9C75EEA5-4826-C92C-96A3-098A907B84AF";
	setAttr ".sc" -type "float3" 0.18064517 0.18064517 0.18064517 ;
createNode file -n "Elisa_Model_file7";
	rename -uid "F1631BAB-499C-76BE-0257-3FABC8115EE2";
	setAttr ".ftn" -type "string" "E:/Work/Modeling/Photogrammetry/Characters/Elisa Duncan/Maya//textures/Elisa Duncan_D.tga";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "Elisa_Model_place2dTexture7";
	rename -uid "AFDBCAEA-4318-B310-66E5-FCA9B721B165";
createNode shadingEngine -n "Elisa_Model_blinn3SG";
	rename -uid "D7E9D292-42B1-5092-AA35-74BB1210EB4E";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo9";
	rename -uid "A6A93954-40B1-E89A-819F-6E9E205BF25F";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyebrows1";
	rename -uid "E972F69B-45D9-E3D8-F61F-B3A65F8E8D9C";
	setAttr ".c" -type "float3" 0.077200003 0.0605 0.0605 ;
createNode shadingEngine -n "Elisa_Model_blinn11SG";
	rename -uid "DDA87CD8-4C12-FBC9-5BF8-748ABA1CCD24";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo17";
	rename -uid "883C7662-465C-EF2F-6CCA-10BD48F356ED";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eyelash1";
	rename -uid "97F7B555-41BD-8CC3-3CCE-E488FC415659";
	setAttr ".c" -type "float3" 0.068400003 0.045600001 0.045600001 ;
createNode shadingEngine -n "Elisa_Model_blinn8SG";
	rename -uid "C2AD52D4-4389-3A3E-1EC8-A38BBC04AAAF";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo14";
	rename -uid "12BD015A-4118-8576-F05E-368C8184135F";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Shadow2";
	rename -uid "3F21EC72-40F8-DB99-7B67-919B31695142";
	setAttr ".it" -type "float3" 1 1 1 ;
createNode shadingEngine -n "Elisa_Model_blinn12SG";
	rename -uid "3F02A3B8-479C-E214-CEE9-2D86D43E90B5";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo18";
	rename -uid "B2726CD5-4F42-79D0-5BC2-C2899274BCE2";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Tears1";
	rename -uid "3CE14269-49DB-7083-1438-13B60962E899";
	setAttr ".c" -type "float3" 0.3581 0.17550001 0.17550001 ;
	setAttr ".it" -type "float3" 0.43225807 0.43225807 0.43225807 ;
createNode shadingEngine -n "Elisa_Model_blinn5SG";
	rename -uid "18FB104A-45ED-3739-E8CE-E4BA25EFF26D";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "Elisa_Model_materialInfo11";
	rename -uid "0C570750-433B-9704-82D7-C6BF37376E4E";
createNode blinn -n "Elisa_Model_Elisa_Duncan_Elisa_Duncan_Eye_inside1";
	rename -uid "A132B7E7-4AC3-DF6F-038F-469A03812963";
	setAttr ".c" -type "float3" 0.41069999 0.18520001 0.18520001 ;
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".msaa" yes;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 15 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 17 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 7 ".u";
select -ne :defaultRenderingList1;
select -ne :defaultTextureList1;
	setAttr -s 7 ".tx";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".mcfr" 30;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr ".hwfr" 30;
connectAttr "Root.s" "C_Pelvis.is";
connectAttr "C_Pelvis.s" "C_Spine_0.is";
connectAttr "C_Spine_0.s" "C_Spine_1.is";
connectAttr "C_Spine_1.s" "C_Spine_2.is";
connectAttr "C_Spine_2.s" "C_Spine_3.is";
connectAttr "C_Spine_3.s" "C_ChestBegin.is";
connectAttr "C_ChestBegin.s" "C_ChestEnd.is";
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
connectAttr "C_ChestBegin.s" "C_Neck_0.is";
connectAttr "C_Neck_0.s" "C_Neck_1.is";
connectAttr "C_Neck_1.s" "C_Head.is";
connectAttr "C_Head.s" "C_FacialRoot.is";
connectAttr "C_FacialRoot.s" "L_Eye.is";
connectAttr "C_FacialRoot.s" "R_Eye.is";
connectAttr "C_FacialRoot.s" "C_UpperTeeth.is";
connectAttr "C_FacialRoot.s" "L_EyelidUpper.is";
connectAttr "C_FacialRoot.s" "L_EyelidLower.is";
connectAttr "C_FacialRoot.s" "R_EyelidUpper.is";
connectAttr "C_FacialRoot.s" "R_EyelidLower.is";
connectAttr "C_FacialRoot.s" "C_Jaw.is";
connectAttr "C_Jaw.s" "C_JawEnd.is";
connectAttr "C_Jaw.s" "C_LowerTeeth.is";
connectAttr "C_ChestBegin.s" "L_Breast.is";
connectAttr "C_ChestBegin.s" "R_Breast.is";
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
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
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
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
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
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_file4.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file5.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file6.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_Elisa_Duncan_file1.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file7.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file8.msg" ":defaultTextureList1.tx" -na;
connectAttr "Elisa_Model_file9.msg" ":defaultTextureList1.tx" -na;
// End of Elisa_Builder.ma
