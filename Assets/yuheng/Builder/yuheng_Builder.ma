//Maya ASCII 2017ff04 scene
//Name: yuheng_Builder.ma
//Last modified: Mon, Oct 15, 2018 04:34:57 PM
//Codeset: 936
requires maya "2017ff04";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" "mtoa" "1.4.2.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 8 , 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "07AB0971-4B77-B354-F149-63B57479E140";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 14.879510258073935 233.10614087541103 356.24856862151108 ;
	setAttr ".r" -type "double3" -740.73835273106783 1443.3999999999935 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "37E79B49-4D88-AD95-3176-7AAB2D8B48DF";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 397.9778900663643;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -3.2849345686560456 165.38538590447507 12.356063880869362 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "E15EF9D6-4A06-1194-5582-73BBEB3636EF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -20.749937321942319 1000.1 9.0577279305956893 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "84DC2AAB-4460-DB72-509B-38A020E2F34F";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 135.34241510434666;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "28AA9790-450E-B0EE-A2A2-8D9A51DE304F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -3.5120010285297321 164.99313730494183 1005.1574667163781 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "4F79D5EA-4741-7C4C-C1E4-878A9E3356B4";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 992.80349758423483;
	setAttr ".ow" 10.40152082905194;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -3.2850000000000219 165.43456021914346 12.353969132143231 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "DF59D432-4FBC-002C-4A72-D192C08455C0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1015.3101300358945 164.94810111659308 11.7679916637475 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "69D84B1C-4344-0BC2-378D-8EBEF417377A";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1015.4039415192125;
	setAttr ".ow" 6.9811762514522213;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -0.093811483318162026 161.00384790512723 10.685882093745095 ;
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
	setAttr ".t" -type "double3" -6.4402427417810059e-015 93.398086968732912 0.59933287275722091 ;
	setAttr ".r" -type "double3" 0 0 1.5919959990811055 ;
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
	rename -uid "9BBF47BC-4C06-7247-E405-7595A52809FE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.3787305403828896 0.60942047346264139 1.5504999693183063e-015 ;
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
	rename -uid "0DA7792C-4C7B-D767-9631-75A1810B937D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 6.4203603642198939 0.38715298980250068 9.9561013509279272e-016 ;
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
	rename -uid "61C576FF-41F5-A9C8-37E1-32ABFEE9C34B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 6.3864127027999018 0.32010932412676352 1.7109553906415659e-015 ;
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
	rename -uid "BBB65849-4380-11CB-212B-109D3A9E9589";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 6.3906709693810928 0.42026509836729886 8.574798091946676e-016 ;
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
	rename -uid "5A7E57C9-47CD-CD74-E7F1-BA8647E0A41B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 6.319713574537241 0.1615095344216585 2.6685595115903552e-015 ;
	setAttr ".r" -type "double3" 0 0 -7.7610804420581596 ;
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
	rename -uid "8852447C-4F5C-387A-8D13-B285B29DACCD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 24.982799786620689 0.56312315721185802 5.7627616969283384e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 6.0480597069556706e-017 0.98017587611435708 -0.19812938167634997 0
		 -3.957012367318657e-016 -0.19812938167635016 -0.9801758761143573 0 -1.0000000000000002 2.2204460492503136e-016 3.3306690738754696e-016 0
		 -1.360977951735926e-014 150.15467294050094 -5.3054764838503967 1;
	setAttr ".radi" 0.65517241379310198;
