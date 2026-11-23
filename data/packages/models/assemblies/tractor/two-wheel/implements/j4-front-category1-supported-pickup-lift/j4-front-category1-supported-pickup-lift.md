# Front Category 1 supported pickup lift

1. **Native CAD, revision 2.** [DWG 2018](j4-front-category1-supported-pickup-lift.dwg). SHA-256 `0115de8ce11d1be638e36710f581cd8ea3a9ff06776e1d32ad512b1c30e39a26`.
2. **Arrangement.** A four-eye cassette supports two rolling stabilizers, paired lift arms with spherical joints, the adjustable upper link and the actuator envelopes.
3. **Pickup geometry.** Lower ball axes are X = 777.052 mm, Y = ±359 mm and Z = 195 mm. The adjustable upper link is set to 459.695 mm. The nominal actuator eye spacing is 494.670 mm. Dimensions are in the tractor frame with X forward, Y left and Z up.
4. **Service.** Native readback verified four Ø24 mm keeper mouths and the 93 mm cassette pin withdrawal region. A Ø8 mm driver is the checked tool envelope.
5. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

6. **Display.** Revision 2 adds nine functional layers and a native view. The lift geometry, part placements and definition membership match revision 1.

## Native display layers

1. **Lift actuator bodies, rods and eyes.** `Display-Implement-Actuators` · `#6147A7`.
2. **Support wheel axles and axle spacers.** `Display-Implement-Caster-Axles` · `#9B6940`.
3. **Complete caster wheel bodies.** `Display-Implement-Caster-Wheels` · `#30343B`.
4. **Fasteners and retaining nuts.** `Display-Implement-Fasteners` · `#A2A8AF`.
5. **Lift frame, supports for the actuator pivots, and fixed brackets.** `Display-Implement-Frame` · `#667584`.
6. **Four-eye mounting cassette.** `Display-Implement-Interface` · `#C6484D`.
7. **Adjustable top link, lower spherical ends and stabilizer links.** `Display-Implement-Linkage` · `#4F80A6`.
8. **Pivot pins, positive locks and retainers.** `Display-Implement-Pins-and-Locks` · `#B99DDD`.
9. **Rolling support frames, caster seats, swivel bodies and forks.** `Display-Implement-Supports` · `#31BDB2`.

## Technical source

- [ISO 730:2009+A1:2014 Category 1 dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
