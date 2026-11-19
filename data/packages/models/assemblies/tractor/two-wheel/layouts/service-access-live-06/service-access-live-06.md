# Tractor service access joint · recorded assembly build

[Native assembly](<service-access-live-06.dwg>) · Full assembly frame · Playback measurements · Time-stamped native checks

The recording shows OpenCADStudio assembling the [validated tractor service access layout](<../service-access-joint/service-access-joint.md>) from an empty drawing. Left is the native CAD window. Right is the live execution log. The dedicated X11 display was captured continuously at normal speed. The source inventory lists the original native models, their source hashes and each local-to-tractor transform. The tractor model uses millimetres. X points forward, Y left and Z up.


| Time | Operation |
| --- | --- |
| 00:02 | Empty drawing |
| 00:04 | Frame |
| 00:09 | Deck supports |
| 00:13 | Left motor backbone |
| 00:16 | Fixed receiver rails |
| 00:20 | Motor and plate |
| 00:24 | M10 screw and first public washer |
| 00:36 | Sleeve, second washer and nut |
| 00:51 | Removable deck last |
| 00:57 | Deck layer off |
| 01:03 | Deck restored |
| 01:03 | Receiver isolation |
| 01:08 | Eight receiver cups |
| 01:15 | Washers hidden |
| 01:20 | Inboard selection |
| 01:24 | Native save and close |
| 01:28 | Fresh reopen and eleven-placement check |
| 01:37 | Select saved outboard washer |

## What the replay checks

1. Build sequence. The drilled frame, deck supports, motor backbone, fixed rails and motor cartridge are installed before the five-piece M10 joint. Its two nominal washers use the same public definition. The removable deck is installed last. The model has eleven top-level placements on six native role layers. [Original geometry, roles and group membership](<../service-access-joint/service-access-joint.md>).
2. Deck visibility. Switching off the deck changed 5,819 decoded geometry pixels at a fixed camera. Restoring the deck yielded 99 residual changed pixels. The measurement excludes menus and terminal text.
3. Receiver and clamp inspection. Fixed-rail isolation hides the five other role layers, exposing the two receiver rails with their eight receivers. Hiding the internal support layer then isolates the eight cups. Hiding both washers at the clamp changed 12,924 decoded geometry pixels. OCS selected the inboard washer before saving.
4. Persistence. The verified DWG was closed and reopened. The independent entity read recovered each occurrence ID, definition, pose and layer. Selecting the saved outboard washer returned the exact native handle `157`. The two installed washer occurrences share source SHA-256 `81ed4acd73ca058cb84ddbe2b97f39a99f3e6e5840df10fff6d271d3c93c99bb`. OCS closed the saved drawing, reopened it, and closed its owned inspection document after the final selection. The whole DWG has SHA-256 `164a5984391d996d5f48f5dabc20b59a13c189f7cf9f198ef8d705c06149d02c`.

The chapter review inspected 25 decoded frames covering all eleven installation stages, both receiver views, the washer toggle, the two distinct blue selections, and the save, close and reopen sequence. The viewport shows native white wireframe geometry on black.

## Run and inspect

Launch the dedicated editor and scratch qualification, record native operations and check the decoded movie. The launcher expects a freshly named runtime directory, the preserved construction runtime holding the imported washer and verified six-layer empty seed, the skills checkout and the independent public parts checkout. The recording runner rejects occupied output names. Scratch qualification encoded and decoded two states of the native motor layer before the full take. Its fixed-camera comparison found 21,577 changed geometry pixels. It checks the movie using the actual fixed-camera pixels.
