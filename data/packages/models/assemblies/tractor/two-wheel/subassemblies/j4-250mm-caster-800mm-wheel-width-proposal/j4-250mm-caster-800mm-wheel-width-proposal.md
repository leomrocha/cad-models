# J4 250 mm caster chassis with 800 mm wheel-width proposal

**Catalogue draft ID** `j4-250mm-caster-800mm-wheel-width-proposal`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](j4-250mm-caster-800mm-wheel-width-proposal.dwg), SHA-256 `89af18f768b2688d1be4eac93f32159a444cacb4f4d2b6b1c6feef33e687417b`.

## Geometry

J4 chassis with 250 mm caster, H390 tow-ball terminal and the 800 mm wheel-width proposal.

Millimetres. X forward, Y left and Z up. Width-target chassis proposal.

The two upper-limit tyre envelopes span 800 mm. The rim seats lie at Y = ±286.78 mm.
The closest sampled guard fastener head is 0.76 mm from each tyre envelope.

## Revision provenance

1. **Historical base** J4 250 mm caster with Category 1 supports and H390 terminal. Catalogue ID `j4-kelly-bmw-250mm-caster-with-category-1-and-h390-terminal`, revision 1, commit `5fd773c7cb6e986e10115be787921b752e037050`, DWG SHA-256 `137509080768049ca0aeed7f559e9d27389f65b3e79455483849e641681296c6`.
2. **Historical files** Run the following in the CAD Models checkout. Companion `git show 5fd773c7cb6e986e10115be787921b752e037050:data/packages/models/assemblies/tractor/two-wheel/subassemblies/j4-kelly-bmw-250mm-caster-with-category-1-and-h390-terminal/j4-kelly-bmw-250mm-caster-with-category-1-and-h390-terminal.md`. DWG `git show 5fd773c7cb6e986e10115be787921b752e037050:data/packages/models/assemblies/tractor/two-wheel/subassemblies/j4-kelly-bmw-250mm-caster-with-category-1-and-h390-terminal/j4-kelly-bmw-250mm-caster-with-category-1-and-h390-terminal.dwg`.
3. **Geometry change** The width-target assembly replaced 18 wheel-end occurrences in this base and added two tyre-clearance cylinders.

## Model references

These packages identify the surviving component sources through the saved historical chassis chain. The reference role identifies a source study with subsequent placement or geometry changes.

