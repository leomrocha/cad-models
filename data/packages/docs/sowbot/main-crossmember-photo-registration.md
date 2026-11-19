# Main crossmember photo registration

The front, middle and rear transverse members intersect separate camera planes. Each plane couples longitudinal position X with elevation Z in the saved Main chassis frame. With the retained camera and ±4 px pick interval, each compatible line has X = -645.081299 + r(398.327766 − Z), in millimetres, and extends along Y. The dimensionless ratio r depends on the chosen photo line. The tread-reference Z = 0 intersections below are comparative projections. [Photo overlay and position intervals](<../../images/sowbot/main-crossmember-photo-registration.png>).

1. **Front crossmember.** Centre ratio 1.401063–1.476082. At the tread-reference plane, the projected X interval is -86.999 to -57.117 mm. Upper-edge ratio 1.431316–1.507556. Lower-edge ratio 1.358327–1.428839.
2. **Middle crossmember.** Centre ratio 2.176060–2.274436. At the tread-reference plane, the projected X interval is 221.704 to 260.890 mm. Upper-edge ratio 2.234713–2.334956. Lower-edge ratio 2.102396–2.223246.
3. **Rear crossmember.** Centre ratio 3.352040–3.474872. At the tread-reference plane, the projected X interval is 690.129 to 739.057 mm. Upper-edge ratio 3.421709–3.538978. Lower-edge ratio 3.284524–3.382277.

## Source and checks

1. **Photo and frame.** The retained chassis photograph is 436 × 250 px. The conditional camera uses equal 150 mm tread widths based on the Sowbot hardware source. Its transverse vanishing point is (-537.748, -99.889) px. The saved chassis X axis follows travel, Y points across the tracks and Z points up.
2. **Calculation.** Each source segment and the vanishing point define an image direction interval. Back-projection gives the matching planes through the camera. All centre lines reproject within ±4 px at the fixed camera. The picks form part of that camera calibration. The held-out track-direction check remains separate. Visible edge picks · Computed intervals and source hashes.
3. **Placement gate.** The image exposes short lengths of the upper and lower edges. A measured crossmember height or a registered second view is needed to separate each line's X and Z. The attachment spans and mating faces are occluded by the tracks and motors. The D6374 shaft and mounting plane remain available on the motor side. [Motor mounting face](<../../library/images/odrive-d6374-mounting-interface.png>).
4. **Actual calculation model:** unavailable.
