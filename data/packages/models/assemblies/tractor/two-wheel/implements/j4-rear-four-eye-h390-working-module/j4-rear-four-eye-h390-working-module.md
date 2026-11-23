# Four-eye H390 tow module

1. **Native CAD, revision 3.** [DWG 2018](j4-rear-four-eye-h390-working-module.dwg). SHA-256 `b93892e74a73ef639997ca87be40f72e902a75c0bb111a6b7908324353978189`. The existing Ø50 mm SM453 ball remains at its original axis.
2. **Carrier revision.** The carrier tube and both webs move 32 mm inboard. The relieved terminal plate spans X = −1070 to −916 mm in the tractor frame and preserves the native slot centres. The ball shoulder seats on the plate with 10 mm nominal thread projection before the washer.
3. **Coupling-clearance screen.** The finite exterior calculation gives a 2.37 mm lower bound at ±5° pitch, ±25° roll and ±25° yaw with ±12.27 mm axial envelope uncertainty. The screen uses the traced Steelpress housing and a square tongue at its proposed station.
4. **Fastening stack.** The retained ball drawing specifies M22 × 1.5 and the fitting list specifies M20. Select the matched cap nut and washer from the physical tow-ball kit.
5. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

6. **Display.** Revision 3 adds five functional layers and restores the terminal plate name from the construction receipt. The native geometry, positions and definition membership match revision 2.

## Native display layers

1. **Relieved terminal plate and tow-ball seat.** `Display-Implement-Coupler-Seat` · `#4F80A6`.
2. **Carrier tubes, crossmember and receiver uprights.** `Display-Implement-Frame` · `#667584`.
3. **Mounting cassette face and four attachment eyes.** `Display-Implement-Interface` · `#C6484D`.
4. **Terminal drop webs.** `Display-Implement-Reinforcements` · `#31BDB2`.
5. **SM453 tow ball.** `Display-Implement-Tow-Ball` · `#C3CCD6`.

## Technical sources

- [TÜV SÜD SM453 approval report 17-00034-AS-MUC-01, ball drawing](https://www.misterdotcom.de/media/0c/d8/c8/1743087730/Zulassung-komplett-AHK-453-44-mit-EQ.pdf?1743087730=#page=47)
- [TÜV SÜD SM453 approval report, fitting list and trailer conditions](https://www.misterdotcom.de/media/0c/d8/c8/1743087730/Zulassung-komplett-AHK-453-44-mit-EQ.pdf?1743087730=#page=51)
