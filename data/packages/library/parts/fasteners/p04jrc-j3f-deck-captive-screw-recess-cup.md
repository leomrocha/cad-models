THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Recessed captive deck cup

1. **Library number:** 126.
2. **Type:** part.
3. **CAD file:** [p04jrc-j3f-deck-captive-screw-recess-cup.dwg](<p04jrc-j3f-deck-captive-screw-recess-cup.dwg>).
4. **DWG SHA-256:** `7037880b79b8f9143cdfb944aa15a7aa1aa4af01d785dd4eb978f1fdb0618297`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Recessed captive deck cup — P04JRC.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion turned-part proposal. Units: mm. Quantity: four per panel, eight per deck.
1. **Proposed steel geometry:** flangeØ22 mm fromZ770…773; lower bodyØ18 mm fromZ759…770. The coaxial upper pocket isØ14 mm fromZ762…773, leaving 3 mm mounting floorZ759…762. The floor outer/source shoulder face isZ762; floor inner/mating face isZ759. The flange underside 770 contacts the matching ledge top 770 over the annular band between ledge-hole radius 9.5 and flange radius 11, width 1.5 mm. Bore/body wall thickness is(18−14)/2=2 mm. The flange joins the matchingØ22 parent-panel aperture with finished top 773.
2. **Exact source installation:** C118/C119 Southco source record, printed page 250: panel 2.9…3.3 mm, source boreØ6.5 +0.08/−0 mm. Machine the 82° flare countersink 0.76 mm deep from the INNER floor faceZ759 towardZ759.76. Source standoff body/shoulder faces outward into the cup pocket, aboveZ762; form its nose into that inner-face countersink using the prescribed source tools. Source P3.2 mm describes the pre-flare nose reference. Actual finished flare profile sets the lower standoff endpoint.
3. **Template section:** nominal countersink mouth 6.5+2×0.76×tan 41°=7.821316 mm; using bore upper 6.58 gives 7.901316 mm. Minimum nominal radial floor material from that mouth to pocket radius 7 is 7−7.901316/2=3.049342 mm. Remaining straight axial section after the 0.76 mm flare seat is 2.24 mm. Source reference standoff diameter calloutsØ6.3/Ø7.5 and headØ7.1 before knurl fit the nominal pocket screen; supplied profile is checked againstØ14.
4. **Bench process and tool access:** turn/drill/countersink the cup, weld it to the plate, then install the Southco standoff and screw with source tools. Source backup-tool main bodyØ12.7 fits theØ14 pocket with 0.65 mm nominal radial space. Source flaring punch and backup tool are separately identified in the source record. Form the standoff before fitting the panel to the fixed receiver so the inner-face punch has axial access. A proposed service slotted driver uses blade width≤5 mm and thickness≤0.7 mm, with the source 0.76 mm slot and actual supplied head. Reserve aØ12.7 mm axial tool cylinder from the source head seat upward through the pocket.
5. **Actual assembly criteria:** closed source head projection from floor outer face is nominal 10.3 mm; maximum permitted actual projection 11 mm keeps it at/below deck top 773. Fixed receiver passageØ19 surrounds theØ18 lower body with 0.5 mm nominal radial clearance. Its floor 758.5 lies 0.5 mm below cup inner face 759. Inspect actual flare/body clearance against the proposed 0.2 mm minimum in P04JPNR — assembly.

1. **Proposed steel geometry:** flangeØ22 mm fromZ770…773; lower bodyØ18 mm fromZ759…770. The coaxial upper pocket isØ14 mm fromZ762…773, leaving 3 mm mounting floorZ759…762. The floor outer/source shoulder face isZ762; floor inner/mating face isZ759. The flange underside 770 contacts the matching ledge top 770 over the annular band between ledge-hole radius 9.5 and flange radius 11, width 1.5 mm. Bore/body wall thickness is(18−14)/2=2 mm. The flange joins the matchingØ22 parent-panel aperture with finished top 773.
2. **Exact source installation:** C118/C119 Southco source record, printed page 250: panel 2.9…3.3 mm, source boreØ6.5 +0.08/−0 mm. Machine the 82° flare countersink 0.76 mm deep from the INNER floor faceZ759 towardZ759.76. Source standoff body/shoulder faces outward into the cup pocket, aboveZ762; form its nose into that inner-face countersink using the prescribed source tools. Source P3.2 mm describes the pre-flare nose reference. Actual finished flare profile sets the lower standoff endpoint.
3. **Template section:** nominal countersink mouth 6.5+2×0.76×tan 41°=7.821316 mm; using bore upper 6.58 gives 7.901316 mm. Minimum nominal radial floor material from that mouth to pocket radius 7 is 7−7.901316/2=3.049342 mm. Remaining straight axial section after the 0.76 mm flare seat is 2.24 mm. Source reference standoff diameter calloutsØ6.3/Ø7.5 and headØ7.1 before knurl fit the nominal pocket screen; supplied profile is checked againstØ14.
4. **Bench process and tool access:** turn/drill/countersink the cup, weld it to the plate, then install the Southco standoff and screw with source tools. Source backup-tool main bodyØ12.7 fits theØ14 pocket with 0.65 mm nominal radial space. Source flaring punch and backup tool are separately identified in the source record. Form the standoff before fitting the panel to the fixed receiver so the inner-face punch has axial access. A proposed service slotted driver uses blade width≤5 mm and thickness≤0.7 mm, with the source 0.76 mm slot and actual supplied head. Reserve aØ12.7 mm axial tool cylinder from the source head seat upward through the pocket.
5. **Actual assembly criteria:** closed source head projection from floor outer face is nominal 10.3 mm; maximum permitted actual projection 11 mm keeps it at/below deck top 773. Fixed receiver passageØ19 surrounds theØ18 lower body with 0.5 mm nominal radial clearance. Its floor 758.5 lies 0.5 mm below cup inner face 759. Inspect actual flare/body clearance against the proposed 0.2 mm minimum in P04JPNR — assembly.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed source-profile cup | PASS | [1, 1, 1, 1] | count |
| Source cup cylinder 6.5 mm | PASS | [[0.0, 4.6659043047514155e-14]] | mm |
| Source cup cylinder 14 mm | PASS | [[0.0, 4.7332598787045204e-14]] | mm |
| Source cup cylinder 18 mm | PASS | [[0.0, 4.647534602764205e-14]] | mm |
| Source cup cylinder 22 mm | PASS | [[0.0, 4.71489017671731e-14]] | mm |
| Cup floor/flange axial planes | PASS | [759.0, 762.0, 770.0, 773.0] | mm |
| Source flare cone half-angle | PASS | [41.00000000000035] | degrees |

## Sources — online

1. Southco Polished Series catalogue, printed pages 249–250.
2. Weldable steel plate stock family — supplier reference.
