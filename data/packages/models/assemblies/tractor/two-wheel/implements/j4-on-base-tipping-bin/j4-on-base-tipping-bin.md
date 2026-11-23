# J4 on-base tipping bin

1. **CAD file, revision 2.** [DWG 2018](j4-on-base-tipping-bin.dwg). SHA-256 `5aaada02ac7ba1450b605081eee321c2f2f19c0763eec91746912049ea21f3b4`. The saved model shows the closed bin and transport retention.
2. **Mounting.** A rear four-eye cassette and two compression pedestals transfer the rear cradle reaction to the integral tractor bulkhead. Two front cradle pads bear over the closed deck's supported zone. The bin shares the rear cassette port with the tow module and other rear carriers.
3. **Tip mechanism.** Separate hinge pins, two transport locks and two rear support legs keep the cradle and bin identifiable. The geometry uses a proposed 52° tip angle and a removable tailgate.
4. **Design case.** The assumed 25 kg payload gives 101.59 mm actuator travel, 3.75 kN factored actuator demand and 481 N total peak static rear cassette reaction. The calculated tipping cases assume both rear supports are deployed.
5. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).
6. **Display.** Eight functional layers identify all 76 solid occurrences. The solid geometry, placements, labels and block membership match revision 1.

## Native display layers

1. **Tipping actuator body, rod, eyes and clevises.** `Display-Implement-Actuators` · `#6147A7`.
2. **Bin floor, walls and removable tailgate.** `Display-Implement-Bodies` · `#929FB6`.
3. **Longitudinal cradle and crossmembers.** `Display-Implement-Frame` · `#667584`.
4. **Stationary hinge lugs and bin hinge webs.** `Display-Implement-Hinges` · `#4C8070`.
5. **Rear four-eye cassette and compression piers.** `Display-Implement-Interface` · `#C6484D`.
6. **Closed and open stops and mating toes.** `Display-Implement-Mechanical-Stops` · `#D89A27`.
7. **Hinge pins, transport locks and tailgate retention.** `Display-Implement-Pins-and-Locks` · `#B99DDD`.
8. **Front deck shoes and deployable rear supports.** `Display-Implement-Supports` · `#31BDB2`.
