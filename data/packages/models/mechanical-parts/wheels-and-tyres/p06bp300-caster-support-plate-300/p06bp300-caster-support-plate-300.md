THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Blickle 300 caster support plate

1. **Library number:** 145.
2. **Type:** part.
3. **CAD file:** [p06bp300-caster-support-plate-300.dwg](<p06bp300-caster-support-plate-300.dwg>).
4. **DWG SHA-256:** `80dce46277b85dc2e9ed9d50a87b45d350d769d92198042cd285ebd6bea77eb6`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Blickle 300 caster support plate — P06BP300.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 1 per C016 alternative. Assembly/reference family:P06B. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Steel 200 X×160 Y×10, centred X−300,Y 0; underside 355/top 365, axes(±80,±60),4×Ø14. Source plate/grid fromC016; thickness10 proposed. Shift entire arm/pin/cheek groupΔH 50 so arm bottom 365 contacts plate top 365. Taller P05W300 joins same frame doubler. Preserve exact source swivel-axis offset separately.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Blickle 300 caster support plate | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-400.0, -200.0], [-80.0, 80.0], [355.0, 365.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-380.0, -60.0], [-380.0, 60.0], [-220.0, -60.0], [-220.0, 60.0]] | mm |

## Sources — online

1. Blickle G16 catalogue chapter 4.
2. Weldable steel plate stock family — supplier reference.
