//Maya ASCII 2017ff04 scene
//Name: Elisa_Builder.ma
//Last modified: Mon, Feb 25, 2019 11:25:13 AM
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
	setAttr ".t" -type "double3" -198.81883462556036 160.88724183028685 108.7604330632351 ;
	setAttr ".r" -type "double3" 0.86164727380828532 298.20000000146916 2.1033154780423197e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "FE873ED0-4D62-874C-B800-B8874E234E17";
	setAttr -k off ".v" no;
	setAttr ".fl" 85;
	setAttr ".coi" 228.32036689050102;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -0.00027026805166918688 160.97976071918538 1.4919159387543788 ;
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
	setAttr ".t" -type "double3" 0 158.48158277082297 1011.1187356800938 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9322B862-422A-AEC8-1CF2-578AF98C07D5";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1011.1187356800938;
	setAttr ".ow" 30.307966583124479;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 0 158.48158277082297 0 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "1E0B2365-4396-7E1C-9774-B287A6729515";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1011.2052426507774 163.5576841067091 3.5928848124297454 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "F622784D-4EDA-F624-8C79-B5B2527F1E42";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1011.2055129188288;
	setAttr ".ow" 21.988088208850726;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -0.00027026805166838197 161.49892680307786 4.7273021021855142 ;
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
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" -90 -13.496466991553524 90 ;
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
	setAttr ".t" -type "double3" 4.9999999999999432 -1.0658141036401503e-014 1.1102230246251629e-015 ;
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
	rename -uid "05667D6F-49F7-38A6-66BF-29954DC8EA66";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.0000000000000284 3.5527136788005009e-015 1.5258969225993081e-015 ;
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
	rename -uid "9595DE26-45AE-575A-8A5F-90986F228BF8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.9999999999999716 -5.3290705182007514e-015 1.4892484008161087e-015 ;
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
	rename -uid "71714EE1-452B-AB04-B469-478503F8361A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 5 -1.3322676295501878e-015 1.444645586505199e-015 ;
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
	rename -uid "2C25ABE3-435E-9E66-74D4-8690B0E96688";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 5.0000000000000711 -5.3290705182007514e-015 1.3924279340154811e-015 ;
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
	setAttr ".t" -type "double3" 24.912029405115064 -2.4868995751603507e-014 5.6988077785042318e-015 ;
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
	setAttr ".t" -type "double3" 23.187386247869412 -0.45595805285650925 -1.5920092494166134 ;
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
	setAttr ".t" -type "double3" 14.83830909385706 -0.98649668350310549 0.32049816331728209 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4226690429428865 -3.6505286404364679 2.8897215262535827 ;
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
	setAttr ".t" -type "double3" 28.591760082069783 -5.6843418860808015e-014 5.1070259132757201e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -11.758530399229764 0 ;
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
	setAttr ".t" -type "double3" 24.080645383873801 8.5265128291212022e-014 7.1054273576010019e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
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
	setAttr ".t" -type "double3" 3.186897762051089 0.57178785862168979 1.5459576764830381 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.77297379850489 -1.463801111038399 3.9007503868178004 ;
	setAttr ".bps" -type "matrix" 0.41186876465116534 -0.86544984892921928 0.28523793522796859 0
		 -0.90416128294366405 -0.42708011939710511 0.0097440259350527469 0 0.11338648566029086 -0.26191435738452062 -0.95840720691440073 0
		 34.507240604818904 93.877060305389605 3.7806576263978822 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Index_1" -p "L_Index_0";
	rename -uid "EAEF5586-49F6-397E-7439-3A916ABDF697";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 7.3299559333269286 -8.5265128291212022e-014 -3.730349362740526e-014 ;
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
	setAttr ".t" -type "double3" 4.5828818255348835 5.6843418860808015e-014 2.1316282072803006e-014 ;
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
	setAttr ".t" -type "double3" 2.7218692266728723 2.8421709430404007e-014 1.4210854715202004e-014 ;
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
	setAttr ".t" -type "double3" 1.9999999999999554 2.8421709430404007e-014 -1.4210854715202004e-014 ;
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
	setAttr ".t" -type "double3" 3.2403685490240264 0.45008722563636638 0.28353062910949056 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 176.90924692631393 9.8253528737981579 4.9201434837871494 ;
	setAttr ".bps" -type "matrix" 0.44257473503976497 -0.89200495251460643 0.091949815627311748 0
		 -0.89657007562281144 -0.43821634605744064 0.064253665621286038 0 -0.01702067572654864 -0.11087650218815649 -0.99368843097840864 0
		 34.547250508843504 93.483739511076408 2.5743864382276556 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Middle_1" -p "L_Middle_0";
	rename -uid "53DC7332-4E56-BCA0-EB50-0B8C33F71A38";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 6.8443709563816952 2.8421709430404007e-014 -3.3750779948604759e-014 ;
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
	setAttr ".t" -type "double3" 4.7750551437277551 2.8421709430404007e-014 -2.1316282072803006e-014 ;
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
	setAttr ".t" -type "double3" 3.3738546452201916 -5.6843418860808015e-014 0 ;
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
	setAttr ".t" -type "double3" 2.3070561573098303 -2.8421709430404007e-014 7.1054273576010019e-015 ;
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
	setAttr ".t" -type "double3" 3.3322934043125514 0.56930380935591529 -1.0166264076138667 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 156.77574418678438 15.893649261116229 -2.6146973138579943 ;
	setAttr ".bps" -type "matrix" 0.32680805478370734 -0.94497711469597612 -0.014654283652138236 0
		 -0.87529203898782948 -0.30848380291422528 0.37242662340937227 0 -0.35645524517534871 -0.10888524252829515 -0.92794593708175521 0
		 34.828832637612706 93.135483750106843 1.3445488380933206 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Ring_1" -p "L_Ring_0";
	rename -uid "F2495954-41B1-859A-4B31-AD8407DF45A1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 6.272130349944689 0 -2.8421709430404007e-014 ;
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
	setAttr ".t" -type "double3" 4.2389573518237764 2.8421709430404007e-014 1.4210854715202004e-014 ;
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
	setAttr ".t" -type "double3" 3.231806106992579 8.5265128291212022e-014 -2.8421709430404007e-014 ;
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
	setAttr ".t" -type "double3" 2.4799134091834816 -9.9475983006414026e-014 2.8421709430404007e-014 ;
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
	setAttr ".t" -type "double3" 3.2557139834662934 -0.057191560778278472 -2.1453663613957659 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 134.56166128333049 21.686165462925068 -14.68043920908142 ;
	setAttr ".bps" -type "matrix" 0.13701902190565271 -0.982599633236522 -0.12539437148241814 0
		 -0.73654920213874675 -0.18570794836406668 0.65039052171997813 0 -0.66236021956696223 0.003243251125286048 -0.74917849732713515 0
		 34.339432070581402 92.705217796446703 0.22751122284903458 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Pinky_1" -p "L_Pinky_0";
	rename -uid "796DF2AE-4941-A988-716D-4BB7B118BF74";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.9700611425120655 4.2632564145606011e-014 1.4210854715202004e-014 ;
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
	setAttr ".t" -type "double3" 3.5642773452595256 0 4.2632564145606011e-014 ;
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
	setAttr ".t" -type "double3" 1.7506404229104504 -4.2632564145606011e-014 -7.1054273576010019e-014 ;
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
	setAttr ".t" -type "double3" 2.4493334333669736 0 4.2632564145606011e-014 ;
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
	setAttr ".t" -type "double3" 2.3159163036183514 -0.60544158728268371 2.202063859361262 ;
	setAttr ".r" -type "double3" -7.1562480332929135e-015 -6.3611093629270351e-015 -2.5444437451708134e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -101.95046059860573 -25.965428211088273 -13.56955891917322 ;
	setAttr ".bps" -type "matrix" 0.06515488578479478 -0.75899365338971603 0.647829819452997 0
		 -0.057443016857054358 -0.65098551735404264 -0.75691357235132795 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.035975848428933 94.38317086786796 4.1733219965685979 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "L_Thumb_1" -p "L_Thumb_0";
	rename -uid "D838E852-4337-F9CD-7385-938FCA62F006";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 5.4665225392128995 -1.7763568394002505e-014 2.8421709430404007e-014 ;
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
	setAttr ".t" -type "double3" 3.4781282901164445 -7.638334409421077e-014 0 ;
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
	setAttr ".t" -type "double3" 3.4126775211040581 -3.5527136788005009e-015 0 ;
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
	setAttr ".t" -type "double3" 23.187818501544214 -0.45605044414923412 1.5920100000000024 ;
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
	rename -uid "952963EE-4E30-8C18-CD94-43AF39E1E4A3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -14.838344370227166 0.98655417062087736 -0.32049425904939 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4226690429437365 -3.6505286404363364 2.8897215262536244 ;
	setAttr ".bps" -type "matrix" 0.2666003241590032 -0.96346582504763489 0.025648998491068199 0
		 0.95879185923477384 0.26783043732062622 0.094789385005749988 0 -0.098195915513021717 -0.00067882981860458499 0.99516687111591351 0
		 15.337338897321946 145.4677280333907 -5.886741238217672 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "R_Elbow" -p "R_Shoulder";
	rename -uid "33780613-482D-D292-8F9D-B0B5E2910C84";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".t" -type "double3" -28.591763274852514 0.00069612425772902498 1.4358258667801493e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377364635090901e-007 -11.758530399229729 -9.644659363826661e-016 ;
	setAttr ".bps" -type "matrix" 0.42895584358440458 -0.86277461866033289 0.26761323145597482 0
		 0.46607536058277577 0.46516195685258321 0.7525942546649631 0 -0.77380271549822566 -0.19810177003902046 0.60165193109885373 0
		 23.006157225510016 117.75341672857235 -5.148942023800136 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
	setAttr ".radi" 0.5;
