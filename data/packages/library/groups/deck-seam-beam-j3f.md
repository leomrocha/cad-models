THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# deck seam beam j3f

1. **Library number:** 23.
2. **Type:** group.
3. **CAD file:** [deck-seam-beam-j3f.dwg](<deck-seam-beam-j3f.dwg>).
4. **DWG SHA-256:** `f9fbbfee5c880f5bcfa2586381f0f453ef7754cb0e7c566cc3bc6d05b217005c`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: one welded beam assembly per deck.

### Parts and contact planes

1. **Base:** one P04JCBF —30×400×3 mm beam base, X±15,Y±200,Z764…767. Its end contact patchesY175…200 and−200…−175 meet the two ledge undersidesZ767.
2. **Crown:** one P04JCBC —30×350×3 mm beam crown, X±15,Y±175,Z767…770. Crown lower face contacts base upper faceZ767; plug weld through three base holes from below. Finish welds within the base lower planeZ764 and keep crown topZ770 planar. Panel contact bands areX−15…−1 and 1…15,14 mm wide each.
3. **Thread blocks:** two P04JMB —25×25×8 mm M8 backing blocks, centredX0,Y±187.5, extendingZ756…764; their upper faces meet base underside 764. Weld along their X-end contact edges, leaving beam/ledge top contacts intact.
4. **Retaining screws:** two C160 — proposed M8×20 countersunk screws, class 10.9, normalZ, heads at ledge top 770 and tips downward. Reuse source DIN74 TypeF bore/mouth and source head profile as recorded in the ledge input. The deck panels cover these heads during operation and are removed for screw access. The receiver blocks provide external-only release without loose lower nuts.

### Dimension and service checks

1. **Counterseat stack:**3 mm ledge+3 mm base=6 mm. Source nominal 90° seat with nominal diameters gives depth(18.25−9)/2=4.625 mm. With source mouth maximum 18.58, bore minimum 9 and project minimum angle 89°, ideal cone depth is 4.874339 mm. Nominal residual section below that cone is 6−4.874339=1.125661 mm. This is an ideal geometry calculation; actual head cone, transition and bearing contact control the supplied assembly. Inspect the supplied head top flush or recessed 0…1 mm belowZ770; this receiving interval is a project condition.
2. **Screw reach:** project receiving length interval 19.5…20.5 mm and proposed head recessionρ0…1 mm give nominal tipZ=770−ρ−L=748.5…750.5 mm. The 8 mm tapped blocks occupy 756…764 mm; actual full-form screw/thread overlap must be at least proposed 5 mm. Evaluate source head/thread transition, incomplete tip thread and tapped chamfers at that interval. The screw reaches through the 6 mm ledge/base stack and the 8 mm backing block, with its tip projecting 5.5…7.5 mm below the block. Source actual head diameter 15.24…16.43 mm and theoretical sharp cone 17.92 mm retain their distinct labels.
3. **Cable/shield spacing:** retained planning cable maximumZ761 and beam underside 764 give 3 mm vertical separation where their X/Y projections meet. BMW shield roof maximum 741.25 gives 22.75 mm to beam underside. Backing-block inner Y edge 175 gives 8 mm to the retained central cable-envelope edge 167; the source cable and terminal bends retain their installed transforms. AtX0, these end blocks are 180 mm longitudinally from lifting postsX±180 and 250 mm from deck postsX±250. They lie above the side-controller carrier top 668 by at least 88 mm. The source/proposed cabinet remains behindX−335, away from the seamX±15.
4. **Assembly:** weld the beam crown and two blocks, inspect surfaces and threads, fit beam under both ledges, and clamp it while machining the matched two-piece TypeF seats. Fit the two M8 screws from above before deck panels. After removing both panels, access source 5 mm hex sockets vertically from above through a proposedØ8 mm driver cylinder extending 40 mm upward. Release and withdraw both M8 screws. Apply the lowering-and-yaw sequence below before lifting the beam between the fixed ledges. Battery and shield restraints remain their own connections.


### Corrected service motion — lowering, yaw and lift proposal

