# Rear Category 1 working lift

1. **Native CAD, revision 2.** [DWG 2018](j4-rear-category1-working-lift.dwg). SHA-256 `29cbef6115dd23e0881fc3786672003eb8ed2a7826ead6b33c7793f722dd7ee4`.
2. **Working configuration.** The cassette carries rounded lower-arm roots, spherical tool joints, both lift actuators and stabilizers, and direct mechanical stops. The saved pose sets the lower arms at −38° and uses a 500 mm indexed upper link.
3. **Operating case.** The screened actuator stroke is 178.12 mm. An assumed 400 N horizontal soil force, 200 N vertical soil force and cultivator weight give a maximum calculated demand of 2.01 kN per actuator with symmetric load sharing.
4. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

5. **Display.** Revision 2 adds seven functional layers and a native view. Twelve lower-arm and pivot roles use the labels from their construction record. Solid geometry, positions and definition membership match revision 1.

## Native display layers

1. **Actuator bodies, rods and pivot housings.** `Display-Implement-Actuators` · `#6147A7`.
2. **Bolts, locknuts, washers, shims and spacers.** `Display-Implement-Fasteners` · `#A2A8AF`.
3. **Lift mast and fixed structural supports.** `Display-Implement-Frame` · `#667584`.
4. **Four-eye cassette and mounting face.** `Display-Implement-Interface` · `#C6484D`.
5. **Lower arms, adjustable upper link and stabilizers.** `Display-Implement-Linkage` · `#4F80A6`.
6. **Direct stops and their supporting members.** `Display-Implement-Mechanical-Stops` · `#D89A27`.
7. **Pivot pins, positive locks and retainers.** `Display-Implement-Pins-and-Locks` · `#B99DDD`.

## Technical source

- [ISO 730:2009+A1:2014 Category 1 dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