createNode joint -n "R_Wrist" -p "R_Elbow";
	rename -uid "10F7B9CF-4645-F575-8D69-F5A08C7150B0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -24.080620443985154 5.2173383892295533e-005 -8.6611514227286079e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377364625159387e-007 -1.4070084281024381e-023 4.0284864284701424e-022 ;
	setAttr ".bps" -type "matrix" 0.42895584358440458 -0.86277461866033289 0.26761323145597482 0
		 0.46607536058277577 0.46516195685258321 0.7525942546649631 0 -0.77380271549822566 -0.19810177003902046 0.60165193109885373 0
		 33.622476635463073 96.400424182857748 1.4742747616993492 1;
	setAttr ".sd" 1;
	setAttr ".typ" 12;
	setAttr ".radi" 0.5;
createNode joint -n "R_Index_0" -p "R_Wrist";
	rename -uid "C1CEF752-4276-9310-624B-D59FB46D3783";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.1868804645248758 -0.57226815067033954 -1.5459742346992886 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.77297379849688 -1.4638011110384481 3.9007503868178537 ;
	setAttr ".bps" -type "matrix" 0.41186876465116534 -0.86544984892921928 0.28523793522796859 0
		 -0.90416128294366405 -0.42708011939710511 0.0097440259350527469 0 0.11338648566029086 -0.26191435738452062 -0.95840720691440073 0
		 34.507240604818904 93.877060305389605 3.7806576263978822 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_1" -p "R_Index_0";
	rename -uid "37F5DC61-4DDE-AE65-E6F1-0CBF4D7232C5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -7.329963748218276 5.2974637981151318e-005 6.4431491786365314e-007 ;
	setAttr ".r" -type "double3" 1.3914926731402885e-014 -2.7829853462805791e-015 1.7691835415640811e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.290329191695982 -12.050114242918179 21.733404124072152 ;
	setAttr ".bps" -type "matrix" 0.070409717008542899 -0.99555393557109495 0.062568627279821931 0
		 -0.98388301354174001 -0.058975043020250723 0.16880805657546372 0 -0.1643675375942652 -0.073445937053481514 -0.98366102236265041 0
		 37.526220500025737 87.533351050233975 5.871439122132065 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_2" -p "R_Index_1";
	rename -uid "E4B2668C-4B95-EA64-ECFC-C98DA3E825AF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.5828947218499572 -0.00012864295928238789 -3.0268055404292227e-005 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2173657553753014e-015 1.3119788061036982e-014 10.602423120057889 ;
	setAttr ".bps" -type "matrix" -0.11181985682751612 -0.98940839978992168 0.09255991596917397 0
		 -0.98004062783349577 0.12520668015518457 0.15441390818266887 0 -0.1643675375942652 -0.073445937053481514 -0.98366102236265041 0
		 37.848899912445233 82.970845012565491 6.15818374694142 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Index_3" -p "R_Index_2";
	rename -uid "E67D8CB2-4999-E251-D3E7-F79C4791CD40";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.7221468050048996 -0.00038880305598354425 -9.8805965343728985e-005 ;
	setAttr ".r" -type "double3" 0 0 3.975693351829396e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.3235273415776335e-016 1.6300342742500006e-014 3.7411148802044698 ;
	setAttr ".bps" -type "matrix" -0.17552764376574342 -0.9791304897451969 0.10243793401556563 0
		 -0.97065614862279892 0.18949717248990022 0.14804547530772044 0 -0.1643675375942652 -0.073445937053481514 -0.98366102236265041 0
		 37.544540885215433 80.27780473656567 6.4101197338413458 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Index_4" -p "R_Index_3";
	rename -uid "620342EB-47AC-A461-B631-A8AA5BB3E7F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.9994780471278786 0.00074307969947540187 0.00019504426445138279 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.1755276437657432 -0.97906038632627412 0.10310580100408367 0
		 -0.97065614862279881 0.18959811414055766 0.14791617982864455 0 -0.1643675375942652 -0.07411690118314071 -0.98361069409813107 0
		 37.193485597683932 78.323920645375111 6.6473909468357233 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Middle_0" -p "R_Wrist";
	rename -uid "13D9C087-4E9B-E398-0611-ED87B5ADC61E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.2403943374950757 -0.45014579276605104 -0.28353298359268031 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 176.90924692631376 9.8253528737981277 4.9201434837871476 ;
	setAttr ".bps" -type "matrix" 0.44257473503976497 -0.89200495251460643 0.091949815627311748 0
		 -0.89657007562281144 -0.43821634605744064 0.064253665621286038 0 -0.01702067572654864 -0.11087650218815649 -0.99368843097840864 0
		 34.547250508843504 93.483739511076408 2.5743864382276556 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_1" -p "R_Middle_0";
	rename -uid "F97E69F6-44BF-092C-5043-20B99B660D8A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -6.8443673701317636 0.00020838648109133828 1.2245020739598544e-005 ;
	setAttr ".r" -type "double3" 2.1568136433674469e-014 -1.9878466759147091e-016 6.0629323615398278e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.4161136110101094 -1.8568497434328373 20.269793279669816 ;
	setAttr ".bps" -type "matrix" 0.10395166292759697 -0.9916543542450299 0.076260694210451674 0
		 -0.97763766958905673 -0.087786495679905499 0.19109714329816851 0 -0.18280765513256275 -0.094420193195707297 -0.97860420413046445 0
		 37.576396171377979 87.37852672113678 3.203725085751906 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_2" -p "R_Middle_1";
	rename -uid "487C1A7D-4AC6-745B-DDE2-93BB874FCB9C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.7749019140564073 0.00038054778474361228 9.9620153655166632e-005 ;
	setAttr ".r" -type "double3" 0 0 9.5416640443905503e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.8675224189963938e-015 7.9513867036587888e-015 26.434714595973528 ;
	setAttr ".bps" -type "matrix" -0.3421398764293016 -0.9270497537013882 0.15335924856081617 0
		 -0.92169499628775065 0.36285476609668638 0.13716687843296052 0 -0.18280765513256275 -0.094420193195707297 -0.97860420413046445 0
		 38.072771094139426 82.643322496098961 3.5678741059057839 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Middle_3" -p "R_Middle_2";
	rename -uid "57F245E6-444B-51C9-57C0-4C98A377B068";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.3741778777147253 -0.00034123810101505114 -0.00011444202678490001 ;
	setAttr ".r" -type "double3" 0 0 1.1131941385122309e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182704892709e-006 1.1131941432516269e-014 7.8475247473755516 ;
	setAttr ".bps" -type "matrix" -0.46478147176281875 -0.86882465117332019 0.17065142548349047 0
		 -0.86634839685366916 0.48603348920670486 0.11494304084473086 0 -0.18280765513256275 -0.094420193195707297 -0.97860420413046445 0
		 36.918440882733378 79.515591378223291 4.0852859190501727 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Middle_4" -p "R_Middle_3";
	rename -uid "74FA4A02-460A-9E65-10BA-9E875713009C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.3068978167364804 0.00020558556286687235 7.0505045307811542e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.7075472925031871e-006 2.0142432712572228e-022 -3.7915166095322089e-022 ;
	setAttr ".bps" -type "matrix" -0.46478147176281859 -0.8687080431890063 0.17124403407043445 0
		 -0.86634839685366938 0.48611178182206727 0.11461147779717586 0 -0.18280765513256267 -0.095087703056192907 -0.97853956994718982 0
		 35.846163926499479 77.514084166395477 4.511935600014052 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Ring_0" -p "R_Wrist";
	rename -uid "C603A6A2-4AFD-15E1-9F6D-769DFF5E1C5D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.3323031971821706 -0.56954535117949945 1.0166243480259496 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 156.77574418678438 15.89364926111622 -2.6146973138580054 ;
	setAttr ".bps" -type "matrix" 0.32680805478370734 -0.94497711469597612 -0.014654283652138236 0
		 -0.87529203898782948 -0.30848380291422528 0.37242662340937227 0 -0.35645524517534871 -0.10888524252829515 -0.92794593708175521 0
		 34.828832637612706 93.135483750106843 1.3445488380933206 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_1" -p "R_Ring_0";
	rename -uid "8BF32CEE-4BF5-9452-D96B-78A8DBB7E6BD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -6.272081534248386 9.4338305331120864e-005 3.6612177893857734e-005 ;
	setAttr ".r" -type "double3" -8.2495637050459938e-015 1.7890620083232288e-015 1.3014183706379036e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.5744174289039593 -4.047093082911644 21.932371729151967 ;
	setAttr ".bps" -type "matrix" -0.048874618494956119 -0.99701866516171789 0.059708064665664556 0
		 -0.93751071449562839 0.066412347372696537 0.34155974634365982 0 -0.34450679510405802 -0.039283348070078009 -0.93796155928243463 0
		 36.878615356627982 87.208464109019019 1.2526352608420734 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_2" -p "R_Ring_1";
	rename -uid "29BA6CF1-416C-95B5-4364-99B83172FF55";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.2391522534653046 -0.000264389127778486 -0.0001115275943703864 ;
	setAttr ".r" -type "double3" 0 0 5.0888874903416268e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2124753150081982e-014 3.6576378836830435e-014 36.679824481650378 ;
	setAttr ".bps" -type "matrix" -0.5992120192292536 -0.75992411060995335 0.25191328294647908 0
		 -0.72267560090149141 0.64882367764907944 0.23825996554937964 0 -0.34450679510405802 -0.039283348070078009 -0.93796155928243463 0
		 36.671437933241215 82.982144508426217 1.5057352005197697 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Ring_3" -p "R_Ring_2";
	rename -uid "883440E3-400E-2FE6-D04E-399CD55FBD48";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.231619754719901 9.1851804057796471e-005 8.2869239236060821e-005 ;
	setAttr ".r" -type "double3" 0 0 2.7829853462805771e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.3465616515484768e-015 3.6576378836829955e-014 4.2167909545142912 ;
	setAttr ".bps" -type "matrix" -0.65072860770563679 -0.71015866797307492 0.26875071240127396 0
		 -0.67665895932930231 0.70294486616456131 0.21909168832311304 0 -0.34450679510405802 -0.039283348070078009 -0.93796155928243463 0
		 34.734900870112725 80.52621712690609 2.3198700867787529 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Ring_4" -p "R_Ring_3";
	rename -uid "5663C7A0-49E5-E99D-FADC-CFA1A50E76EF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.4799633690400071 -9.218413761402644e-005 -4.7133288603617984e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.2074182697257331e-006 1.4242850445899379e-021 -8.0430212303426471e-022 ;
	setAttr ".bps" -type "matrix" -0.65072860770563667 -0.70997518078224697 0.2692350678992238 0
		 -0.67665895932930253 0.70309415086468618 0.21861214005459767 0 -0.34450679510405802 -0.039923147334365028 -0.93793454485590277 0
		 33.121150270124268 78.76698671202999 3.0184408557943465 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Pinky_0" -p "R_Wrist";
	rename -uid "30898DCF-41F1-419C-44BC-83AA4B458F05";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.2557405010658158 0.056385861287566286 2.1453459702264173 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 134.56166128333049 21.686165462925032 -14.68043920908141 ;
	setAttr ".bps" -type "matrix" 0.13701902190565271 -0.982599633236522 -0.12539437148241814 0
		 -0.73654920213874675 -0.18570794836406668 0.65039052171997813 0 -0.66236021956696223 0.003243251125286048 -0.74917849732713515 0
		 34.339432070581402 92.705217796446703 0.22751122284903458 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_1" -p "R_Pinky_0";
	rename -uid "ABFE9E5C-4B90-F71B-53DD-24990AB276E9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.9701275739303057 -0.0003896231268356587 -0.00035867971266156928 ;
	setAttr ".r" -type "double3" -8.4980445395353328e-015 8.3489560388417272e-015 -1.2945851476894468e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.711001615715066 -3.2056117956273944 19.599490288000133 ;
	setAttr ".bps" -type "matrix" -0.15484431076205557 -0.9862354728160152 0.057989926573459721 0
		 -0.80131607639977176 0.15971042016390163 0.57652851394735483 0 -0.57785446708310517 0.042803899944294642 -0.81501658941500055 0
		 35.020424987139677 87.821637540651253 -0.39570647034545636 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_2" -p "R_Pinky_1";
	rename -uid "996717BD-4947-05D4-92A7-7D92CF32E373";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.5643079116066403 3.8935133346740258e-005 2.5346097629608266e-005 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377365614826499e-007 4.4527765730065075e-014 25.061569604295759 ;
	setAttr ".bps" -type "matrix" -0.47969722473379034 -0.82573243664678531 0.29674318130677046 0
		 -0.66028386884339407 0.56243556894894364 0.4976860891428227 0 -0.57785446708310517 0.042803899944294642 -0.81501658941500055 0
		 34.468516918248163 84.306420787801827 -0.18901428880640841 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Pinky_3" -p "R_Pinky_2";
	rename -uid "869D1896-4E70-1D48-CAA5-569550BC641F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -1.7507241454944307 -8.8864840975588777e-005 -9.2118292315035433e-005 ;
	setAttr ".r" -type "double3" 0 0 2.5444437451708134e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4254468496441868e-015 4.611804288122085e-014 6.0210688115630289 ;
	setAttr ".bps" -type "matrix" -0.54631084571130917 -0.76218098594540029 0.34731053039246063 0
		 -0.60632390248966361 0.64594734368434148 0.46381392223266454 0 -0.57785446708310517 0.042803899944294642 -0.81501658941500055 0
		 33.628739565871221 82.860860205699581 0.3304763196122818 1;
	setAttr ".radi" 0.5517241379310337;
