THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Notched trimmed splash panel

1. **Library number:** 197.
2. **Type:** part.
3. **CAD file:** [p24jpt-j-trimmed-splash-panel.dwg](<p24jpt-j-trimmed-splash-panel.dwg>).
4. **DWG SHA-256:** `0c97a5e25b84a29b8ce0ef0e730fe75e5abd8582d1fd3e56ae4a2de652d3c728`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Notched trimmed splash panel — P24JPT.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm.

### Panel and fixing constructor

1. **Manufactured plate proposal:** flat steel sheet, thickness 1.5 mm; X = −237.1…237.1, Z = 550…750; left Y = 173.5…175. Mirror Y for the right panel. Quantity: two plates per pair. Preserve P24JP — original 480 mm splash panel as the separate 480 mm comparison shape.
2. **Six retained fixing axes per panel:** Ø6.5 mm through holes normal Y at X = −220, 0, +220 and Z = 570, 730. Minimum X edge ligament at outer holes is 237.1−220−3.25 = 13.85 mm. The source maximum Ø12 mm C146 washer ends at |X|226, leaving 11.1 mm to the sheet end. Lower-row joint S04B and upper split crossbar axes retain their existing poses in P24JP — original 480 mm splash panel.
3. **Edge treatment proposal:** use the four cut shapes below. Finish exposed steel edge segments and exposed corners with a proposed C0.2 mm edge break, while preserving the 1.5 mm grip thickness. The run stops leave the support-contact regions accessible. The trim is segmented at these contact regions.
4. **Top cuts:** one P24TTC — 338 mm central top cut per panel, X −169…169, and two P24TTO — 46.1 mm outer top cuts, X −237.1…−191 and 191…237.1, all at Z 750. The full-length comparison is recorded in the named-space checks below.
5. **Bottom cuts:** two P24TB — 132.5 mm bottom edge-protector cuts per panel, X = −149…−16.5 and 16.5…149 at Z = 550.
6. **Side cuts:** two P24TS — 135 mm side edge-protector cuts per panel, Z = 584…719 at X = −237.1 and +237.1. All cut ends are square. The top and side runs have separate endpoints; the exposed corner/connection-edge segments receive the stated edge break.

### Stair-bridge clearance cuts — corner-open proposal

1. **Proposed corner-open cuts:** remove the sheet through its full 1.5 mm thickness over X −237.1…−204 and X 204…237.1, Z 550…555.5. Remove the central open-bottom notch X −16…16 over the same Z interval. Proposed internal corner radius at most 0.25 mm. This P24JPT cut shape pairs with P24JSHS — stair support. The retained P24JP plate supplies the original straight-bottom comparison.
2. **Corner-strip comparison:** an outer closed notch Xc±16 centred at |Xc|220 would leave 237.1−236=1.1 mm of sheet to the side edge below Z 555.5. The corner-open proposal extends those outer cuts to the panel ends. Its two retained bottom-edge runs occupy X −204…−16 and X 16…204 at Z 550; the outer side edges begin at Z 555.5.
3. **Bridge and weld spacing:** bridge material spans Xc±15,Z 552…555, with proposed X end weld bounds Xc±15.5. Each retained vertical notch/corner-cut face at |X|16/204 lies 0.5 mm beyond the nearest weld bound, and notch/corner top 555.5 lies 0.5 mm above weld maximum 555. The maximum proposed 0.25 mm internal corner radius fits inside that 0.5 mm reserve. Sheet contact with support face Y 175 starts above 555.5.
4. **Fixing and trim lands:** lower Ø6.5 mm holes at Z 570 have 570−555.5−3.25=11.25 mm material ligament above these cuts. Source washer lower edge 564 is 8.5 mm above the cuts. Bottom trim inner nominal endpoints |X|16.5 lie 0.5 mm into retained edge relative to central cut faces 16; their 0.5 mm axial end treatment reaches those faces. Outer nominal endpoints |X|149 and end treatment 149.5 leave 0.5 mm to lifting-foot inner faces 150. Nearest central stair weld remains 0.5 mm beyond the trim end-treatment bound. Side trim begins at 584,28.5 mm above the changed outer side-edge start 555.5.

### Source section and assumed placement

1. C114 — EMKA 1010-12 source section gives source outside width 8.3 mm, overall height 11.5 mm, crown wall 2.4 mm and grip range 0.8–2.5 mm. The proposed 1.5 mm sheet lies within that grip range.
2. **Project placement assumptions:** centre the sheet thickness across the section outside width and seat its edge against the inside crown. The resulting projection beyond each sheet face is (8.3−1.5)/2 = 3.4 mm. The leg overlap along each sheet face is 11.5−2.4 = 9.1 mm. Section bounding boxes below follow these two assumptions; the retained drawing supplies the rounded section itself.
3. **Per-pair cut quantity:** two central top cuts, four outer top cuts, four bottom cuts and four side cuts, fourteen cuts total. Net uncoated source-profile length is 2×(338+2×46.1+2×132.5+2×135) = 1930.4 mm. Cut-process allowance is a separate fabrication input.

