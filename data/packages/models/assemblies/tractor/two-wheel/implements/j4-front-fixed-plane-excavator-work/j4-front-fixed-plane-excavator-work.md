# Four-eye fixed-plane front excavator

Fixed-plane boom, dipper and bucket with a four-eye cassette and two adjustable supports.

1. **CAD file.** [DWG 2018](j4-front-fixed-plane-excavator-work.dwg). SHA-256 `5f111cf80a3916fa67d1efc086ee8701e65c8846a0c72ca02ae7f632d7518b77`.
2. **Geometry and design case.** The excavator uses a 680 mm boom, 730 mm dipper, three actuator envelopes and two 180 × 180 mm deployable pads. Studied cutting-tip positions span 805–2,043 mm forward of the drive axle. The ground support calculation assumes two loaded pads and stationary work.
3. **Jack adjustment.** Two 18 mm across-flats positive drives and split thrust retainers fit the original Ø24 mm jack axes. The checked retracted sliders retain 15 mm nominal clearance below their drive hardware.
4. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

5. **Native display.** Revision 3 preserves all 111 solid occurrences, their geometry and placements. OpenCADStudio read back all ten functional layers, isolated them individually and restored normal visibility.

   - `Display-Implement-Frame` — main cassette support, outriggers and bearing transfer webs, `#667584`.
   - `Display-Implement-Interface` — cassette face and four eyes, `#C6484D`.
   - `Display-Implement-Boom` — two long boom webs, `#426A83`.
   - `Display-Implement-Dipper` — two dipper webs, `#548E91`.
   - `Display-Implement-Bodies` — bucket shell, cheeks and wrist tabs, `#929FB6`.
   - `Display-Implement-Working-Surfaces` — five cutting teeth, `#4F80A6`.
   - `Display-Implement-Supports` — support pads, telescoping jacks and thrust hardware, `#31BDB2`.
   - `Display-Implement-Drive` — actuator and jack-drive geometry, `#B99A50`.
   - `Display-Implement-Pins-and-Locks` — pivot, hinge and actuator pins, `#B99DDD`.
   - `Display-Implement-Fasteners` — eight jack cap screws, `#A2A8AF`.