createNode joint -n "R_Pinky_4" -p "R_Pinky_3";
	rename -uid "78BEA841-4CE8-66CC-0EF6-6DAC7F8748F2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.4490322942759377 0.00014165095059581745 0.00022611646230075166 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -0.54631084571130906 -0.76194389892066927 0.34783035341350488 0
		 -0.60632390248966372 0.64626357315736205 0.46337319654851011 0 -0.57785446708310517 0.042247945600333889 -0.81504559747578054 0
		 32.290642146459575 80.994694534566293 1.2117278882745066 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103525;
createNode joint -n "R_Thumb_0" -p "R_Wrist";
	rename -uid "42FC3E03-4A2D-2A4C-1801-CF84E1A7842B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.315948656795868 0.60502947338380864 -2.2020702908751222 ;
	setAttr ".r" -type "double3" -7.1562480332929135e-015 -6.3611093629270351e-015 -2.5444437451708134e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -101.95046059860566 -25.965428211088309 -13.569558919173257 ;
	setAttr ".bps" -type "matrix" 0.06515488578479478 -0.75899365338971603 0.647829819452997 0
		 -0.057443016857054358 -0.65098551735404264 -0.75691357235132795 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.035975848428933 94.38317086786796 4.1733219965685979 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_1" -p "R_Thumb_0";
	rename -uid "61932D09-49E3-E582-5470-BC8C0F759340";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -5.4663913327557587 0.00015107687027082761 -0.0003158433899557167 ;
	setAttr ".r" -type "double3" 0 0 6.3611093629270335e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4464044189932622e-015 -1.8288189418415205e-014 
		9.0441670532607361 ;
	setAttr ".bps" -type "matrix" 0.055315044607155472 -0.85188961456470313 0.52079202224775933 0
		 -0.066970927777490766 -0.52358150682332216 -0.84933933180163101 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.392146500111309 90.234114954493521 7.71469830618262 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_2" -p "R_Thumb_1";
	rename -uid "C9D39DC7-4A76-17F6-9F28-B892615470B6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.4782535867378002 -0.00011350738246385106 0.00033624632317241776 ;
	setAttr ".r" -type "double3" 0 0 1.9083328088781101e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.3194733483923417e-015 -1.1628903054100985e-014 
		22.560097226313406 ;
	setAttr ".bps" -type "matrix" 0.025388657566857317 -0.98757423775451036 0.15508881645866962 0
		 -0.083067896291060248 -0.15668642128205185 -0.98414891657289383 0 0.99622042775318076 0.012103318116170936 -0.086013772256821053 0
		 33.584539321628554 87.27113358601963 9.5260797720295969 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "R_Thumb_3" -p "R_Thumb_2";
	rename -uid "271E5414-444A-5652-51BC-538F8136DB12";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.4128370445909617 -7.3414378270797442e-005 0.00034896718369736845 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.5377364625159387e-007 -2.3696979935122415e-023 1.2589020074589515e-022 ;
	setAttr ".bps" -type "matrix" 0.025388657566857473 -0.98746821781080185 0.15576243090203795 0
		 -0.08306789629106022 -0.15735769885150874 -0.98404180765754823 0 0.99622042775318087 0.012044643029874957 -0.086022008239475256 0
		 33.671182622597989 83.907583529576485 10.083935269972683 1;
	setAttr ".ds" 2;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "C_Neck_0" -p "C_ChestBegin";
	rename -uid "83A0A31F-48DD-C923-B412-F4BF7578FA41";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 25.359253404546521 0.49585129276853479 8.2169913231499697e-015 ;
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
	setAttr ".t" -type "double3" 6.1610734169495345 -7.1054273576010019e-015 -6.3108872417680944e-030 ;
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
	setAttr ".t" -type "double3" 5.5042648571119912 0 3.8055961791890692e-016 ;
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
	setAttr ".t" -type "double3" 4.3289621916327405 -0.74056241803955203 -9.3827666486746244e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4845900818983826e-015 1.2897885128422727e-014 -83.793697841515851 ;
	setAttr ".radi" 1.169502703832018;
