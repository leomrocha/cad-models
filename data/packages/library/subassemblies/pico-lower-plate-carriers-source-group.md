# Pico lower formed plate and side carriers

1. **Library number:** 298.
2. **Plan use:** Assembly 2, step 2, models 09–11.
3. **Native drawing:** [Pico lower formed plate and side carriers](<pico-lower-plate-carriers-source-group.dwg>).
4. **DWG SHA-256:** `1e15a8ab85127e198b188e745bb435b3cfad92dc85f54f6128d550535be9b654`. DWG 2018, 239,829 bytes.
5. **State:** SAVED_CURRENT_SOURCE_GEOMETRY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Geometry:** One block reference contains three Solid3D occurrences. The lower formed plate is source body 3108. The left and right side carriers are source bodies 3234 and 3368.
2. **Frame:** Manufacturer STEP XYZ in millimetres. The group placement is the identity matrix. The plate and both handed carriers retain their installed source coordinates.
3. **Source and geometry checks:** The STEP subset retains the selected geometry records byte for byte. Each placed body matches its source vertex set with recorded bidirectional error of 0 mm. All face counts match, with 215 on the lower plate and 175 on each carrier. Each body has reciprocal closed coedge topology. These checks use the current ACIS700 SAT records.
4. **Persistence and closure:** Completed SAVE, expected path, byte size, SHA-256, audit and zero dropped entities PASS. Persistence verification uses SAVE only. Guarded closure of owned construction document 7 PASS. Start document 1 was preserved.
5. **Views:** The four views represent all three placed solids. They use 1,665 recorded edges, including 224 trim edges shown by their endpoints. XY, XZ, YZ and isometric pixels were inspected.
6. **Lower plate and carrier attachment check:** The installed source bodies have conservative transverse gaps of **8.065 mm** to the left carrier and **8.180 mm** to the right carrier. Faces 14388 and 14389 on the 2 mm lower formed plate have 77 paired inner opening profiles by projected source endpoints. Both carrier bore axes are transverse. These three bodies form a separated lower plate and carrier arrangement in the manufacturer STEP. Actual checking model unavailable.

## References

1. [Lower formed plate, library 266](<../parts/mechanical/pico-lower-plate-manufacturer-source.md>).
2. [Left side carrier, library 267](<../parts/mechanical/pico-left-side-frame-manufacturer-source.md>).
3. [Right side carrier, library 268](<../parts/mechanical/pico-right-side-frame-manufacturer-source.md>).
4. [XY view](<../images/pico-lower-plate-carriers-source-group-XY.png>).
5. [XZ view](<../images/pico-lower-plate-carriers-source-group-XZ.png>).
6. [YZ view](<../images/pico-lower-plate-carriers-source-group-YZ.png>).
7. [Isometric view](<../images/pico-lower-plate-carriers-source-group-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Original STEP SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