### Named occupied-space checks

1. **Deck posts:** side-run crown outer bounds are X = ±239.5 mm, leaving 0.5 mm to post inner faces |X|240. Top-cut axial end treatment reaches |X|237.6, leaving 2.4 mm to those post faces. These compare different section directions: crown projection in X for side runs and axial end treatment in X for the top run.
2. **Upper crossbars and washer row:** top-run legs end at Z 740.9, giving 0.9 mm above crossbar top 740. Upper-row washer maximum Z 736 leaves 4.9 mm to that leg-end boundary. Side-run end treatment occupies Z 583.5…719.5, leaving 0.5 mm below upper crossbar bottom 720 and 0.5 mm above lower-support top 583.
3. **Lower brackets and washer row:** bottom-run end treatment ends at X = −149.5…−16 and 16…149.5. With lower-bracket centres −220/0/+220, width 30 and proposed X weld projection at most 0.5, the nearest trim end has a 0.5 mm gap. Bottom trim maximum Z 559.1 leaves 4.9 mm to the lower washer minimum Z 564. Side trim inner X boundary |X|228 leaves 2 mm to outer washer |X|226.
4. **Lifting supports:** stanchions and upper arms start at Y 175 but their upper arm/root occupied regions begin Z 697 and extend outboard from Y 195. Side trims lie at |X|228…239.5, separated from lift-post outer |X|190 and root outer |X|210. Top central trim end treatment reaches|X|169.5 and outer trim end treatment begins|X|190.5, each giving 0.5 mm to lifting-stanchion faces|X|170/190. Exposed top-edge spans around those stanchions receive the proposed C0.2 mm finish. Top trim is above crossbar 740 by the stated 0.9 mm; lifting-tab occupied Y 218…226 is 39.6 mm beyond trim maximum Y 178.4. Deck cap bottom Z 764 leaves 11.6 mm above top-trim maximum Z 752.4.
5. **Cable comparison:** retained reference AL = (−40,185,754), assumed cable OD 14 mm, gives distance sqrt((185−178.4)^2+(754−752.4)^2) = 6.791171 mm from cable centre to the nearest top-trim bounding-box corner. Against radius 7 this gives 0.208829 mm bounding-box overlap. The rounded source section controls the actual surface comparison.
6. **Separate cable-crossing proposal:** AL_trim = (−40,187,754), mirrored AR_trim. Its assumed OD 14 mm cable bounding box has inner Y 180, giving 1.6 mm to trim outer Y 178.4. Circle-to-box distance is sqrt(8.6^2+1.6^2)−7 = 1.747571 mm. Keep the J3f physical installation and existing cable bypass route SL→EL(−280,160,754)→OL(−280,210,754)→DL(−280,210,680)→QL(−30,210,680)→CL(−30,187,680) and its Y mirror as their retained route. AL_trim identifies a separate local crossing option; connecting bends and terminal routes retain their component-specific shapes.
7. **Check scope:** calculated sheet holes, conservative section bounds, end-treatment envelopes and the named retained rectangular supports/straight cable section. Source-profile corner curves, stock tolerances, weld shape and actual cable bend sweeps enter the corresponding detailed occupied shapes.

### Full-length top-trim construction finding

1. A 474.2 mm full-length top run with end treatment has conservative bounds X −237.6…237.6,Y 170.1…178.4,Z 740.9…752.4. Lifting stanchions occupy X −190…−170 /170…190,Y 175…195,Z 548…747. Each bounding-box intersection is 20 mm in X,3.4 mm in Y and 6.1 mm in Z. The seven-run construction above uses the three separately cut top runs around these stanchions.

2. **Earlier bottom-run finding:** the 187 mm runs crossed lifting feet |X|150…210,Y 170…195,Z 540…548; their crown bound Z 547.6 gave 0.4 mm vertical box overlap. The 132.5 mm runs above end at|X|149.5 including axial treatment,0.5 mm inboard of those feet. The other bottom-edge segments receive the proposed C0.2 mm finish.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Notched trimmed splash panel | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-237.1, 237.1], [173.50000000000003, 175.00000000000006], [550.0, 750.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-220.0, 570.0], [-220.0, 730.0], [0.0, 570.0], [0.0, 730.0], [220.0, 570.0], [220.0, 730.0]] | mm |
| Specified notch boundary vertices | PASS | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] | count |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