createNode joint -n "L_Eye" -p "C_FacialRoot";
	rename -uid "F0F1DFD3-4B47-A705-C6C5-709C6E3D975B";
	setAttr ".t" -type "double3" 5.8028765937914173 2.1768783048587466 -3.2852890586086683 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036369923054885053 90 0 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_Eye" -p "C_FacialRoot";
	rename -uid "3C41E4A6-4D70-D2A6-F357-EE9EB08DE0A5";
	setAttr ".t" -type "double3" 5.8028765937914297 2.1768783048586897 3.2849999999999944 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 6.6208594470752379e-032 2.3854160110976376e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036369923054885053 90 0 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_UpperTeeth" -p "C_FacialRoot";
	rename -uid "C5E109B6-4178-CA58-7A45-FAAF0799FE3D";
	setAttr ".t" -type "double3" 8.236845225292047 -3.5661100942829762 -3.1572692238520917e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2773640411191917e-014 1.9778670992816012e-014 83.793697841515851 ;
createNode joint -n "L_EyelidUpper" -p "C_FacialRoot";
	rename -uid "FBC760A5-4750-3D6E-158B-C7A7333179FD";
	setAttr ".t" -type "double3" 5.8266091275029002 2.2173375396653512 -3.2987138503231908 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036369923054885053 90 0 ;
	setAttr ".radi" 1.5;