createNode joint -n "R_Clav" -p "C_ChestBegin";
	rename -uid "145FCEF8-498D-25BA-6A4F-98B74E76A353";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 16.78064509511978 -1.8864674064058988 3.4306381195280182 ;
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
	rename -uid "B2C4C167-4FB2-01E0-00FC-9EB746BF9100";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -11.592782869859846 0.44678233403809031 2.9730049129822103 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.8790257720567514 -12.882184598937723 -46.264838399505713 ;
	setAttr ".bps" -type "matrix" 0.26235226505945086 0.96470156178127819 -0.022851383217186154 0
		 0.96011801640670313 -0.26333161408024858 -0.093967311322336461 0 -0.096667903615593617 0.0027125122403274561 -0.99531299533760365 0
		 -15.337299999999994 145.46816650143637 -5.8867444007556049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "R_Elbow" -p "R_Shoulder";
	rename -uid "612AD460-4C4D-2C9A-1510-92BD79A05055";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -31.978170526706862 0.023039425737081842 -0.16232049739285026 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.9812640243846538 -10.360091258501519 -3.0343090736949301 ;
	setAttr ".bps" -type "matrix" 0.43389320214860133 0.85690266771633017 -0.27830649864828944 0
		 0.46157048511156973 -0.47669839186407365 -0.74813857704844777 0 -0.77375020284527474 0.19615417725565557 -0.60235717173621639 0
		 -22.884002750078423 117.71811015626857 -5.2294136802891966 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "R_Wrist" -p "R_Elbow";
	rename -uid "440BDF9E-40FD-2514-D966-BB8078E708AB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -26.186465636997532 0.098094062929149572 -0.42095159674840588 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.9233321615938133 -5.4851953198709262 -16.805043808821036 ;
	setAttr ".bps" -type "matrix" 0.42895584361388206 0.86277461858135351 -0.26761323166335294 0
		 0.46607536049615472 -0.46516195703129459 -0.75259425460814888 0 -0.77380271553405833 0.19810176996336093 -0.60165193107768 0
		 -33.622499955472293 96.510213366543951 1.6584548023795049 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "R_Index_0" -p "R_Wrist";
	rename -uid "638519FB-4BF4-3118-B7F5-D292ED04F116";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.7981721237696746 0.31186130367893838 -1.1261411675312303 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -166.38115976087681 -13.608092242905476 5.0892407609823938 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_1" -p "R_Index_0";
	rename -uid "D59F87FD-4525-080C-0041-DF9EDF2E8931";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.6677866507726407 0.0026738088590718689 -0.35075586552173021 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.14081335176965537 -1.0849562550793357 14.469913880452969 ;
	setAttr ".bps" -type "matrix" 0.070409717061975116 0.99555393555438121 -0.062568627485633771 0
		 -0.98388301355159469 0.058975043043975897 -0.1688080565097374 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.526199955645332 87.643111883799548 6.0556173428662277 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_2" -p "R_Index_1";
	rename -uid "AFDA2BD3-410C-8C6A-0FE9-1BB584F28418";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.3984845497797522 0.034535906990811327 7.2619051358913111e-006 ;
	setAttr ".r" -type "double3" 0 0 -1.5902773407317584e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 10.602423120057919 ;
	setAttr ".bps" -type "matrix" -0.11181985677680931 0.98940839977785855 -0.092559916159378919 0
		 -0.98004062785301338 -0.12520668012878922 -0.15441390808019673 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.848899955890239 83.080615224110034 6.3423652107990893 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_3" -p "R_Index_2";
	rename -uid "A72EA0A0-4252-B97C-3C9D-7FA0D79046A3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.6273444520327587 0.0061474562371870434 -1.1995798489650156e-005 ;
	setAttr ".r" -type "double3" 0 0 1.6697912077683464e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 3.7411148802044698 ;
	setAttr ".bps" -type "matrix" -0.17552764371641655 0.97913048973488204 -0.10243793419867887 0
		 -0.97065614864558369 -0.18949717246277237 -0.14804547519305628 0 -0.16436753751238731 0.073445937260984723 0.98366102236083819 0
		 -37.54449995602824 80.387542747408176 6.5942982539178967 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Index_4" -p "R_Index_3";
	rename -uid "8D6AB8FD-42AC-D09A-7311-309ED5AA74C7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.9999697926523083 4.9963689612297912e-005 9.0513276882475679e-006 ;
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
	rename -uid "470A9DED-4CEC-EA71-343B-9DA3C67E4110";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.9972748552141297 -0.07251480383871467 0.22930118514080178 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.36314723337367 0.64881297169357222 -2.4547227014271669 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_1" -p "R_Middle_0";
	rename -uid "4879C0EC-481E-CC5D-7E05-E49B905F7C78";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.4514564935600518 0.27253954659749979 0.1933686056145838 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.0816030219547752 -0.98478532917935446 9.2733107384518227 ;
	setAttr ".bps" -type "matrix" 0.10395166297972064 0.9916543542235956 -0.076260694418124136 0
		 -0.97763766959898024 0.087786495698780886 -0.19109714323873037 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -37.576399955864808 87.488331567080024 3.3879011425116676 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_2" -p "R_Middle_1";
	rename -uid "2F7760BE-4C0B-EB3E-86C8-4C8125FCBF53";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.8477064115471222 -0.0076689018953430832 1.3132439491414516e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 12.229208181143033 ;
	setAttr ".bps" -type "matrix" -0.34213987638704557 0.92704975369059783 -0.15335924872031434 0
		 -0.92169499631984086 -0.36285476607024247 -0.13716687828728594 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -38.072799956113705 82.753082069150992 3.7520511892174429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_3" -p "R_Middle_2";
	rename -uid "4E665173-497F-AC15-DDA1-A1A3A9626694";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7822628699411638 0.081487438640095888 -1.0206056913375505e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 5.1136715350966799 ;
	setAttr ".bps" -type "matrix" -0.4647814717253399 0.86882465116624141 -0.17065142562160487 0
		 -0.86634839689122833 -0.48603348917903533 -0.11494304067864308 0 -0.18280765504985413 0.094420193403274399 0.97860420412588744 0
		 -36.918399956256252 79.6253283979663 4.2694677865740021 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Middle_4" -p "R_Middle_3";
	rename -uid "6ABF9C3E-4BD3-5A28-EC71-07917FDC1909";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.3069698639193064 3.8314309804832192e-005 1.9994370983766885e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.46478147176281848 0.86870804318900663 -0.17124403407043384 0
		 -0.86634839685366949 -0.48611178182206682 -0.11461147779717742 0 -0.18280765513256333 0.095087703056191936 0.97853956994718994 0
		 -35.846200000000053 77.514099999999985 4.5119399999999752 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Ring_0" -p "R_Wrist";
	rename -uid "C2E146C8-4650-923B-F902-28949A6BFD13";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.0448729284869103 0.26323871064442983 1.4411903664740251 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 164.03591863448693 10.073235800660113 0.29817893780035659 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_1" -p "R_Ring_0";
	rename -uid "5D0A3318-45F4-1276-0A26-7EADF418FAA5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.9508154391813832 -0.27821188146063491 0.13369781987003648 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.2608413222003847 -3.9270558582583481 13.88079702620829 ;
	setAttr ".bps" -type "matrix" -0.048874618441212436 0.99701866515257287 -0.059708064862364088 0
		 -0.93751071452645818 -0.066412347386439724 -0.34155974625636643 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.878599956028665 87.318262414793537 1.436814679904429 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_2" -p "R_Ring_1";
	rename -uid "F3735389-457E-B293-E841-9287438A7F14";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.0409119845182317 0.029773390786743903 -1.2528417814294812e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 8.5519751351837829 ;
	setAttr ".bps" -type "matrix" -0.5992120192045679 0.7599241105944099 -0.25191328305208532 0
		 -0.72267560095831995 -0.64882367765463878 -0.23825996536187455 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -36.671399956256458 83.091888787317785 1.6899118183151796 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_3" -p "R_Ring_2";
	rename -uid "D5BA0741-4424-7DA4-F34F-2FA6AE6B9A93";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.8167994939404224 0.030573211526395028 1.5668669799850932e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 0.3795302805419089 ;
	setAttr ".bps" -type "matrix" -0.65072860768519603 0.71015866795716542 -0.26875071249280685 0
		 -0.67665895938779275 -0.70294486616896223 -0.21909168812835048 0 -0.3445067950277852 0.039283348278949512 0.937961559301701 0
		 -34.734899956336264 80.636032872997248 2.504046803748186 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Ring_4" -p "R_Ring_3";
	rename -uid "40963185-4E34-BACA-67C4-E4BDA0AD92EE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.4798969251928753 5.0355086088416101e-005 1.6836138357234631e-005 ;
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
	rename -uid "632768A5-4F43-885F-9F3D-728555ECDEC3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.7818913569085453 0.93103572024384107 2.76690882764923 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 163.27819291549955 18.880976272515085 0.36791916897980215 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_1" -p "R_Pinky_0";
	rename -uid "505A989E-4AAE-8F77-FD50-268AF1E1E49D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.7047041038006938 -0.26506145950408211 -0.013141774064415301 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 14.212706485275573 -7.15214861056781 21.000260753196649 ;
	setAttr ".bps" -type "matrix" -0.15484431070880841 0.98623547281342838 -0.057989926759633319 0
		 -0.80131607645459935 -0.15971042023289406 -0.57652851385203763 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -35.020399956122709 87.931386935486174 -0.21152847538694763 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_2" -p "R_Pinky_1";
	rename -uid "5AEEA746-4592-3373-5D1C-CABFEF54CC6E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.742437640018295 0.12639696906985165 1.5323782260878716e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.8855114422302579 ;
	setAttr ".bps" -type "matrix" -0.47969722470878084 0.82573243661521722 -0.29674318143504091 0
		 -0.66028386891561475 -0.56243556901034497 -0.49768608897761768 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -34.468499956312485 84.416245127431338 -0.0048361978950919871 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_3" -p "R_Pinky_2";
	rename -uid "4349FC7C-478D-7A83-35D0-52AB560D5C1A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.135155228649225 -0.040509492172027706 -9.5532884341054114e-006 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.0210688115630289 ;
	setAttr ".bps" -type "matrix" -0.54631084569401323 0.76218098590756578 -0.34731053050269445 0
		 -0.60632390256410917 -0.64594734374209284 -0.46381392205491606 0 -0.57785446702134347 -0.042803899746473979 0.81501658946917943 0
		 -33.628699956356272 82.970590433278744 0.51465380386059834 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Pinky_4" -p "R_Pinky_3";
	rename -uid "FD70334E-4097-FA68-63C4-D2846EBC81DA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.1987356002198482 -3.8045360625460489e-005 -1.7743270923631371e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.54631084571130817 0.76194389892066949 -0.3478303534135051 0
		 -0.60632390248966272 -0.64626357315736116 -0.46337319654851244 0 -0.57785446708310706 -0.042247945600334832 0.81504559747577898 0
		 -32.290600000000055 80.994700000000023 1.2117299999999669 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Thumb_0" -p "R_Wrist";
	rename -uid "B067AD63-4489-63D3-5A29-17BCB2E0D729";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.9688953912645246 1.1699313652289334 -2.1975311343536639 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -108.69401454001661 -52.101384130980705 -20.577156277869193 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_1" -p "R_Thumb_0";
	rename -uid "B6763438-4387-4D63-EE1D-288FA174BD47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -3.3118817000111349 0.18051644526282473 7.148875154072698e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 7.2715006906401092 ;
	setAttr ".bps" -type "matrix" 0.055315044616028729 0.85188961445670097 -0.5207920224234821 0
		 -0.066970927679814024 0.52358150699809647 0.84933933170159248 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.392099955341656 90.343855173995593 7.8988800193043414 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_2" -p "R_Thumb_1";
	rename -uid "CD8DD991-43D6-6179-9E62-8F96041AC389";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.4676547357344631 -0.022696680780995848 -7.8812967174712867e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 1.9121667007214742 ;
	setAttr ".bps" -type "matrix" 0.02538865761252548 0.98757423772182551 -0.15508881665932572 0
		 -0.08306789620426222 0.15668642148488737 0.98414891654792691 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.5844999553725 87.380918895272671 9.7102593440773521 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_3" -p "R_Thumb_2";
	rename -uid "3E874373-4C53-B81C-C39F-07A2EAF3E5CE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7209180826518988 0.28171309579556691 -5.9790500298362304e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -9.5324154644603638 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Neck_0" -p "C_ChestBegin";
	rename -uid "260459C7-4970-990B-0949-39B95AB258CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 21.286880880813925 -0.81665677931687775 8.2473144850726457e-015 ;
	setAttr ".r" -type "double3" 0 0 -3.0174395601940014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -25.987270023432483 ;
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
	setAttr ".t" -type "double3" 6.2677104264476684 0.0032338366333530587 -2.2212185884194545e-017 ;
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
	setAttr ".t" -type "double3" 6.9690010031213205 0.18505591415993905 2.3822257241378547e-016 ;
	setAttr ".r" -type "double3" 0 0 18.256071274301714 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 3.9774202365524855e-016 0.99420750314017159 0.10747762883403142 0
		 -3.8723387470698558e-016 0.10747762883403147 -0.99420750314017159 0 -1 2.2204460492503131e-016 4.4408920985006262e-016 0
		 -1.0072601522555171e-015 163.08851152654773 -4.3144474094236802 1;
	setAttr ".typ" 8;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_FacialRoot" -p "C_Head";
	rename -uid "F7BDD0DB-4059-F737-4FDF-1A8250576489";
	setAttr ".t" -type "double3" 3.8981900297545322 -0.40663109581947965 -9.4127179861655877e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.9837095073778706 27.927043278189814 -63.230731446679862 ;
	setAttr ".radi" 1.169502703832018;
