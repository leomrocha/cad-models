# J4 20 mm rear bearing hanger assembly

**Catalogue draft ID** `j4-20-bearing-hangers`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](j4-20-bearing-hangers.dwg), SHA-256 `a3241b501e7f0804d07bf0555ef96f03a9e5815ce3bc5964c2d785e22b42fb2b`.

## Geometry

Four retained SKF SY20TF bearing reconstructions on four J4 hanger stations, with separate bearing plates, hollow lower tubes, rear posts, upper links and eight internal compression sleeves.

Millimetres. X along the chassis, Y along the wheel shafts, Z up.

All four inverted bearing datums share Z = 233 mm. The eight compression sleeves occupy the nominal 24 mm interval between the hollow beam walls. The retained SKF reconstruction records a 32 mm crown-width check against the 21 mm source dimension.

## Embedded model revisions

- [SKF SY20TF bearing unit](../../../../../mechanical-parts/bearings/skf-sy20tf-checked/skf-sy20tf-checked.md), 4 instances, SHA-256 `94dd235468e260ba90537fd4dffc664e20f9c64460a25ad7786170c8d991d91c`.
- [Bearing beam compression sleeve](../../../../../mechanical-parts/bearings/p13ct24-bearing-beam-compression-sleeve/p13ct24-bearing-beam-compression-sleeve.md), 8 instances, SHA-256 `3147f6c0e4ebd02d13d1eed7b320b91788463e6dbb04b5a135c9878dc5285cdb`.
- [J4 inverted bearing support plate, 20 mm shaft](../../../../../mechanical/drive/bearing-supports/p13j4pl-j4-inverted-bearing-support-plate/p13j4pl-j4-inverted-bearing-support-plate.md), 4 instances, SHA-256 `115204ad78c7e25c9eaee4348580685a78436dc138355d1ae6c67ac7a2868e71`.
- [J4 hollow lower bearing cantilever, 20 mm shaft](../../../../../mechanical/drive/bearing-supports/p13j4low-j4-lower-bearing-cantilever/p13j4low-j4-lower-bearing-cantilever.md), 4 instances, SHA-256 `7ee467ae479472823dc73a80f11ac46d210cd87b49942dc9861d6972a02b3882`.
- [J4 rear bearing hanger post, 20 mm shaft](../../../../../mechanical/drive/bearing-supports/p13j4post-j4-rear-bearing-hanger-post/p13j4post-j4-rear-bearing-hanger-post.md), 4 instances, SHA-256 `302f6f08e97080fc5da8953f61c8754abf7eba6d407193007d84eec4dff380e0`.
- [J4 upper bearing hanger link](../../../../../mechanical/drive/bearing-supports/p13j4top-j4-upper-bearing-hanger-link/p13j4top-j4-upper-bearing-hanger-link.md), 4 instances, SHA-256 `6dcde35e884d38c3de376f124947791070ef33378eb3b93c57a74df54be3dd56`.

## Checks

OpenCADStudio verified the reference geometry at revision 6794. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](j4-20-bearing-hangers-XY.png)
- [Elevation](j4-20-bearing-hangers-XZ.png)
- [End](j4-20-bearing-hangers-YZ.png)
- [Isometric](j4-20-bearing-hangers-top-isometric.png)