createNode joint -n "L_EyelidLower" -p "C_FacialRoot";
	rename -uid "4CF8D120-4FD1-E705-6CDA-EEAD721AB958";
	setAttr ".t" -type "double3" 5.8109734331714531 2.1483594707518421 -3.289884414224487 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036369923054885053 90 0 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidUpper" -p "C_FacialRoot";
	rename -uid "F9C0BA30-4A63-715D-7EA6-DEA23CD021F9";
	setAttr ".t" -type "double3" 5.7948950419162077 2.204991071231035 3.2895299242718297 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036369923054885053 90 0 ;
	setAttr ".radi" 1.5;
createNode joint -n "R_EyelidLower" -p "C_FacialRoot";
	rename -uid "5CC7BE12-4415-A1C3-99AC-DDB67BF982FF";
	setAttr ".t" -type "double3" 5.8110887206762829 2.1479534030172545 3.2803392130401874 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036369923054885053 90 0 ;
	setAttr ".radi" 1.5;
createNode joint -n "C_Jaw" -p "C_FacialRoot";
	rename -uid "90F5DFFD-421B-F522-194C-34BDB73DAB70";
	setAttr ".t" -type "double3" -0.20603759086715367 -1.4900607790721665 0.00027026805165687961 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4845900818983822e-015 1.9258994491349767e-014 -1.1131941385122302e-014 ;