createNode joint -n "R_Eye" -p "C_FacialRoot";
	rename -uid "D96F951A-4B27-4E11-BE1E-56ADA417778B";
	setAttr ".t" -type "double3" 5.9305218822887884 0.62872820600402846 6.746482353533823 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_UpperTeeth" -p "C_FacialRoot";
	rename -uid "53B4410E-4BB8-4A61-36B6-ABA350C449AE";
	setAttr ".t" -type "double3" 3.1649558235445547 -5.6585343358166167 2.6995598859721524 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidUpper" -p "C_FacialRoot";
	rename -uid "28C14202-4144-D2F4-193C-7B898ECF1A94";
	setAttr ".t" -type "double3" 6.2601165037497424 1.2871146382250913 6.8117204692597015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidLower" -p "C_FacialRoot";
	rename -uid "26532AF3-46D8-68BF-DBAD-5D952D536807";
	setAttr ".t" -type "double3" 5.6486796363346627 0.22003997050242674 6.6652246566720477 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_Jaw" -p "C_FacialRoot";
	rename -uid "E076E946-47FD-0BDE-025D-58AE7B75A16F";
	setAttr ".t" -type "double3" -0.014036996024306627 -2.4693314836871449 0.42744138140172222 ;
	setAttr ".r" -type "double3" 13.071002108670084 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.2272854136545986e-015 60.477845958002632 -18.110959232148453 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_JawEnd" -p "C_Jaw";
	rename -uid "7D1BE41E-42D6-7673-8912-9F878BFF89D5";
	setAttr ".t" -type "double3" 1.284985572808095e-014 -2.3690434981273256 8.2559646911088578 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_LowerTeeth" -p "C_Jaw";
	rename -uid "D5AE60C6-4A37-2134-21D4-539F7FA8ADFC";
	setAttr ".t" -type "double3" 1.0735782721535747e-014 -1.9100451628799024 5.0176723933427692 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -7.5549687203861124e-014 -9.5416640443905503e-015 
		-2.1946285137169665e-017 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidUpper" -p "C_FacialRoot";
	rename -uid "5EBA17CE-4340-F7D7-7420-C098B1C80588";
	setAttr ".t" -type "double3" 9.2505317939317706 0.30903034378309258 1.2555673209580789 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_Eye" -p "C_FacialRoot";
	rename -uid "E115AC65-41C2-FF98-F685-50B96B5513B9";
	setAttr ".t" -type "double3" 8.9178462520962256 -0.34863292938507584 1.1960127083801675 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidLower" -p "C_FacialRoot";
	rename -uid "E642C18F-4435-09DD-2FB5-C4B2053E1FFC";
	setAttr ".t" -type "double3" 8.6348596503931105 -0.75673026627666218 1.1170459243598598 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 60.477845958002646 -18.110959232148424 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_Breast" -p "C_ChestBegin";
	rename -uid "A3738DC7-44CB-34D6-FA14-86997475DC0F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.9840870165205422 -10.18415216016575 11.288697328051674 ;
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
	setAttr ".t" -type "double3" 0.98374068365892242 -10.184124897518716 -11.288700000000013 ;
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
	setAttr ".t" -type "double3" 16.780734928456468 -1.886475894264672 -3.4306400000000141 ;
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
	setAttr ".t" -type "double3" 11.592773760973222 -0.44728846118849219 -2.9729541150490988 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.8790257720570951 -12.882184598937679 -46.264838399505749 ;
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
	setAttr ".t" -type "double3" 31.977901906843528 -0.022764354962660605 0.16232697260069973 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.9812640243850881 -10.360091258501535 -3.034309073694859 ;
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
	setAttr ".t" -type "double3" 26.186452383291261 -0.098128728829223633 0.42095234623207034 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.9233321615940451 -5.4851953198708827 -16.805043808821033 ;
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
	setAttr ".t" -type "double3" 2.7981679882702508 -0.31181419274862776 1.1261397818300267 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -166.38115976087687 -13.608092242905499 5.0892407609824035 ;
	setAttr ".bps" -type "matrix" 0.41186876467940975 0.86544984884769571 -0.28523793543453901 0
		 -0.9041612829193939 0.42708011944815283 -0.009744025949658397 0 0.11338648575122801 0.26191435757066173 0.95840720685277325 0
		 -34.507199955438324 93.986839537656508 3.96483407945991 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_1" -p "L_Index_0";
	rename -uid "75AF5B46-400B-18E2-504A-D5B39115F831";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.6677567678817127 -0.0026401336249080032 0.35071771795691031 ;
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
	setAttr ".t" -type "double3" 4.3984662837735158 -0.034609579619043984 2.4843819455000471e-006 ;
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
	setAttr ".t" -type "double3" 2.6274038871094803 -0.0060920599026133004 2.8428681864589578e-005 ;
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
	setAttr ".t" -type "double3" 1.9999487889167824 -9.5583433491697178e-005 5.0735682324720699e-005 ;
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
	setAttr ".t" -type "double3" 2.9972191363771543 0.0725786146731906 -0.22928423261699571 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.36314723337344 0.64881297169357055 -2.4547227014272166 ;
	setAttr ".bps" -type "matrix" 0.44257473508480871 0.8920049524701642 -0.09194981584164312 0
		 -0.89657007560218771 0.43821634609707805 -0.064253665638729252 0 -0.01702067564168408 0.11087650238903739 0.99368843095744763 0
		 -34.547299955556511 93.593562273620662 2.7585655340758297 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_1" -p "L_Middle_0";
	rename -uid "7AD3A36B-44BE-05B4-7630-9BBD9B63FA87";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.4514910788413857 -0.27255905828475591 -0.19334797346396826 ;
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
	setAttr ".t" -type "double3" 4.8476875240474442 0.0077031535520859507 -1.4836968155407249e-005 ;
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
	setAttr ".t" -type "double3" 2.7822518972653825 -0.081507315773748701 6.2072614319674813e-006 ;
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
	setAttr ".t" -type "double3" 2.3070211180663307 4.8744769785002973e-006 -2.7786433992815773e-005 ;
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
	setAttr ".t" -type "double3" 3.0448285786504101 -0.26322992163923686 -1.4411715666733151 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 164.03591863448676 10.073235800660127 0.2981789378003144 ;
	setAttr ".bps" -type "matrix" 0.32680805484026404 0.94497711467976453 0.014654283436280398 0
		 -0.87529203899911401 0.30848380289062538 -0.37242662340239829 0 -0.3564552450957863 0.10888524273585221 0.9279459370879628 0
		 -34.828799955673908 93.245301097309635 1.528727689883199 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_1" -p "L_Ring_0";
	rename -uid "67EA57FC-48C6-1201-4426-538D0F56C072";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.9507909136937442 0.27815737696148801 -0.13370653804843968 ;
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
	setAttr ".t" -type "double3" 4.0409686559283386 -0.029791761694497154 1.8436763669527068e-005 ;
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
	setAttr ".t" -type "double3" 2.8167457515409211 -0.030564134923288577 -2.0798052261739031e-005 ;
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
	setAttr ".t" -type "double3" 2.4799326019100505 -7.9379589756456426e-005 -9.0800624423792442e-006 ;
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
	setAttr ".t" -type "double3" 2.7818345369334594 -0.93102032559878012 -2.7668849121974972 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 163.27819291549932 18.880976272515085 0.36791916897974908 ;
	setAttr ".bps" -type "matrix" 0.13701902197314864 0.98259963325371269 0.125394371273959 0
		 -0.73654920217914932 0.18570794827641951 -0.65039052169924894 0 -0.66236021950807156 -0.0032432509357540277 0.74917849738002162 0
		 -34.339399955787236 92.814962958670989 0.41168888502057976 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_1" -p "L_Pinky_0";
	rename -uid "DD5CEE0E-45B4-70C7-866F-70BFFAFA68BE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.7047322921334356 0.26506414717970017 0.013142735779517523 ;
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
	setAttr ".t" -type "double3" 2.742418388682978 -0.12645915648736406 7.338779710153176e-006 ;
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
	setAttr ".t" -type "double3" 2.1352172001479204 0.04054282982673385 6.4889120743316653e-006 ;
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
	setAttr ".t" -type "double3" 2.1986903450876838 3.6254112693256957e-005 -1.9891313272069056e-006 ;
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
	setAttr ".t" -type "double3" 1.9688819069808829 -1.1698590234246495 2.1975295908304204 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -108.69401454001674 -52.101384130980755 -20.577156277869083 ;
	setAttr ".bps" -type "matrix" 0.065154885778203331 0.75899365325558299 -0.64782981961080921 0
		 -0.057443016759197163 0.65098551750966649 0.75691357222491051 0 0.99622042775925512 -0.012103318157274306 0.086013772180691894 0
		 -33.03599995537769 94.492971807981093 4.3574994168117698 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_1" -p "L_Thumb_0";
	rename -uid "BE9C3BC1-4A78-B007-1029-C6B11792AC78";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.3118396221746096 -0.18050489886172727 -8.5914183173940728e-005 ;
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
	setAttr ".t" -type "double3" 3.4676670414272763 0.022661413859864865 1.0998111150684053e-005 ;
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
	setAttr ".t" -type "double3" 2.7209765953391738 -0.28166741017864183 8.7519273122893537e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472935639464e-006 -1.272221889173292e-014 -9.5324154644603887 ;
	setAttr ".bps" -type "matrix" 0.02538865756685791 0.98746821781080218 -0.15576243090203645 0
		 -0.083067896291059123 0.15735769885150797 0.98404180765754901 0 0.99622042775318176 -0.012044643029875901 0.086022008239474645 0
		 -33.671200000000027 83.907599999999988 10.083899999999984 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Hip" -p "C_Pelvis";
	rename -uid "1592F0AF-4F67-70CD-B69A-41B122B7BF81";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -5.1093562216767054 -0.82278843189799389 7.2107892390192845 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 168.54708099488485 8.1975146413132514 7.4750990157296382 ;
	setAttr ".bps" -type "matrix" 0.04367621427123513 0.99879915221154247 -0.022195536678289766 0
		 -1.3006955835555549e-012 0.022216737247664126 0.999753177832443 0 0.99904573884629189 -0.043665434013329021 0.00097034297773582754 0
		 -8.2375200000000035 99.635493474825282 -2.2160409616281522 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 2;