1. [J4 captive chain guards and rails with top-mounted rear feet](../j4-top-mounted-deck-rails-and-captive-guards/j4-top-mounted-deck-rails-and-captive-guards.md), reference, catalogue revision 1, SHA-256 `e8a7690da5a47d2c5818c5747dfbe9baa2f363404a7e73017b8c6daa13fdf6fa`. Source guard bodies and captive guard hardware. Later rail replacements are recorded separately.
2. [J4 rear crossmember for inboard caster root plates](../../../../../mechanical/chassis/crossmembers/p02j4r-j4-short-rear-crossmember-248mm/p02j4r-j4-short-rear-crossmember-248mm.md), embedded, catalogue revision 1, SHA-256 `8590028336da6d49cde85b17d033c982045a741ccd965d75301417d45c90b872`. P02 — Rear crossmember.
3. [Main frame crossmember](../../../../../mechanical-parts/components/p02-main-frame-crossmember-reference/p02-main-frame-crossmember-reference.md), embedded, catalogue revision field empty, SHA-256 `f2cd4fdf0b6f1c7b2ddc58fbbe1f9680c92ecac4fee7365acececf92c55104c2`. P02 — Middle crossmember.
4. [J front narrow crossmember](../../../../../mechanical-parts/components/p02jf-j-front-narrow-crossmember/p02jf-j-front-narrow-crossmember.md), embedded, catalogue revision field empty, SHA-256 `cb2075536d1391cbae7ffd5a4b1cd9ac47f711adad08933f1a2d14a025140e0e`. P02JF — Narrow front crossmember.
5. [J4 left 30 mm wheel stack with keyed sprocket hub blank](../j4-30mm-left-wheel-stack-with-keyed-sprocket-hub/j4-30mm-left-wheel-stack-with-keyed-sprocket-hub.md), reference, catalogue revision 1, SHA-256 `270b280fbfc44d96ea566c44374c452e721a77a10d30dae7a820354ebd117553`. Source of left brake and sprocket side hardware. Final wheel-end replacements use the width-target package.
6. [J4 right 30 mm wheel stack with keyed sprocket hub blank](../j4-30mm-right-wheel-stack-with-keyed-sprocket-hub/j4-30mm-right-wheel-stack-with-keyed-sprocket-hub.md), reference, catalogue revision 1, SHA-256 `9a3d6fc6ec65914ca99fe1b22d90b73f2695456045f5d66243ec6b6018301845`. Source of right brake and sprocket side hardware. Final wheel-end replacements use the width-target package.
7. [J4 30 mm shifted left hanger assembly with J04 fasteners](../j4-30-bearing-hangers-with-shifted-left-post-j04-stack/j4-30-bearing-hangers-with-shifted-left-post-j04-stack.md), embedded, catalogue revision 1, SHA-256 `7657e9f60b799aa127e9e28f45686f95f434329f30eb89a9a84366aec9568d6d`. Installed bearing hangers with fasteners.
8. [J4 relieved left motor backbone](../../../../../mechanical/chassis/motor-mounts/p03jin-j4-relieved-left-motor-backbone/p03jin-j4-relieved-left-motor-backbone.md), embedded, catalogue revision 1, SHA-256 `6afcdb83ffb199d9864e1997086ccf0601e5bc3cc9929081c103222e840ac059`. Left fixed motor backbone.
9. [J4 relieved right motor backbone](../../../../../mechanical/chassis/motor-mounts/p03jbr-j4-relieved-right-motor-backbone/p03jbr-j4-relieved-right-motor-backbone.md), embedded, catalogue revision 1, SHA-256 `faab7e6913a007675f6f5f55632d888b8f2bd9b3b1f2c41e73d7159e2d364ab0`. Right fixed motor backbone.
10. [J4 Motenergy ME0907 moving plate with lower-edge relief](../../../../../mechanical/chassis/motor-mounts/p11-j4-me0907-moving-motor-plate-lower-relief/p11-j4-me0907-moving-motor-plate-lower-relief.md), embedded, catalogue revision 1, SHA-256 `1f0195d6d17b927ed5fa3713f1523a24c7f7015233cb485b309c89994cf92384`. Left moving motor plate; Right moving motor plate.
11. [Motenergy ME0907 motor](../../../../../electronics/components/motenergy-me0907-mechanical-reference/motenergy-me0907-mechanical-reference.md), embedded, catalogue revision field empty, SHA-256 `6c9c1505c3beb528b10cb27c5a2af0406c16e00a2f766cfaa27bed8c132d1a33`. Left Motenergy ME0907 motor; Right Motenergy ME0907 motor.
12. [J4 250 mm caster with 60 mm rearward head](../j4-caster-250-60mm-rearward-head-installation/j4-caster-250-60mm-rearward-head-installation.md), embedded, catalogue revision 1, SHA-256 `5048e2eddffc0c249b2edb53d8ec8ba39b7bac3980fad3e8d578167f53d97f08`. Caster and stepped bridge.
13. [J4 H390 hitch tube frame for 250 mm caster](../j4-h390-hitch-frame-for-250mm-caster/j4-h390-hitch-frame-for-250mm-caster.md), embedded, catalogue revision 1, SHA-256 `ab689b4183388140906725a57063d8353b6340b68ec8b382aa61c04bc438cff6`. H390 hitch tube frame.
14. [J4 left 520 chain route envelope](../../../../../mechanical/drivetrain/clearance/j4-left-520-chain-route-envelope/j4-left-520-chain-route-envelope.md), embedded, catalogue revision 1, SHA-256 `12a5bc2def72aa3edc1e636cfc4e6958e150271fd8fcee6e33ad0c245c404784`. Left chain planning space.
15. [J4 right 520 chain route envelope](../../../../../mechanical/drivetrain/clearance/j4-right-520-chain-route-envelope/j4-right-520-chain-route-envelope.md), embedded, catalogue revision 1, SHA-256 `4659f03e25d3bb125654509729ba7231a621de8b7b999dbb9b1b1072c6a3abaa`. Right chain planning space.
16. [J4 recessed deck with front fasteners for rear top-mounted feet](../j4-recessed-deck-for-rear-top-feet/j4-recessed-deck-for-rear-top-feet.md), reference, catalogue revision 1, SHA-256 `e4bd8404029b3bbdcace384bcfa37b82046c8c669872d884e7fbd1baa8217719`. Recessed deck source. The right deck ledge was replaced by the detachable assembly.
17. [BMW i3 raised J tray with upper threaded bridges and shield](../bmw-i3-raised-j-tray-with-b01-threaded-bridges/bmw-i3-raised-j-tray-with-b01-threaded-bridges.md), embedded, catalogue revision 1, SHA-256 `77d5fe79cf7599605e23d8668bf67ef6263da5f1a402b053eff8ad0ac8156246`. BMW raised tray and supports.
18. [J3f negative-Y detachable deck ledge and two cap joints](../j3f-negative-y-detachable-deck-ledge-and-cap-joints/j3f-negative-y-detachable-deck-ledge-and-cap-joints.md), embedded, catalogue revision 1, SHA-256 `412f79109647f15a603478452b8b0332e12e17eb3f4f550b8a3cb3e70a0c8c5c`. Detachable ledge joints.
19. [J4 Kelly controller carriers on guarded rails](../j4-kelly-carrier-and-guard-rail-installation/j4-kelly-carrier-and-guard-rail-installation.md), reference, catalogue revision 1, SHA-256 `626b06fff3fa01af2cf3e9261ba94526800cd2449eae643cada535efcbbdff4f`. Kelly carrier and guard rail installation source. The Gemini installation replaces the left rail.
20. [Fibox R2 cabinet and Pilz PNOZ X3 packaging layout](../fibox-r2-pilz-pnoz-x3-relay-packaging-layout/fibox-r2-pilz-pnoz-x3-relay-packaging-layout.md), reference, catalogue revision 1, SHA-256 `54399f8fd33e7233e6314e90b9d89bff619708b6f236c1f5201f0d8309543b93`. Fibox cabinet, Pilz relay envelope and transverse mount source. The installation translates the package rearward by 45 mm.
21. [J4 raised Gemini 1S receiver mount on the left rail](../j4-raised-gemini-receiver-rail-and-cradle/j4-raised-gemini-receiver-rail-and-cradle.md), embedded, catalogue revision 1, SHA-256 `65d2ce041d03e40eb2299279acd79e4ea94c14f071e24bfdfd8fb24b686da0af`. J4 Gemini receiver mount and left rail.
22. [J4 outboard splash panels with detachable left beam](../p24j4-outboard-splash-with-detachable-beam/p24j4-outboard-splash-with-detachable-beam.md), embedded, catalogue revision 1, SHA-256 `12494b7cc2cf170d91fcc7d2bce42d3978b74822649ed455d47317b6b8997dcb`. Outboard splash assembly.
23. [J4 Category 1 front attachment support](../j4-front-category-1-attachment-support/j4-front-category-1-attachment-support.md), embedded, catalogue revision 1, SHA-256 `b7174503de56cfa099e65f61d607594cad98e3acabe7f77dd19d024e85a09aed`. Front Category 1 support.
24. [J4 Category 1 rear attachment support](../j4-rear-category-1-attachment-support/j4-rear-category-1-attachment-support.md), embedded, catalogue revision 1, SHA-256 `eb7a834ec82fdbad059b6917d30853f0c983388524e748b02dcfb37084716179`. Rear Category 1 support.
25. [J4 280 mm terminal longitudinal carrier tube](../../../../../mechanical/chassis/hitch/p07jtc280-j4-terminal-longitudinal-carrier/p07jtc280-j4-terminal-longitudinal-carrier.md), embedded, catalogue revision 1, SHA-256 `05fac236bd2ee1bb8952181c59e3fb2ac01d35f402876f9663a5c46b8f45c5e7`. Left longitudinal carrier; Right longitudinal carrier.
26. [J4 160 mm terminal transverse carrier tube](../../../../../mechanical/chassis/hitch/p07jtc160-j4-terminal-transverse-carrier/p07jtc160-j4-terminal-transverse-carrier.md), embedded, catalogue revision 1, SHA-256 `2c21fbcd46a151e2c3326034f586a3535097076c29877fab007533729bf06c5e`. Rear transverse carrier.
27. [J4 SM453 terminal plate](../../../../../mechanical/chassis/hitch/p07tp-j4-sm453-rounded-slot-terminal-plate/p07tp-j4-sm453-rounded-slot-terminal-plate.md), embedded, catalogue revision 1, SHA-256 `129401734961e00bc03373e323c517b571765a70c5d0437a2a328fde5716f0c0`. Terminal plate.
28. [J4 20 mm terminal drop web](../../../../../mechanical/chassis/hitch/p07jdw-j4-20mm-terminal-drop-web/p07jdw-j4-20mm-terminal-drop-web.md), embedded, catalogue revision 1, SHA-256 `75dbbefe5f2ec496025c93c8588f2b2c3a5258e250087e5a0af4e2be4cdfcaaf`. Left terminal drop web; Right terminal drop web.
29. [SM453 50 mm tow ball body](../../../../../mechanical/chassis/hitch/c025-sm453-50-mm-tow-ball/c025-sm453-50-mm-tow-ball.md), embedded, catalogue revision 1, SHA-256 `5d6feef99480a13f5bddb07d502d524947a5aea6ddfe9ce0ba3a68dfd3fd7dba`. SM453 bare ball.
30. [J4 width-target paired wheel stacks and tyre references](../j4-800mm-wheel-stack-and-clearance-layout/j4-800mm-wheel-stack-and-clearance-layout.md), embedded, catalogue revision 1, SHA-256 `b56564ae6821359b596c85d2429a909763f4eb8ee215a5f5e6cf4fcee7f9fe07`. Width-target wheel hardware and clearance.

## Checks

OpenCADStudio verified the reference geometry at revision 74708. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [OpenCADStudio · Isometric](j4-250mm-caster-800mm-wheel-width-proposal-ocs-isometric.png)
- [Plan](j4-250mm-caster-800mm-wheel-width-proposal-XY.png)
- [Elevation](j4-250mm-caster-800mm-wheel-width-proposal-XZ.png)
- [End](j4-250mm-caster-800mm-wheel-width-proposal-YZ.png)
- [Isometric](j4-250mm-caster-800mm-wheel-width-proposal-top-isometric.png)