1. **Recorded geometry conflict:** the base end patches lie under the fixed ledges at Z767 mm. Direct upward motion from the installed pose intersects those ledges. The crown also initially occupies the full gap between their inner faces Y±175 mm.
2. **Prepare the swept space:** remove both deck panels and the two beam-retaining M8 screws. Electrically isolate and disconnect the upper harnesses crossing the beam work zone at their service connections, release their supports and move them outside the proposed motion volume before lowering. The retained upper cable planning centre Z754 mm with radius 7 mm reaches Z761 mm; the lowered base reaches Z760.5 mm, so this crossing harness occupies the beam's lowered volume. Secure the displaced harnesses outside the motion volume during service. Battery restraint and shield supports retain their existing attachments.
3. **Lower:** support the beam, keep X/Y fixed and translate it 3.5 mm downward. Base becomes Z760.5…763.5 mm; crown Z763.5…766.5 mm; backing blocks Z752.5…760.5 mm. Crown top then has 767−766.5 = 0.5 mm nominal separation below the fixed ledge undersides. This is a proposed service clearance using the finished sheet/weld boundaries.
4. **Yaw:** rotate 40° about vertical axis (X,Y) = (0,0) at that lowered height. Let θ be yaw and use X′ = X cosθ − Y sinθ, Y′ = X sinθ + Y cosθ. The 30 × 400 mm base has final half-extents |X′| ≤ 15 cos40° + 200 sin40° = 140.0482 mm and |Y′| ≤ 15 sin40° + 200 cos40° = 162.8507 mm. It fits between the ledge inner faces Y±175 with 12.1493 mm nominal lateral clearance. The 30 × 350 mm crown has final |Y′| ≤143.6996 mm; the two 25 mm blocks have final |Y′| ≤161.2437 mm. All beam pieces therefore pass between those faces at the final yaw.
5. **Swept planning bounds:** during yaw 0…40°, every beam piece stays inside a vertical cylinder of radius √(200² + 15²) = 200.5617 mm about the origin, from Z752.5 to766.5 mm. Side lifting-tab inner Y218 gives at least 17.4383 mm plan separation from that cylinder. Deck caps start at |X|230 mm, giving at least 29.4383 mm plan separation. Lowest block Z752.5 gives 11.25 mm vertical separation above the retained BMW shield roof Z741.25. These checks cover the named retained planning shapes and the finished proposed weld envelope.
6. **Lift:** retain 40° yaw and lift vertically 60 mm through the now-clear ledge gap. Base underside reaches Z820.5 mm; lowest block reaches Z812.5 mm. Continue upward within the same clear Y band to remove the beam. Reinstall by reversing the yaw/lowering path, refit the two M8 screws, restore harness supports/connections, then refit the two deck panels. The bench/support fixture controls the beam during these manual service movements.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P04JCBF — Seam beam base | 1 | [Seam beam base](<../parts/mechanical/p04jcbf-j3f-deck-seam-beam-base.md>) — 119 | `0f0caf750c51ad56bf69cb62b1a11be7a5cef58932c4f154396623d74ff644cd` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JCBC — Seam beam crown | 1 | [Seam beam crown](<../parts/mechanical/p04jcbc-j3f-deck-seam-beam-crown.md>) — 118 | `15d35d0f4b29da4c468b6ffb56f3fbb5079b7316f6caeae007a95b9bdede70bb` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JMB — M8 nominal-thread backing block | 1 | [Seam beam M8 threaded block](<../parts/mechanical/p04jmb-j3f-seam-beam-m8-thread-block.md>) — 124 | `c22cdc9dd8bcc28ca8db6aaff2484a357196f7c46cd37c702b22c6a75505fc2b` | `{"position_mm":[0.0,-187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JMB — M8 nominal-thread backing block | 1 | [Seam beam M8 threaded block](<../parts/mechanical/p04jmb-j3f-seam-beam-m8-thread-block.md>) — 124 | `c22cdc9dd8bcc28ca8db6aaff2484a357196f7c46cd37c702b22c6a75505fc2b` | `{"position_mm":[0.0,187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. 08 parts and materials.
2. 08 parts and materials.
3. 08 parts and materials.
4. 08 parts and materials.
5. 08 parts and materials.
6. 08 parts and materials.
7. 08 parts and materials.
8. 08 parts and materials.
9. 08 parts and materials.
10. 08 parts and materials.
11. 08 parts and materials.
12. 08 parts and materials.
13. 08 parts and materials.
14. 08 parts and materials.
15. 08 parts and materials.
16. 08 parts and materials.
17. 08 parts and materials.
18. 08 parts and materials.
19. 08 parts and materials.
20. 08 parts and materials.
21. 08 parts and materials.
22. 08 parts and materials.
23. 08 parts and materials.
24. 08 parts and materials.
25. 08 parts and materials.
26. 08 parts and materials.
27. 08 parts and materials.
28. 08 parts and materials.
29. 08 parts and materials.
30. 08 parts and materials.
31. 08 parts and materials.
32. 08 parts and materials.
33. 08 parts and materials.
34. 08 parts and materials.
35. 08 parts and materials.
36. 08 parts and materials.
37. 08 parts and materials.
38. 08 parts and materials.
39. 08 parts and materials.
40. official manufacturer PDF.
41. sumitomo exact interfaces.
42. Exact manufacturer data sheet.
43. manufacturer data sheet.
44. manufacturer data sheet.
45. WISKA mounting instruction.
46. Kelly KLS-N wiring diagram, §3.2.2, p.14.
47. Southco Polished Series catalogue, printed pages 249–250.
48. DIN EN ISO 10642:2020-02 / EN ISO 10642:2019.
49. DIN Handbook 193 preview containing DIN 74:2003-04.
50. Böllhoff DIN 7991 steel 10.9 datasheet.
51. Supplier catalog: DIN 7991 class 12.9.
52. ASME B18.3-2012, Globalso copy.
53. ASME B18.2.1-2010, Tables 5–6.
54. supplier Grade 5 product sheet.
55. ASME B18.3-2012, Finesz copy.
56. ASME B18.21.1-2009, Table 12 and material requirements.
57. ISO 6410-1:1993, metric thread designation.
58. Tyro Gemini 1S technical specification PDF.

## References — local

118. [Seam beam crown](<../parts/mechanical/p04jcbc-j3f-deck-seam-beam-crown.md>) — library entry 118.
119. [Seam beam base](<../parts/mechanical/p04jcbf-j3f-deck-seam-beam-base.md>) — library entry 119.
124. [Seam beam M8 threaded block](<../parts/mechanical/p04jmb-j3f-seam-beam-m8-thread-block.md>) — library entry 124.

## Views

1. [deck seam beam j3f isometric](<../images/deck-seam-beam-j3f-isometric.png>).
