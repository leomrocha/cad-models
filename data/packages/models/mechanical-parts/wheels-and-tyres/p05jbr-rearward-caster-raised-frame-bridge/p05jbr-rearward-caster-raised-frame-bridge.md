THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Rearward caster raised frame bridge

1. **Library number:** 134.
2. **Type:** part.
3. **CAD file:** [p05jbr-rearward-caster-raised-frame-bridge.dwg](<p05jbr-rearward-caster-raised-frame-bridge.dwg>).
4. **DWG SHA-256:** `8fa9ed8cb308c1249b367009b6cc3f7dfa88ad1f18b748d847cbafe202b7de13`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Rearward caster raised frame bridge — P05JBR.

**Design status:** Discussion nominal hollow-section reference.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Rearward caster J4 placement alternative. Quantity: 2 per rearward caster alternative.

### Geometry, datum and interfaces

40×40×3 box tube 135 long X−460…−325; centre Y±150,Z 520; bottom 500/top 540. Front end X−325 contacts rear end of 650 rail; load joint uses explicit external root plates P05JROOT. All arm/cheek/head/pin source-S geometry translates X−240: caster axis−540, primary−460, arm end−335. Arm front end−335 clears cabinet rear−325 by 10. This changes rear support-wheel location and total length; it is a separate placement alternative, not same J3f caste axis−300.

### Source and construction

Parent P05D — Caster frame doubler; current J3f/J4 arrangement. All custom dimensions here are proposed inputs. Cut/turn/form, deburr and inspect stated contact faces, axes and length before assembly.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-20.0, 20.0], [-20.0, 20.0], [0.0, 135.0]] | mm |
| Nominal inner and outer corner radii | PASS | [3.0, 6.0] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
