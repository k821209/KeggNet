import requests

inText = '''
ko00001 KEGG Orthology (KO) (157)

  ko:K06611 E2.4.1.67; stachyose synthetase [EC:2.4.1.67]
  ko:K01512 acyP; acylphosphatase [EC:3.6.1.7]
  ko:K01601 rbcL; ribulose-bisphosphate carboxylase large chain [EC:4.1.1.39]
  ko:K00122 FDH; formate dehydrogenase [EC:1.17.1.9]
  ko:K19517 MIK; 1D-myo-inositol 3-kinase [EC:2.7.1.64]
  ko:K00915 IPMK; inositol-polyphosphate multikinase [EC:2.7.1.140 2.7.1.151]
  ko:K00416 QCR6; ubiquinol-cytochrome c reductase subunit 6
  ko:K02266 COX6A; cytochrome c oxidase subunit 6a
  ko:K02108 ATPF0A; F-type H+-transporting ATPase subunit a
  ko:K02110 ATPF0C; F-type H+-transporting ATPase subunit c
  ko:K02709 psbH; photosystem II PsbH protein
  ko:K02724 psbZ; photosystem II PsbZ protein
  ko:K08902 psb27; photosystem II Psb27 protein
  ko:K08903 psb28; photosystem II 13kDa protein
  ko:K02689 psaA; photosystem I P700 chlorophyll a apoprotein A1
  ko:K02697 psaJ; photosystem I subunit IX
  ko:K02634 petA; apocytochrome f
  ko:K02637 petD; cytochrome b6-f complex subunit 4
  ko:K13034 ATCYSC1; L-3-cyanoalanine synthase/ cysteine synthase [EC:2.5.1.47 4.4.1.9]
  ko:K07408 CYP1A1; cytochrome P450 family 1 subfamily A polypeptide 1 [EC:1.14.14.1]
  ko:K01832 TBXAS1; thromboxane-A synthase [EC:5.3.99.5]
  ko:K15718 LOX1_5; linoleate 9S-lipoxygenase [EC:1.13.11.58]
  ko:K10528 HPL; hydroperoxide lyase [EC:4.1.2.-]
  ko:K18858 CHAT; (Z)-3-hexen-1-ol acetyltransferase [EC:2.3.1.195]
  ko:K06928 NTPCR; nucleoside-triphosphatase [EC:3.6.1.15]
  ko:K01522 FHIT; bis(5'-adenosyl)-triphosphatase [EC:3.6.1.29]
  ko:K00133 asd; aspartate-semialdehyde dehydrogenase [EC:1.2.1.11]
  ko:K00422 E1.10.3.1; polyphenol oxidase [EC:1.10.3.1]
  ko:K11818 CYP83B1; aromatic aldoxime N-monooxygenase [EC:1.14.14.45]
  ko:K09658 DPM2; dolichol phosphate-mannose biosynthesis regulatory protein
  ko:K09659 DPM3; dolichol-phosphate mannosyltransferase subunit 3
  ko:K05531 MNN10; mannan polymerase II complex MNN10 subunit [EC:2.4.1.-]
  ko:K13248 PHOSPHO2; pyridoxal phosphate phosphatase PHOSPHO2 [EC:3.1.3.74]
  ko:K18551 SDT1; pyrimidine and pyridine-specific 5'-nucleotidase [EC:3.1.3.-]
  ko:K03426 E3.6.1.22; NAD+ diphosphatase [EC:3.6.1.22]
  ko:K15086 TPS14; (3S)-linalool synthase [EC:4.2.3.25]
  ko:K04122 GA3; ent-kaurene oxidase [EC:1.14.14.86]
  ko:K17913 CCD8; carlactone synthase / all-trans-10'-apo-beta-carotenal 13,14-cleaving dioxygenase [EC:1.13.11.69 1.13.11.70]
  ko:K12639 CYP724B1; cytochrome P450 family 724 subfamily B polypeptide 1 [EC:1.14.13.-]
  ko:K13223 BX2; indole-2-monooxygenase [EC:1.14.14.153]
  ko:K03043 rpoB; DNA-directed RNA polymerase subunit beta [EC:2.7.7.6]
  ko:K03009 RPB12; DNA-directed RNA polymerases I, II, and III subunit RPABC4
  ko:K10845 TTDA; TFIIH basal transcription factor complex TTD-A subunit
  ko:K12832 SF3B5; splicing factor 3B subunit 5
  ko:K12624 LSM5; U6 snRNA-associated Sm-like protein LSm5
  ko:K12896 SFRS7; splicing factor, arginine/serine-rich 7
  ko:K02986 RP-S4; small subunit ribosomal protein S4
  ko:K02994 RP-S8; small subunit ribosomal protein S8
  ko:K02983 RP-S30e; small subunit ribosomal protein S30e
  ko:K02887 RP-L20; large subunit ribosomal protein L20
  ko:K02924 RP-L39e; large subunit ribosomal protein L39e
  ko:K03538 POP4; ribonuclease P protein subunit POP4 [EC:3.1.26.5]
  ko:K14288 XPOT; exportin-T
  ko:K04554 UBE2J2; ubiquitin-conjugating enzyme E2 J2 [EC:2.3.2.23]
  ko:K08504 BET1; blocked early in transport 1
  ko:K05641 ABCA1; ATP-binding cassette, subfamily A (ABC1), member 1
  ko:K13411 DUOX; dual oxidase [EC:1.6.3.1 1.11.1.-]
  ko:K19704 PTC1; protein phosphatase PTC1 [EC:3.1.3.16]
  ko:K14495 GID2; F-box protein GID2
  ko:K18461 WASH1; WAS protein family homolog 1
  ko:K13289 CTSA; cathepsin A (carboxypeptidase C) [EC:3.4.16.5]
  ko:K19748 GORAB; RAB6-interacting golgin
  ko:K05747 WAS; Wiskott-Aldrich syndrome protein
  ko:K07192 FLOT; flotillin
  ko:K12127 TOC1; pseudo-response regulator 1
  ko:K18177 COA4; cytochrome c oxidase assembly factor 4
  ko:K18178 COA5; cytochrome c oxidase assembly factor 5
  ko:K13428 EFR; LRR receptor-like serine/threonine-protein kinase EFR [EC:2.7.11.1]
  ko:K13457 RPM1; disease resistance protein RPM1
  ko:K13460 RPS5; disease resistance protein RPS5
  ko:K08956 AFG3; AFG3 family protein [EC:3.4.24.-]
  ko:K17553 PPP1R11; protein phosphatase 1 regulatory subunit 11
  ko:K11844 USP16_45; ubiquitin carboxyl-terminal hydrolase 16/45 [EC:3.4.19.12]
  ko:K15235 JOSD; josephin [EC:3.4.19.12]
  ko:K16296 SCPL-I; serine carboxypeptidase-like clade I [EC:3.4.16.-]
  ko:K08657 TASP1; taspase, threonine aspartase, 1 [EC:3.4.25.-]
  ko:K13692 IAGLU; UDP-glucose:(indol-3-yl)acetate beta-D-glucosyltransferase [EC:2.4.1.121]
  ko:K05527 bolA; BolA family transcriptional regulator, general stress-responsive regulator
  ko:K15437 AIMP1; aminoacyl tRNA synthase complex-interacting multifunctional protein 1
  ko:K09512 DNAJB6; DnaJ homolog subfamily B member 6
  ko:K09539 DNAJC19; DnaJ homolog subfamily C member 19
  ko:K04798 pfdB; prefoldin beta subunit
  ko:K08742 SIAH2; E3 ubiquitin-protein ligase SIAH2 [EC:2.3.2.27]
  ko:K15683 NFXL1; NF-X1-type zinc finger protein NFXL1
  ko:K19038 ATL41; E3 ubiquitin-protein ligase ATL41 [EC:2.3.2.27]
  ko:K16281 RHA1; RING-H2 zinc finger protein RHA1
  ko:K16285 XERICO; RING/U-box domain-containing protein [EC:2.3.2.27]
  ko:K12175 GPS1; COP9 signalosome complex subunit 1
  ko:K11672 ACTR5; actin-related protein 5
  ko:K15271 HFM1; ATP-dependent DNA helicase HFM1/MER3 [EC:3.6.4.12]
  ko:K18185 COX23; cytochrome c oxidase assembly protein subunit 23
  ko:K17972 NAA20; N-terminal acetyltransferase B complex catalytic subunit [EC:2.3.1.254]
  ko:K13862 SLC4A11; solute carrier family 4 (sodium borate transporter), member 11
  ko:K03322 mntH; manganese transport protein
  ko:K17292 TBCA; tubulin-specific chaperone A
  ko:K00464 diox1; all-trans-8'-apo-beta-carotenal 15,15'-oxygenase [EC:1.13.11.75]
  ko:K19706 FAH; dihydroceramide fatty acyl 2-hydroxylase [EC:1.14.18.7]
  ko:K16219 NTMT1; protein N-terminal methyltransferase [EC:2.1.1.244]
  ko:K19861 BEBT; benzyl alcohol O-benzoyltransferase [EC:2.3.1.196 2.3.1.232]
  ko:K01531 mgtA; P-type Mg2+ transporter [EC:7.2.2.14]
  ko:K07478 ycaJ; putative ATPase
  ko:K18813 
  ko:K00750 GYG1; glycogenin [EC:2.4.1.186]
  ko:K01176 AMY; alpha-amylase [EC:3.2.1.1]
  ko:K05573 ndhB; NAD(P)H-quinone oxidoreductase subunit 2 [EC:7.1.1.2]
  ko:K05581 ndhJ; NAD(P)H-quinone oxidoreductase subunit J [EC:7.1.1.2]
  ko:K03945 NDUFA1; NADH dehydrogenase (ubiquinone) 1 alpha subcomplex subunit 1
  ko:K02153 ATPeV0E; V-type H+-transporting ATPase subunit e
  ko:K02706 psbD; photosystem II P680 reaction center D2 protein [EC:1.10.3.9]
  ko:K02708 psbF; photosystem II cytochrome b559 subunit beta
  ko:K02718 psbT; photosystem II PsbT protein
  ko:K02690 psaB; photosystem I P700 chlorophyll a apoprotein A2
  ko:K02696 psaI; photosystem I subunit VIII
  ko:K02640 petG; cytochrome b6-f complex subunit 5
  ko:K07410 CYP1B1; cytochrome P450 family 1 subfamily B polypeptide 1 [EC:1.14.14.1]
  ko:K06124 PHOSPHO1; phosphoethanolamine/phosphocholine phosphatase [EC:3.1.3.75]
  ko:K04715 CERK; ceramide kinase [EC:2.7.1.138]
  ko:K10526 OPCL1; OPC-8:0 CoA ligase 1 [EC:6.2.1.-]
  ko:K08241 E2.1.1.141; jasmonate O-methyltransferase [EC:2.1.1.141]
  ko:K16329 psuG; pseudouridylate synthase [EC:4.2.1.70]
  ko:K00499 CMO; choline monooxygenase [EC:1.14.15.7]
  ko:K11868 CYP71A13; indoleacetaldoxime dehydratase [EC:4.99.1.6]
  ko:K13029 CYP71E1; 4-hydroxyphenylacetaldehyde oxime monooxygenase [EC:1.14.14.37]
  ko:K01444 AGA; N4-(beta-N-acetylglucosaminyl)-L-asparaginase [EC:3.5.1.26]
  ko:K02548 menA; 1,4-dihydroxy-2-naphthoate polyprenyltransferase [EC:2.5.1.74]
  ko:K17912 CCD7; 9-cis-beta-carotene 9',10'-cleaving dioxygenase [EC:1.13.11.68]
  ko:K03040 rpoA; DNA-directed RNA polymerase subunit alpha [EC:2.7.7.6]
  ko:K03046 rpoC; DNA-directed RNA polymerase subunit beta' [EC:2.7.7.6]
  ko:K03006 RPB1; DNA-directed RNA polymerase II subunit RPB1 [EC:2.7.7.6]
  ko:K12621 LSM2; U6 snRNA-associated Sm-like protein LSm2
  ko:K02950 RP-S12; small subunit ribosomal protein S12
  ko:K02886 RP-L2; large subunit ribosomal protein L2
  ko:K02878 RP-L16; large subunit ribosomal protein L16
  ko:K02917 RP-L35Ae; large subunit ribosomal protein L35Ae
  ko:K03537 POP5; ribonuclease P/MRP protein subunit POP5 [EC:3.1.26.5]
  ko:K14398 CPSF6_7; cleavage and polyadenylation specificity factor subunit 6/7
  ko:K10583 UBE2S; ubiquitin-conjugating enzyme E2 S [EC:2.3.2.23]
  ko:K11864 BRCC3; BRCA1/BRCA2-containing complex subunit 3 [EC:3.4.19.-]
  ko:K15360 STRA13; centromere protein X
  ko:K05643 ABCA3; ATP-binding cassette, subfamily A (ABC1), member 3
  ko:K17771 TOM7; mitochondrial import receptor subunit TOM7
  ko:K08762 DBI; diazepam-binding inhibitor (GABA receptor modulator, acyl-CoA-binding protein)
  ko:K18182 COX16; cytochrome c oxidase assembly protein subunit 16
  ko:K18173 COA1; cytochrome c oxidase assembly factor 1
  ko:K16290 XCP; xylem cysteine proteinase [EC:3.4.22.-]
  ko:K07426 CYP4B1; cytochrome P450 family 4 subfamily B polypeptide 1 [EC:1.14.14.1]
  ko:K18485 MYF6; myogenic factor 6
  ko:K09566 PPIG; peptidyl-prolyl isomerase G (cyclophilin G) [EC:5.2.1.8]
  ko:K19373 DNAJC28; DnaJ homolog subfamily C member 28
  ko:K07890 RAB21; Ras-related protein Rab-21
  ko:K17778 TIM10; mitochondrial import inner membrane translocase subunit TIM10
  ko:K17783 ERV1; mitochondrial FAD-linked sulfhydryl oxidase [EC:1.8.3.2]
  ko:K18187 PET100F; protein PET100, fungi type
  ko:K17469 SULTR2; sulfate transporter 2, low-affinity
  ko:K18848 IAMT1; indole-3-acetate O-methyltransferase [EC:2.1.1.278]
  ko:K02200 ccmH; cytochrome c-type biogenesis protein CcmH
  ko:K02715 psbN; PsbN protein

ko01000 Enzymes (77)

  ko:K00133 asd; aspartate-semialdehyde dehydrogenase [EC:1.2.1.11]
  ko:K13411 DUOX; dual oxidase [EC:1.6.3.1 1.11.1.-]
  ko:K00422 E1.10.3.1; polyphenol oxidase [EC:1.10.3.1]
  ko:K15718 LOX1_5; linoleate 9S-lipoxygenase [EC:1.13.11.58]
  ko:K17913 CCD8; carlactone synthase / all-trans-10'-apo-beta-carotenal 13,14-cleaving dioxygenase [EC:1.13.11.69 1.13.11.70]
  ko:K00464 diox1; all-trans-8'-apo-beta-carotenal 15,15'-oxygenase [EC:1.13.11.75]
  ko:K12639 CYP724B1; cytochrome P450 family 724 subfamily B polypeptide 1 [EC:1.14.13.-]
  ko:K07408 CYP1A1; cytochrome P450 family 1 subfamily A polypeptide 1 [EC:1.14.14.1]
  ko:K11818 CYP83B1; aromatic aldoxime N-monooxygenase [EC:1.14.14.45]
  ko:K04122 GA3; ent-kaurene oxidase [EC:1.14.14.86]
  ko:K13223 BX2; indole-2-monooxygenase [EC:1.14.14.153]
  ko:K19706 FAH; dihydroceramide fatty acyl 2-hydroxylase [EC:1.14.18.7]
  ko:K00122 FDH; formate dehydrogenase [EC:1.17.1.9]
  ko:K16219 NTMT1; protein N-terminal methyltransferase [EC:2.1.1.244]
  ko:K18858 CHAT; (Z)-3-hexen-1-ol acetyltransferase [EC:2.3.1.195]
  ko:K19861 BEBT; benzyl alcohol O-benzoyltransferase [EC:2.3.1.196 2.3.1.232]
  ko:K17972 NAA20; N-terminal acetyltransferase B complex catalytic subunit [EC:2.3.1.254]
  ko:K04554 UBE2J2; ubiquitin-conjugating enzyme E2 J2 [EC:2.3.2.23]
  ko:K08742 SIAH2; E3 ubiquitin-protein ligase SIAH2 [EC:2.3.2.27]
  ko:K16285 XERICO; RING/U-box domain-containing protein [EC:2.3.2.27]
  ko:K19038 ATL41; E3 ubiquitin-protein ligase ATL41 [EC:2.3.2.27]
  ko:K06611 E2.4.1.67; stachyose synthetase [EC:2.4.1.67]
  ko:K13692 IAGLU; UDP-glucose:(indol-3-yl)acetate beta-D-glucosyltransferase [EC:2.4.1.121]
  ko:K05531 MNN10; mannan polymerase II complex MNN10 subunit [EC:2.4.1.-]
  ko:K13034 ATCYSC1; L-3-cyanoalanine synthase/ cysteine synthase [EC:2.5.1.47 4.4.1.9]
  ko:K19517 MIK; 1D-myo-inositol 3-kinase [EC:2.7.1.64]
  ko:K00915 IPMK; inositol-polyphosphate multikinase [EC:2.7.1.140 2.7.1.151]
  ko:K03043 rpoB; DNA-directed RNA polymerase subunit beta [EC:2.7.7.6]
  ko:K13428 EFR; LRR receptor-like serine/threonine-protein kinase EFR [EC:2.7.11.1]
  ko:K19704 PTC1; protein phosphatase PTC1 [EC:3.1.3.16]
  ko:K13248 PHOSPHO2; pyridoxal phosphate phosphatase PHOSPHO2 [EC:3.1.3.74]
  ko:K18551 SDT1; pyrimidine and pyridine-specific 5'-nucleotidase [EC:3.1.3.-]
  ko:K03538 POP4; ribonuclease P protein subunit POP4 [EC:3.1.26.5]
  ko:K13289 CTSA; cathepsin A (carboxypeptidase C) [EC:3.4.16.5]
  ko:K16296 SCPL-I; serine carboxypeptidase-like clade I [EC:3.4.16.-]
  ko:K11844 USP16_45; ubiquitin carboxyl-terminal hydrolase 16/45 [EC:3.4.19.12]
  ko:K15235 JOSD; josephin [EC:3.4.19.12]
  ko:K08956 AFG3; AFG3 family protein [EC:3.4.24.-]
  ko:K08657 TASP1; taspase, threonine aspartase, 1 [EC:3.4.25.-]
  ko:K01512 acyP; acylphosphatase [EC:3.6.1.7]
  ko:K06928 NTPCR; nucleoside-triphosphatase [EC:3.6.1.15]
  ko:K03426 E3.6.1.22; NAD+ diphosphatase [EC:3.6.1.22]
  ko:K01522 FHIT; bis(5'-adenosyl)-triphosphatase [EC:3.6.1.29]
  ko:K15271 HFM1; ATP-dependent DNA helicase HFM1/MER3 [EC:3.6.4.12]
  ko:K01601 rbcL; ribulose-bisphosphate carboxylase large chain [EC:4.1.1.39]
  ko:K10528 HPL; hydroperoxide lyase [EC:4.1.2.-]
  ko:K15086 TPS14; (3S)-linalool synthase [EC:4.2.3.25]
  ko:K01832 TBXAS1; thromboxane-A synthase [EC:5.3.99.5]
  ko:K01531 mgtA; P-type Mg2+ transporter [EC:7.2.2.14]
  ko:K17783 ERV1; mitochondrial FAD-linked sulfhydryl oxidase [EC:1.8.3.2]
  ko:K02706 psbD; photosystem II P680 reaction center D2 protein [EC:1.10.3.9]
  ko:K17912 CCD7; 9-cis-beta-carotene 9',10'-cleaving dioxygenase [EC:1.13.11.68]
  ko:K07410 CYP1B1; cytochrome P450 family 1 subfamily B polypeptide 1 [EC:1.14.14.1]
  ko:K07426 CYP4B1; cytochrome P450 family 4 subfamily B polypeptide 1 [EC:1.14.14.1]
  ko:K13029 CYP71E1; 4-hydroxyphenylacetaldehyde oxime monooxygenase [EC:1.14.14.37]
  ko:K00499 CMO; choline monooxygenase [EC:1.14.15.7]
  ko:K08241 E2.1.1.141; jasmonate O-methyltransferase [EC:2.1.1.141]
  ko:K18848 IAMT1; indole-3-acetate O-methyltransferase [EC:2.1.1.278]
  ko:K10583 UBE2S; ubiquitin-conjugating enzyme E2 S [EC:2.3.2.23]
  ko:K00750 GYG1; glycogenin [EC:2.4.1.186]
  ko:K02548 menA; 1,4-dihydroxy-2-naphthoate polyprenyltransferase [EC:2.5.1.74]
  ko:K04715 CERK; ceramide kinase [EC:2.7.1.138]
  ko:K03006 RPB1; DNA-directed RNA polymerase II subunit RPB1 [EC:2.7.7.6]
  ko:K03040 rpoA; DNA-directed RNA polymerase subunit alpha [EC:2.7.7.6]
  ko:K03046 rpoC; DNA-directed RNA polymerase subunit beta' [EC:2.7.7.6]
  ko:K06124 PHOSPHO1; phosphoethanolamine/phosphocholine phosphatase [EC:3.1.3.75]
  ko:K03537 POP5; ribonuclease P/MRP protein subunit POP5 [EC:3.1.26.5]
  ko:K01176 AMY; alpha-amylase [EC:3.2.1.1]
  ko:K11864 BRCC3; BRCA1/BRCA2-containing complex subunit 3 [EC:3.4.19.-]
  ko:K16290 XCP; xylem cysteine proteinase [EC:3.4.22.-]
  ko:K01444 AGA; N4-(beta-N-acetylglucosaminyl)-L-asparaginase [EC:3.5.1.26]
  ko:K16329 psuG; pseudouridylate synthase [EC:4.2.1.70]
  ko:K11868 CYP71A13; indoleacetaldoxime dehydratase [EC:4.99.1.6]
  ko:K09566 PPIG; peptidyl-prolyl isomerase G (cyclophilin G) [EC:5.2.1.8]
  ko:K10526 OPCL1; OPC-8:0 CoA ligase 1 [EC:6.2.1.-]
  ko:K05573 ndhB; NAD(P)H-quinone oxidoreductase subunit 2 [EC:7.1.1.2]
  ko:K05581 ndhJ; NAD(P)H-quinone oxidoreductase subunit J [EC:7.1.1.2]

ko00194 Photosynthesis proteins (16)

  ko:K02709 psbH; photosystem II PsbH protein
  ko:K02724 psbZ; photosystem II PsbZ protein
  ko:K08902 psb27; photosystem II Psb27 protein
  ko:K08903 psb28; photosystem II 13kDa protein
  ko:K02689 psaA; photosystem I P700 chlorophyll a apoprotein A1
  ko:K02697 psaJ; photosystem I subunit IX
  ko:K02634 petA; apocytochrome f
  ko:K02637 petD; cytochrome b6-f complex subunit 4
  ko:K02110 ATPF0C; F-type H+-transporting ATPase subunit c
  ko:K02108 ATPF0A; F-type H+-transporting ATPase subunit a
  ko:K02706 psbD; photosystem II P680 reaction center D2 protein [EC:1.10.3.9]
  ko:K02708 psbF; photosystem II cytochrome b559 subunit beta
  ko:K02718 psbT; photosystem II PsbT protein
  ko:K02690 psaB; photosystem I P700 chlorophyll a apoprotein A2
  ko:K02696 psaI; photosystem I subunit VIII
  ko:K02640 petG; cytochrome b6-f complex subunit 5

ko03029 Mitochondrial biogenesis (13)

  ko:K03538 POP4; ribonuclease P protein subunit POP4 [EC:3.1.26.5]
  ko:K09539 DNAJC19; DnaJ homolog subfamily C member 19
  ko:K18177 COA4; cytochrome c oxidase assembly factor 4
  ko:K18178 COA5; cytochrome c oxidase assembly factor 5
  ko:K18185 COX23; cytochrome c oxidase assembly protein subunit 23
  ko:K17972 NAA20; N-terminal acetyltransferase B complex catalytic subunit [EC:2.3.1.254]
  ko:K03537 POP5; ribonuclease P/MRP protein subunit POP5 [EC:3.1.26.5]
  ko:K17771 TOM7; mitochondrial import receptor subunit TOM7
  ko:K17778 TIM10; mitochondrial import inner membrane translocase subunit TIM10
  ko:K17783 ERV1; mitochondrial FAD-linked sulfhydryl oxidase [EC:1.8.3.2]
  ko:K18173 COA1; cytochrome c oxidase assembly factor 1
  ko:K18182 COX16; cytochrome c oxidase assembly protein subunit 16
  ko:K18187 PET100F; protein PET100, fungi type

ko04121 Ubiquitin system (13)

  ko:K02983 RP-S30e; small subunit ribosomal protein S30e
  ko:K04554 UBE2J2; ubiquitin-conjugating enzyme E2 J2 [EC:2.3.2.23]
  ko:K08742 SIAH2; E3 ubiquitin-protein ligase SIAH2 [EC:2.3.2.27]
  ko:K15683 NFXL1; NF-X1-type zinc finger protein NFXL1
  ko:K19038 ATL41; E3 ubiquitin-protein ligase ATL41 [EC:2.3.2.27]
  ko:K16281 RHA1; RING-H2 zinc finger protein RHA1
  ko:K16285 XERICO; RING/U-box domain-containing protein [EC:2.3.2.27]
  ko:K14495 GID2; F-box protein GID2
  ko:K11844 USP16_45; ubiquitin carboxyl-terminal hydrolase 16/45 [EC:3.4.19.12]
  ko:K15235 JOSD; josephin [EC:3.4.19.12]
  ko:K12175 GPS1; COP9 signalosome complex subunit 1
  ko:K10583 UBE2S; ubiquitin-conjugating enzyme E2 S [EC:2.3.2.23]
  ko:K11864 BRCC3; BRCA1/BRCA2-containing complex subunit 3 [EC:3.4.19.-]

ko00199 Cytochrome P450 (11)

  ko:K07408 CYP1A1; cytochrome P450 family 1 subfamily A polypeptide 1 [EC:1.14.14.1]
  ko:K01832 TBXAS1; thromboxane-A synthase [EC:5.3.99.5]
  ko:K13223 BX2; indole-2-monooxygenase [EC:1.14.14.153]
  ko:K10528 HPL; hydroperoxide lyase [EC:4.1.2.-]
  ko:K11818 CYP83B1; aromatic aldoxime N-monooxygenase [EC:1.14.14.45]
  ko:K04122 GA3; ent-kaurene oxidase [EC:1.14.14.86]
  ko:K12639 CYP724B1; cytochrome P450 family 724 subfamily B polypeptide 1 [EC:1.14.13.-]
  ko:K07410 CYP1B1; cytochrome P450 family 1 subfamily B polypeptide 1 [EC:1.14.14.1]
  ko:K07426 CYP4B1; cytochrome P450 family 4 subfamily B polypeptide 1 [EC:1.14.14.1]
  ko:K11868 CYP71A13; indoleacetaldoxime dehydratase [EC:4.99.1.6]
  ko:K13029 CYP71E1; 4-hydroxyphenylacetaldehyde oxime monooxygenase [EC:1.14.14.37]

ko04131 Membrane trafficking (9)

  ko:K08504 BET1; blocked early in transport 1
  ko:K07192 FLOT; flotillin
  ko:K18461 WASH1; WAS protein family homolog 1
  ko:K19748 GORAB; RAB6-interacting golgin
  ko:K13289 CTSA; cathepsin A (carboxypeptidase C) [EC:3.4.16.5]
  ko:K13411 DUOX; dual oxidase [EC:1.6.3.1 1.11.1.-]
  ko:K05747 WAS; Wiskott-Aldrich syndrome protein
  ko:K07890 RAB21; Ras-related protein Rab-21
  ko:K17771 TOM7; mitochondrial import receptor subunit TOM7

ko03011 Ribosome (9)

  ko:K02983 RP-S30e; small subunit ribosomal protein S30e
  ko:K02924 RP-L39e; large subunit ribosomal protein L39e
  ko:K02887 RP-L20; large subunit ribosomal protein L20
  ko:K02986 RP-S4; small subunit ribosomal protein S4
  ko:K02994 RP-S8; small subunit ribosomal protein S8
  ko:K02917 RP-L35Ae; large subunit ribosomal protein L35Ae
  ko:K02950 RP-S12; small subunit ribosomal protein S12
  ko:K02886 RP-L2; large subunit ribosomal protein L2
  ko:K02878 RP-L16; large subunit ribosomal protein L16

ko03400 DNA repair and recombination proteins (9)

  ko:K03009 RPB12; DNA-directed RNA polymerases I, II, and III subunit RPABC4
  ko:K10845 TTDA; TFIIH basal transcription factor complex TTD-A subunit
  ko:K15271 HFM1; ATP-dependent DNA helicase HFM1/MER3 [EC:3.6.4.12]
  ko:K03043 rpoB; DNA-directed RNA polymerase subunit beta [EC:2.7.7.6]
  ko:K03006 RPB1; DNA-directed RNA polymerase II subunit RPB1 [EC:2.7.7.6]
  ko:K11864 BRCC3; BRCA1/BRCA2-containing complex subunit 3 [EC:3.4.19.-]
  ko:K15360 STRA13; centromere protein X
  ko:K03046 rpoC; DNA-directed RNA polymerase subunit beta' [EC:2.7.7.6]
  ko:K03040 rpoA; DNA-directed RNA polymerase subunit alpha [EC:2.7.7.6]

ko01002 Peptidases and inhibitors (8)

  ko:K11844 USP16_45; ubiquitin carboxyl-terminal hydrolase 16/45 [EC:3.4.19.12]
  ko:K15235 JOSD; josephin [EC:3.4.19.12]
  ko:K08956 AFG3; AFG3 family protein [EC:3.4.24.-]
  ko:K13289 CTSA; cathepsin A (carboxypeptidase C) [EC:3.4.16.5]
  ko:K16296 SCPL-I; serine carboxypeptidase-like clade I [EC:3.4.16.-]
  ko:K08657 TASP1; taspase, threonine aspartase, 1 [EC:3.4.25.-]
  ko:K16290 XCP; xylem cysteine proteinase [EC:3.4.22.-]
  ko:K11864 BRCC3; BRCA1/BRCA2-containing complex subunit 3 [EC:3.4.19.-]

ko03110 Chaperones and folding catalysts (8)

  ko:K09512 DNAJB6; DnaJ homolog subfamily B member 6
  ko:K09539 DNAJC19; DnaJ homolog subfamily C member 19
  ko:K04798 pfdB; prefoldin beta subunit
  ko:K08956 AFG3; AFG3 family protein [EC:3.4.24.-]
  ko:K02108 ATPF0A; F-type H+-transporting ATPase subunit a
  ko:K13289 CTSA; cathepsin A (carboxypeptidase C) [EC:3.4.16.5]
  ko:K19373 DNAJC28; DnaJ homolog subfamily C member 28
  ko:K09566 PPIG; peptidyl-prolyl isomerase G (cyclophilin G) [EC:5.2.1.8]

ko02000 Transporters (7)

  ko:K05641 ABCA1; ATP-binding cassette, subfamily A (ABC1), member 1
  ko:K13862 SLC4A11; solute carrier family 4 (sodium borate transporter), member 11
  ko:K03322 mntH; manganese transport protein
  ko:K05643 ABCA3; ATP-binding cassette, subfamily A (ABC1), member 3
  ko:K17469 SULTR2; sulfate transporter 2, low-affinity
  ko:K17771 TOM7; mitochondrial import receptor subunit TOM7
  ko:K17778 TIM10; mitochondrial import inner membrane translocase subunit TIM10

ko03021 Transcription machinery (6)

  ko:K03009 RPB12; DNA-directed RNA polymerases I, II, and III subunit RPABC4
  ko:K10845 TTDA; TFIIH basal transcription factor complex TTD-A subunit
  ko:K03043 rpoB; DNA-directed RNA polymerase subunit beta [EC:2.7.7.6]
  ko:K03006 RPB1; DNA-directed RNA polymerase II subunit RPB1 [EC:2.7.7.6]
  ko:K03040 rpoA; DNA-directed RNA polymerase subunit alpha [EC:2.7.7.6]
  ko:K03046 rpoC; DNA-directed RNA polymerase subunit beta' [EC:2.7.7.6]

ko03041 Spliceosome (5)

  ko:K12896 SFRS7; splicing factor, arginine/serine-rich 7
  ko:K12832 SF3B5; splicing factor 3B subunit 5
  ko:K12624 LSM5; U6 snRNA-associated Sm-like protein LSm5
  ko:K12621 LSM2; U6 snRNA-associated Sm-like protein LSm2
  ko:K09566 PPIG; peptidyl-prolyl isomerase G (cyclophilin G) [EC:5.2.1.8]

ko01009 Protein phosphatases and associated proteins (4)

  ko:K17553 PPP1R11; protein phosphatase 1 regulatory subunit 11
  ko:K19704 PTC1; protein phosphatase PTC1 [EC:3.1.3.16]
  ko:K13248 PHOSPHO2; pyridoxal phosphate phosphatase PHOSPHO2 [EC:3.1.3.74]
  ko:K06124 PHOSPHO1; phosphoethanolamine/phosphocholine phosphatase [EC:3.1.3.75]

ko03016 Transfer RNA biogenesis (4)

  ko:K03538 POP4; ribonuclease P protein subunit POP4 [EC:3.1.26.5]
  ko:K14288 XPOT; exportin-T
  ko:K15437 AIMP1; aminoacyl tRNA synthase complex-interacting multifunctional protein 1
  ko:K03537 POP5; ribonuclease P/MRP protein subunit POP5 [EC:3.1.26.5]

ko04147 Exosome (4)

  ko:K07192 FLOT; flotillin
  ko:K13289 CTSA; cathepsin A (carboxypeptidase C) [EC:3.4.16.5]
  ko:K17292 TBCA; tubulin-specific chaperone A
  ko:K07890 RAB21; Ras-related protein Rab-21

ko03019 Messenger RNA biogenesis (3)

  ko:K12624 LSM5; U6 snRNA-associated Sm-like protein LSm5
  ko:K14398 CPSF6_7; cleavage and polyadenylation specificity factor subunit 6/7
  ko:K12621 LSM2; U6 snRNA-associated Sm-like protein LSm2

ko03036 Chromosome and associated proteins (3)

  ko:K07192 FLOT; flotillin
  ko:K11672 ACTR5; actin-related protein 5
  ko:K11864 BRCC3; BRCA1/BRCA2-containing complex subunit 3 [EC:3.4.19.-]

ko03009 Ribosome biogenesis (2)

  ko:K03538 POP4; ribonuclease P protein subunit POP4 [EC:3.1.26.5]
  ko:K03537 POP5; ribonuclease P/MRP protein subunit POP5 [EC:3.1.26.5]

ko01003 Glycosyltransferases (2)

  ko:K13692 IAGLU; UDP-glucose:(indol-3-yl)acetate beta-D-glucosyltransferase [EC:2.4.1.121]
  ko:K00750 GYG1; glycogenin [EC:2.4.1.186]

ko03000 Transcription factors (2)

  ko:K05527 bolA; BolA family transcriptional regulator, general stress-responsive regulator
  ko:K18485 MYF6; myogenic factor 6

ko04812 Cytoskeleton proteins (2)

  ko:K05747 WAS; Wiskott-Aldrich syndrome protein
  ko:K17292 TBCA; tubulin-specific chaperone A

ko01001 Protein kinases (1)

  ko:K13428 EFR; LRR receptor-like serine/threonine-protein kinase EFR [EC:2.7.11.1]

ko01006 Prenyltransferases (1)

  ko:K02548 menA; 1,4-dihydroxy-2-naphthoate polyprenyltransferase [EC:2.5.1.74]

ko04031 GTP-binding proteins (1)

  ko:K07890 RAB21; Ras-related protein Rab-21'''

resp = requests.post("http://localhost:5000/KeggNetApi",
                     json={"text": inText.strip()})

print(resp.json())