createNode joint -n "R_Knee" -p "R_Hip";
	rename -uid "4236AEE6-40A0-4935-1706-B2B519C6FE0C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -38.709648303830996 0.12595619856495213 0.12270055390329504 ;
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
	rename -uid "59979143-4152-6C89-C2B2-C1A56187C865";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -42.277908555999339 -0.10737049170038084 -0.25695724377227508 ;
	setAttr ".r" -type "double3" 0 -3.721119391838581 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -4.0647038662964281 -2.9201065636837744 -73.084026862622892 ;
	setAttr ".bps" -type "matrix" 0.089586411029085211 0.82001406268021293 -0.56528860944266346 0
		 -0.078021190938231205 0.57160461050695421 0.81681139990316831 0 0.99291840990260016 -0.029070711272434359 0.11518647933940374 0
		 -11.971399122896578 14.273993436447512 -1.7960609639808891 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 1.0377079476680056;
createNode joint -n "R_Ball" -p "R_Ankle";
	rename -uid "4B2071F6-4C27-DC5B-56BF-98AEB7536294";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -14.883177422794814 0.58013592502718403 -0.25284142968375889 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -2.329391593643833 -4.773860201868863 -23.098971141735728 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Toe" -p "R_Ball";
	rename -uid "1953DB6E-463D-6103-AC73-BD84881418A7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -8.4674993316176774 -1.8785029981945525 0.70128421096003635 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0.50000190515003462 0 0.49999999612681634 ;
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "L_Hip" -p "C_Pelvis";
	rename -uid "2EB04C85-4244-36F8-F622-51B4BD810584";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -5.1093103503544199 -0.82277863371731641 -7.2107900000000047 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 168.54708099488488 8.1975146413132443 -172.52490098427037 ;
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
	setAttr ".t" -type "double3" 38.709705096841724 -0.12596703155594513 -0.12268008366458361 ;
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
	setAttr ".t" -type "double3" 42.277894442571679 0.10738330076218361 0.25688592542579514 ;
	setAttr ".r" -type "double3" 0 -3.721119391838581 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -4.0647038662958916 -2.9201065636815997 -73.084026862622821 ;
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
	setAttr ".t" -type "double3" 14.883175583373715 -0.58013713891273166 0.25284864587828793 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -2.3293915936440062 -4.7738602018688177 -23.098971141735728 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "L_Toe" -p "L_Ball";
	rename -uid "E3D1F95C-4AFB-1D58-177F-6984AA27A0DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 8.4675616119578763 1.8785103798589522 -0.70123654030536997 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0.50000190515331144 1.440024086126487e-015 0.49999999612701113 ;
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode transform -n "locator_R_ArmPV" -p "yuheng_BuilderGrp";
	rename -uid "9B5F5B1D-4E26-7B26-F06D-4887BA082BD9";
	setAttr ".t" -type "double3" -48.030311584472656 120.89861297607422 -35.118618011474609 ;
