# Deck access, left drive and one drilled-foot clamp joint

Validation assembly; tractor design status remains a discussion proposal. [Native DWG](<service-access-joint.dwg>). Units are mm. In tractor coordinates X is forward, Y left and Z up.

## Recorded occurrences

Each directly installed occurrence has its own persistent identity. Definition IDs identify reusable geometry. The assembly keeps the actual source revision and placement recorded for each member.

| Occurrence | Definition | Readable label | Native layer |
| --- | --- | --- | --- |
| service-access-joint.fixed.1 | fixed-receiver-rails | fixed receiver rails | NAV-FIXED |
| service-access-joint.access.1 | removable-deck-access | removable deck access | NAV-ACCESS |
| service-access-joint.drive.1 | left-drive-cartridge | left drive cartridge | NAV-DRIVE |
| service-access-joint.structure.1 | library-24 | Four deck side supports | NAV-STRUCTURE |
| service-access-joint.structure.2 | library-26 | Raised frame core with foot passages | NAV-STRUCTURE |
| service-access-joint.structure.3 | library-117 | P03JIN — Left fixed motor backbone | NAV-STRUCTURE |
| service-access-joint.joint.1 | library-74 | C142 — M10×70 screw nominal reference | NAV-JOINT |
| service-access-joint.washer.1 | plain-washer-10p5-20-2 | C148 — Inboard M10 washer nominal reference | NAV-WASHER |
| service-access-joint.joint.2 | library-121 | P04JCT34 — M10 rail compression sleeve | NAV-JOINT |
| service-access-joint.washer.2 | plain-washer-10p5-20-2 | C148 — Outboard M10 washer nominal reference | NAV-WASHER |
| service-access-joint.joint.3 | library-79 | C154 — M10 nut nominal reference | NAV-JOINT |

Original positions, normals, rotations, source hashes and locators. Reopened model observations.

This layout uses the foot-passage rail revision and a single documented M10 joint. Its two public plain-washer instances represent nominal geometry only. The private records bind the mounting location, application and source revision. Nested selection and washer world frames. [Four role-coloured views](<service-access-layer-sheet.png>).

DWG SHA-256: `b162eff34695ddb5ffa16dc30f97c790b0e0dea98f8bd3c0d57840a8750b13b1`.