createNode joint -n "C_JawOffset" -p "C_Jaw";
	rename -uid "67831D9B-4EEB-13D9-88C5-D194B5F44EA4";
	setAttr ".t" -type "double3" 0.69999976370784145 0 1.5547459153442134e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -44.024671329798863 ;
createNode joint -n "C_JawEnd" -p "C_JawOffset";
	rename -uid "BF51FCB3-4D3F-F0EA-B6FB-3991FF6726BA";
	setAttr ".t" -type "double3" 9.2614255475660485 0 -2.7403209909571125e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "C_LowerTeeth" -p "C_JawOffset";
	rename -uid "084F43C4-4801-480B-D39B-0B917D15FC4B";
	setAttr ".t" -type "double3" 7.6551522892721096 1.7350943232106744 -4.4511920191392385e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -44.024671329798863 89.999999999999986 0 ;
createNode joint -n "C_LowerLipBegin" -p "C_FacialRoot";
	rename -uid "FDDD9C9F-4578-73AD-DEC6-97BD220011CA";
	setAttr ".t" -type "double3" -0.20603759086715367 -1.4900607790721949 0.00027026805165687956 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 9.9440336432480698e-016 1.8049898351667555e-014 -22.490143822282686 ;
createNode joint -n "C_LowerLipEnd" -p "C_LowerLipBegin";
	rename -uid "B865A7C8-4FD3-DBF9-74B5-4A8C9A50B17B";
	setAttr ".t" -type "double3" 9.4213200452879846 1.1368683772161603e-013 -5.4210108624275222e-020 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "C_Throat" -p "C_Neck_0";
	rename -uid "34C7286E-4A18-C745-3286-85AE3ECE4473";
	setAttr ".t" -type "double3" 6.0380048961246384 -4.7304766549194586 3.44034972153842e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -9.3264352853862587 ;
	setAttr ".radi" 0.5;
createNode joint -n "L_Breast" -p "C_ChestBegin";
	rename -uid "3F4A639A-48A1-379E-57F8-13A94A510781";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 5.9904225855234614 -8.7864674284425099 -7.8906594358327045 ;
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
	setAttr ".t" -type "double3" 5.9903960095492579 -8.7864588067821323 7.89066 ;
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
	setAttr ".t" -type "double3" -1.3722824643070339 -0.021250189231771799 -8.2375185657379006 ;
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
	setAttr ".t" -type "double3" 42.574412456291974 -1.0658141036401503e-014 -1.9539925233402755e-014 ;
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
	setAttr ".t" -type "double3" 42.882476181269666 1.4788170688007085e-013 5.3290705182007514e-015 ;
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
	setAttr ".t" -type "double3" 11.395686988248084 -2.8421709430404007e-014 -5.3290705182007514e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -40.319578859158966 ;
	setAttr ".bps" -type "matrix" 0.10215059601859774 -0.24737070314834397 0.96352114193562921 0
		 -0.023522797391771579 -0.96891771037355545 -0.2462623571058577 0 0.99449079117702799 0.002491133950868047 -0.10479437253845231 0
		 12.992315368191564 4.9293490702579756 4.6457902653503096 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "L_Toe" -p "L_Ball";
	rename -uid "D253813E-4A98-670B-3054-6A8B2EF78F0B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 10.186729757111321 5.3290705182007514e-015 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0.49999999612681695 0 0.49999999612681695 ;
	setAttr ".bps" -type "matrix" 0.10215059877882557 -0.24737070206271949 0.96352114192171456 0
		 -0.023522787492969086 -0.96891771062446264 -0.24626235706419144 0 0.9944907911276446 0.002491144164384583 -0.10479437276430556 0
		 14.032896887052129 2.4096571554708217 14.460000745352577 1;
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
	setAttr ".t" -type "double3" -42.57432505057433 -5.5511151231257827e-015 5.7859833262341454e-006 ;
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
	setAttr ".t" -type "double3" -42.882501399175524 -8.332710632608098e-007 1.0495371293828271e-005 ;
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
	setAttr ".t" -type "double3" -11.395699406441832 -1.0971067689879987e-005 -9.5427450297336236e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "xzy";
	setAttr ".jo" -type "double3" 0 0 -40.31957885915898 ;
	setAttr ".bps" -type "matrix" 0.10215059601859712 0.24737070314834389 -0.96352114193562977 0
		 -0.023522797391812976 0.96891771037355545 0.24626235710585312 0 0.99449079117702699 -0.0024911339508273053 0.10479437253846194 0
		 -12.992299025426934 4.9293534257172151 4.6457890359005187 1;
	setAttr ".radi" 0.97517567709196495;
createNode joint -n "R_Toe" -p "R_Ball";
	rename -uid "F6C386E1-4DE4-D13C-A0DF-E4B110FE7B91";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -10.186732610927153 -8.7764594347561342e-007 -1.9291117467901131e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0.50000190515003462 0 0.49999999612681634 ;
	setAttr ".bps" -type "matrix" 0.10215059877882496 0.24737070206271941 -0.96352114192171479 0
		 -0.023522754356568424 0.96891771054145726 0.24626236055593601 0 0.99449079191142264 -0.0024911764486910365 0.10479436455885126 0
		 -14.032899999999985 2.4096599999999997 14.45999999999998 1;
	setAttr ".radi" 0.97517567709196495;
createNode transform -n "locator_L_Foot_Ext" -p "Elisa_BuilderGrp";
	rename -uid "B966980D-4B3F-6CA5-C8B1-C9B022FFC748";
	setAttr ".t" -type "double3" 17.846928301843754 0 7.2815800637385166 ;
	setAttr ".r" -type "double3" 0 7.5255510185616528 0 ;