createNode locator -n "locator_R_ArmPVShape" -p "locator_R_ArmPV";
	rename -uid "92A57A01-4CBC-274F-A0DB-F19817271C23";
	setAttr -k off ".v";
createNode transform -n "locator_R_LegPV" -p "yuheng_BuilderGrp";
	rename -uid "2726DAF4-4362-6AD6-532D-BC9DD47CE60E";
	setAttr ".t" -type "double3" -12.887722969055176 46.740501403808594 33.389591217041016 ;
createNode locator -n "locator_R_LegPVShape" -p "locator_R_LegPV";
	rename -uid "EC203BE0-45EF-4990-3C72-A5BDC2D263B0";
	setAttr -k off ".v";
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
createNode transform -n "locator_R_Foot_Ext" -p "yuheng_BuilderGrp";
	rename -uid "22427981-4593-D21B-85B9-F198484A8A47";
	setAttr ".t" -type "double3" -28.494337329551218 0.14341159317586971 2.2329580024170923 ;
	setAttr ".r" -type "double3" 0 155.68996253243344 0 ;
	setAttr ".rp" -type "double3" 3.5527136788005009e-015 0 -1.7763568394002505e-015 ;
	setAttr ".rpt" -type "double3" -7.5216923527874547e-015 0 1.9326462819643175e-015 ;
	setAttr ".sp" -type "double3" 3.5527136788005009e-015 0 -1.7763568394002505e-015 ;
