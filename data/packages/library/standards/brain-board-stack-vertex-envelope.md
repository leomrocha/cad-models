# Brain board stack vertex envelope

1. **Library number:** 317.
2. **Plan use:** Brain enclosure fit reference for Assembly 4.
3. **Native drawing:** [Brain board stack vertex envelope](<brain-board-stack-vertex-envelope.dwg>).
4. **DWG SHA-256:** `4f86e05c27fec6f0517a09584857f745858e9dacefe99730ec07b8b2493be8c8`.
5. **Actual execution model:** unavailable.

## Technical specification

1. The solid bounds the recorded model vertices of two Avaota-A1 computers, two SparkFun NEO-F9P receivers, one LEVIA-H7 board and the planar ORP mounting face in the saved layout. The reference uses Brain assembly XYZ coordinates in millimetres.
2. Verified spans are **106.191200 × 99.999800 × 63.669978 mm**. The opposite corners are (−0.732800, 0.000100, −10.000000) mm and (105.458400, 99.999900, 53.669978) mm. The receivers set the X extents, the ORP face sets both Y extents and the bottom, and LEVIA-H7 sets the top.
3. The calculation uses reachable solid vertices and mesh vertices. Assembly check scope contains the five boards and the zero-thickness plate face. The antennas and switch are external references. Allowances for case hardware, installation, and additional components belong to the enclosure fit check.
4. The source Brain layout matches DWG SHA-256 `a3e174ab293d61fd81580ed1701b708320e9a28550ddfb44bca14a7cd3afbd7f`.

## Checks

1. Verified all eight corner positions, six planar faces and reciprocal closed topology. The maximum vertex-set distance was 7.11e-15 mm.
2. Incremental and final verified SAVE, [isometric view](<../images/brain-board-stack-vertex-envelope-isometric.png>) and guarded closure passed.

## Sources — online

1. Sowbot Brain hardware.

## References

1. [ORP 28-opening mounting face](<../parts/mechanical/brain-orp-mounting-plate-28-opening-source-face.md>).
2. [Avaota-A1 board and connectors](<../subassemblies/avaota-a1-v17-board-source-connectors.md>).
3. [LEVIA-H7 board](<../parts/electrical/levia-h7-board-exterior-stage.md>).
4. [SparkFun NEO-F9P board and connectors](<../subassemblies/sparkfun-neo-f9p-source-connector-exterior-stage.md>).