createNode locator -n "locator_L_Foot_ExtShape" -p "locator_L_Foot_Ext";
	rename -uid "2A2B6838-493E-40AD-FE3D-52A8E961E3EA";
	setAttr -k off ".v";
createNode transform -n "locator_L_Foot_Int" -p "Elisa_BuilderGrp";
	rename -uid "57F4F6F2-40E0-20C1-5178-D6B61F2FB63C";
	setAttr ".t" -type "double3" 8.5422567423755016 0 7.9961478000971091 ;
createNode locator -n "locator_L_Foot_IntShape" -p "locator_L_Foot_Int";
	rename -uid "8F60CE5B-41BD-34B5-225D-659481109D39";
	setAttr -k off ".v";
createNode transform -n "locator_L_Foot_Base" -p "Elisa_BuilderGrp";
	rename -uid "0BEDCCA8-4D3D-C715-9AE5-5E921B80034F";
	setAttr ".t" -type "double3" 11.860438668243384 0 -6.5621914369771419 ;
createNode locator -n "locator_L_Foot_BaseShape" -p "locator_L_Foot_Base";
	rename -uid "45FFFEC1-4213-D6A6-AF3B-DA85954CBA6D";
	setAttr -k off ".v";
createNode transform -n "locator_L_Foot_BaseSwive" -p "Elisa_BuilderGrp";
	rename -uid "833D0FA0-45E5-53CE-0A94-028DA7E85DB0";
	setAttr ".t" -type "double3" 11.860438668243384 0 -5.078761871046142 ;
createNode locator -n "locator_L_Foot_BaseSwiveShape" -p "locator_L_Foot_BaseSwive";
	rename -uid "84C40DDD-4A56-7EC5-F29F-F387B03CB398";
	setAttr -k off ".v";
createNode transform -n "locator_L_Foot_ToeSwive" -p "Elisa_BuilderGrp";
	rename -uid "B4C7F34F-4C89-99D2-21D8-43BE100B2D96";
	setAttr ".t" -type "double3" 13.28402045162443 0 8.4672370119646434 ;
createNode locator -n "locator_L_Foot_ToeSwiveShape" -p "locator_L_Foot_ToeSwive";
	rename -uid "10B04A00-43D2-0D8F-C5A3-9AA9A4EE5A9B";
	setAttr -k off ".v";
createNode transform -n "locator_L_ArmPV" -p "Elisa_BuilderGrp";
	rename -uid "A2899E0E-4D16-45FC-16D7-F6BB66F09A1E";
	setAttr ".t" -type "double3" 47.138191223144531 146.09976196289062 -48.116950988769531 ;
createNode locator -n "locator_L_ArmPVShape" -p "locator_L_ArmPV";
	rename -uid "43394C4B-48F8-CF42-79DB-E0A2686ED41E";
	setAttr -k off ".v";
createNode transform -n "locator_R_ArmPV" -p "Elisa_BuilderGrp";
	rename -uid "C4EECBBC-492B-1974-4896-BD950BEAC2EC";
	setAttr ".t" -type "double3" -47.138191223144531 146.09976196289062 -48.116950988769531 ;
createNode locator -n "locator_R_ArmPVShape" -p "locator_R_ArmPV";
	rename -uid "30DD9F2A-42B6-7E6F-4E7B-D5A71E3B231E";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 7.1054273576010019e-015 0 0 ;
createNode transform -n "locator_L_LegPV" -p "Elisa_BuilderGrp";
	rename -uid "16B9036F-4FC5-8593-A6F8-A69CB7C828C7";
	setAttr ".t" -type "double3" 9.626434326171875 56.9853515625 49.005508422851563 ;
createNode locator -n "locator_L_LegPVShape" -p "locator_L_LegPV";
	rename -uid "3B554D60-4160-41F4-D2CC-F5961E0E74BF";
	setAttr -k off ".v";
createNode transform -n "locator_R_LegPV" -p "Elisa_BuilderGrp";
	rename -uid "480F59B9-4069-B38D-4785-60AC39AAEA36";
	setAttr ".t" -type "double3" -9.626434326171875 56.9853515625 49.005508422851563 ;
createNode locator -n "locator_R_LegPVShape" -p "locator_R_LegPV";
	rename -uid "89637BCC-4C92-8029-1B06-22BD4B37E5DD";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 0 -7.1054273576010019e-015 ;
createNode transform -n "locator_L_ChestHeadBegin" -p "Elisa_BuilderGrp";
	rename -uid "1453C96C-4D64-31B6-26F7-E284748DAB1D";
	setAttr ".t" -type "double3" 1.228016835740152 148.93232647433274 -1.6945137446791576 ;
createNode locator -n "locator_L_ChestHeadBeginShape" -p "locator_L_ChestHeadBegin";
	rename -uid "4DB8FD04-45A2-96AC-E36B-9EAFBD717098";
	setAttr -k off ".v";
createNode transform -n "locator_L_ChestHeadEnd" -p "Elisa_BuilderGrp";
	rename -uid "90A1BA11-41B1-0BD7-966F-4991B3F86E3F";
	setAttr ".t" -type "double3" 5.4453574642256566 162.5037290874408 -4.9413182981233703 ;
createNode locator -n "locator_L_ChestHeadEndShape" -p "locator_L_ChestHeadEnd";
	rename -uid "66033758-42E3-32FA-8001-4AAF4E1FC819";
	setAttr -k off ".v";
createNode transform -n "locator_R_ChestHeadBegin" -p "Elisa_BuilderGrp";
	rename -uid "E72FDA16-47BA-D76F-E02E-3F9A068C9310";
	setAttr ".t" -type "double3" -1.228016835740152 148.93232647433274 -1.6945137446791576 ;
createNode locator -n "locator_R_ChestHeadBeginShape" -p "locator_R_ChestHeadBegin";
	rename -uid "E192E5BB-4E06-F558-92B2-2FAA5AC58206";
	setAttr -k off ".v";