createNode locator -n "locator_R_Foot_ExtShape" -p "locator_R_Foot_Ext";
	rename -uid "7790831C-45B8-768F-7547-42BDC79AE1D3";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -3.5527136788005009e-015 -5.5511151231257827e-017 
		3.9443045261050599e-031 ;
createNode transform -n "locator_R_Foot_Int" -p "yuheng_BuilderGrp";
	rename -uid "C73CA874-4E91-0424-76D0-109C78C4C097";
	setAttr ".t" -type "double3" -18.172580587150449 0 6.432998998723555 ;
	setAttr ".r" -type "double3" 0 160.47244852087374 0 ;
	setAttr ".rp" -type "double3" 0 0 1.7763568394002505e-015 ;
	setAttr ".rpt" -type "double3" 5.9376522011032067e-016 0 -3.4505391724426786e-015 ;
	setAttr ".sp" -type "double3" 0 0 1.7763568394002505e-015 ;
createNode locator -n "locator_R_Foot_IntShape" -p "locator_R_Foot_Int";
	rename -uid "F4D35250-40A5-7667-021D-408B027FE956";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 2.0434901271564345e-016 0 -5.8882639917960981e-016 ;
createNode transform -n "locator_R_Foot_Base" -p "yuheng_BuilderGrp";
	rename -uid "267AC70D-4B73-7AA1-7AB5-E99D06728D1C";
	setAttr ".t" -type "double3" -17.126727565741071 0.87666600942611694 -12.941733892444205 ;
	setAttr ".r" -type "double3" 0 162.27307880700354 0 ;
	setAttr ".rp" -type "double3" 0 0 -8.8817841970012523e-016 ;
	setAttr ".rpt" -type "double3" -2.7043314091592181e-016 0 1.7341848153706083e-015 ;
	setAttr ".sp" -type "double3" 0 0 -8.8817841970012523e-016 ;
createNode locator -n "locator_R_Foot_BaseShape" -p "locator_R_Foot_Base";
	rename -uid "C768D21D-4C76-C3CB-DEF7-A2A1AF73B763";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 3.5527136788005009e-015 -1.1102230246251565e-016 0 ;
createNode transform -n "locator_R_Foot_BaseSwive" -p "yuheng_BuilderGrp";
	rename -uid "B247CEA4-4D8A-61DC-F776-6CBBE212A004";
	setAttr ".t" -type "double3" -18.835947901097406 0.86427691328901979 -7.9156431985422966 ;
	setAttr ".r" -type "double3" 0 159.60235777354958 0 ;
	setAttr ".rp" -type "double3" 0 -1.1102230246251565e-016 0 ;
	setAttr ".sp" -type "double3" 0 -1.1102230246251565e-016 0 ;
createNode locator -n "locator_R_Foot_BaseSwiveShape" -p "locator_R_Foot_BaseSwive";
	rename -uid "6E69480B-48FD-7B6C-9529-BEA5E485EC36";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 3.0814879110195774e-032 1.1102230246251565e-016 1.5543122344752192e-015 ;
createNode transform -n "locator_R_Foot_ToeSwive" -p "yuheng_BuilderGrp";
	rename -uid "CF0247DD-4A2A-4434-13A3-0E9AF1F38128";
	setAttr ".t" -type "double3" -23.103343485638323 0.11554945879680645 4.3556402479563463 ;
	setAttr ".r" -type "double3" 0 160.85106021997646 0 ;