createNode transform -n "locator_R_ChestHeadEnd" -p "Elisa_BuilderGrp";
	rename -uid "209C89DE-4573-5405-0BBD-E9B2A318FCCA";
	setAttr ".t" -type "double3" -5.4453574642256566 162.5037290874408 -4.9413182981233703 ;
createNode locator -n "locator_R_ChestHeadEndShape" -p "locator_R_ChestHeadEnd";
	rename -uid "059C5CF4-4D39-D598-6043-75B652C320F4";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 8.8817841970012523e-016 0 8.8817841970012523e-016 ;
createNode transform -n "left";
	rename -uid "A27AB1CC-48E2-3552-FDA1-7C810AC662F0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1012.9358765637044 160.72133458161295 2.7795146932845256 ;
	setAttr ".r" -type "double3" 0 -89.999999999999986 0 ;
createNode camera -n "leftShape" -p "left";
	rename -uid "3DC88714-42A0-9E29-5F19-7D93381AEF9D";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 1012.9356062956525;
	setAttr ".ow" 37.16545074074444;
	setAttr ".imn" -type "string" "left1";
	setAttr ".den" -type "string" "left1_depth";
	setAttr ".man" -type "string" "left1_mask";
	setAttr ".tp" -type "double3" -0.0002702680516692979 160.72133458161295 2.7795146932843009 ;
	setAttr ".hc" -type "string" "viewSet -ls %camera";
	setAttr ".o" yes;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "F2A30AD8-4DD3-ED53-B205-F89939C85F27";
	setAttr -s 15 ".lnk";
	setAttr -s 15 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "339C6C94-4783-CFC8-643B-7A982FAEFF27";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "7FB2B463-4D42-B6E1-B847-47B1C3BFAAA2";
createNode displayLayerManager -n "layerManager";
	rename -uid "4DABBAF1-41BB-638F-3D75-F9854E9736BA";
createNode displayLayer -n "defaultLayer";
	rename -uid "C16A99AE-484B-A128-EB09-BAA8563A353E";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "77448BA4-4FBE-8C44-977D-06A3BE4F703F";
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
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1570\n            -height 1054\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n"
		+ "            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n"
		+ "            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n"
		+ "            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n"
		+ "            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n"
		+ "                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n"
		+ "                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n"
		+ "                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n"
		+ "                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n"
		+ "                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n"
		+ "                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n"
		+ "                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n"
		+ "                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n"
		+ "                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n"
		+ "\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1570\\n    -height 1054\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1570\\n    -height 1054\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "8D1B5323-46C8-E467-96E1-878BD9E1C95A";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 24 -ast 0 -aet 250 ";
	setAttr ".st" 6;
createNode renderLayerManager -n "Elisa_Model_renderLayerManager";
	rename -uid "993479EA-4049-E910-C09D-EE8115630A28";
createNode renderLayer -n "Elisa_Model_defaultRenderLayer";
	rename -uid "A9EEB583-4DD5-8F25-5F58-339B5659651A";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager1";
	rename -uid "C36151D0-4E2E-858A-45D1-BDB8A8083F86";
createNode renderLayer -n "defaultRenderLayer1";
	rename -uid "6A97851C-47A0-25B4-6325-AC8746858D82";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager2";
	rename -uid "9703E420-43CB-7A2F-98F0-76936E6B8965";
createNode renderLayer -n "defaultRenderLayer2";
	rename -uid "207185DB-4F01-D8A8-3AF3-FA80B42E264C";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager3";
	rename -uid "94962BE2-4E9D-068E-11BC-9BBDF894039F";
createNode renderLayer -n "defaultRenderLayer3";
	rename -uid "321300FA-4DA4-6392-C2D9-F59A0C2F8473";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager4";
	rename -uid "93B22343-42E8-FFD4-3285-D9BCD570D65E";
createNode renderLayer -n "defaultRenderLayer4";
	rename -uid "A2495691-42A1-C18E-E5E3-E19C47B19C9C";
	setAttr ".g" yes;
createNode renderLayerManager -n "renderLayerManager5";
	rename -uid "818D6BC1-455E-7BB3-BC48-B185D56FF83A";
createNode renderLayer -n "defaultRenderLayer5";
	rename -uid "7B8BA366-431D-2F4E-6CBA-2B9A3D7F0925";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "4609FC7F-4784-5972-0955-E5A4B848011E";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1010.1190074805246 -414.28569782347978 ;
	setAttr ".tgi[0].vh" -type "double2" 967.26186632637166 730.95235190694416 ;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".msaa" yes;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
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
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -s 7 ".r";
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
select -ne :defaultRenderGlobals;
	setAttr ".mcfr" 30;
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
	setAttr -k on ".hwfr" 30;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
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
connectAttr "C_Jaw.s" "C_JawOffset.is";
connectAttr "C_JawOffset.s" "C_JawEnd.is";
connectAttr "C_JawOffset.s" "C_LowerTeeth.is";
connectAttr "C_FacialRoot.s" "C_LowerLipBegin.is";
connectAttr "C_LowerLipBegin.s" "C_LowerLipEnd.is";
connectAttr "C_Neck_0.s" "C_Throat.is";
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
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Elisa_Model_renderLayerManager.rlmi[0]" "Elisa_Model_defaultRenderLayer.rlid"
		;
connectAttr "renderLayerManager1.rlmi[0]" "defaultRenderLayer1.rlid";
connectAttr "renderLayerManager2.rlmi[0]" "defaultRenderLayer2.rlid";
connectAttr "renderLayerManager3.rlmi[0]" "defaultRenderLayer3.rlid";
connectAttr "renderLayerManager4.rlmi[0]" "defaultRenderLayer4.rlid";
connectAttr "renderLayerManager5.rlmi[0]" "defaultRenderLayer5.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "Elisa_Model_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer2.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer3.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer4.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer5.msg" ":defaultRenderingList1.r" -na;
// End of Elisa_Builder.ma