createNode locator -n "locator_R_Foot_ToeSwiveShape" -p "locator_R_Foot_ToeSwive";
	rename -uid "F3BCD73A-4BA8-B3D0-8FDD-8FA57C27412D";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 4.163336342344337e-017 0 ;
createNode transform -n "locator_L_ArmPV" -p "yuheng_BuilderGrp";
	rename -uid "7A20E7AA-4EB2-40F4-55A3-41A2D6DF3320";
	setAttr ".t" -type "double3" 48.03 120.89861297607422 -35.118618011474609 ;
createNode locator -n "locator_L_ArmPVShape" -p "locator_L_ArmPV";
	rename -uid "C1C529B0-453A-F7C1-BFB5-47A20D33DE51";
	setAttr -k off ".v";
createNode transform -n "locator_L_LegPV" -p "yuheng_BuilderGrp";
	rename -uid "33F93F0E-4D10-7EAA-1DAF-E2A639F57D14";
	setAttr ".t" -type "double3" 12.888 46.740501403808594 33.389591217041016 ;
createNode locator -n "locator_L_LegPVShape" -p "locator_L_LegPV";
	rename -uid "E9F85FC8-43DC-2305-5CD9-818845E2A6AA";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "72159E46-4A85-7503-5E77-D4A41BC2E0B8";
	setAttr -s 31 ".lnk";
	setAttr -s 31 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "77E39C0D-41E4-846B-C049-C1ACCA5AAC60";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "7418737C-4B2B-A104-29EF-289359098E85";
createNode displayLayerManager -n "layerManager";
	rename -uid "E5C07327-40F0-9609-904F-9D982AB802B8";
createNode displayLayer -n "defaultLayer";
	rename -uid "85F25CCF-46DC-85D2-2094-1AB96562B425";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "3FDDEAC3-4D45-AAA5-6AF6-3EA4A692950D";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "02373C42-40FA-6C99-1E09-479B29ED0D98";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "C909B1FF-4F50-4D5A-00DC-6389EC7C0DD8";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n"
		+ "            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 953\n            -height 467\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n"
		+ "            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 953\n            -height 466\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n"
		+ "            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n"
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 953\n            -height 466\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 1\n            -jointXray 1\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1914\n            -height 985\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 1\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1914\\n    -height 985\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 1\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1914\\n    -height 985\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
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
select -ne :time1;
	setAttr ".o" 0;
select -ne :renderPartition;
	setAttr -s 3 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -s 3 ".r";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "Root.s" "C_Pelvis.is";
connectAttr "C_Pelvis.s" "C_Spine_0.is";
connectAttr "C_Spine_0.s" "C_Spine_1.is";
connectAttr "C_Spine_1.s" "C_Spine_2.is";
connectAttr "C_Spine_2.s" "C_Spine_3.is";
connectAttr "C_Spine_3.s" "C_ChestBegin.is";
connectAttr "C_ChestBegin.s" "C_ChestEnd.is";
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
connectAttr "C_Pelvis.s" "R_Hip.is";
connectAttr "R_Hip.s" "R_Knee.is";
connectAttr "R_Knee.s" "R_Ankle.is";
connectAttr "R_Ankle.s" "R_Ball.is";
connectAttr "R_Ball.s" "R_Toe.is";
connectAttr "C_Pelvis.s" "L_Hip.is";
connectAttr "L_Hip.s" "L_Knee.is";
connectAttr "L_Knee.s" "L_Ankle.is";
connectAttr "L_Ankle.s" "L_Ball.is";
connectAttr "L_Ball.s" "L_Toe.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
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
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "lambert5.msg" ":defaultShaderList1.s" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of yuheng_Builder.ma
