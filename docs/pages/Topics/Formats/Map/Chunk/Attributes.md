# Attributes

**File Extensions**: .atr
_____

## Description
The chunk attributes format specifies the collision properties of an area
by holding the flags for each X and Y coordinate 

From 0 X and 0 Y to 256 X and 0 Y, following 0 X and 1 Y, 0 X and 2 Y and so on)

### Coordinate
For each coordinate, there is a byte that tells how the collision should be treated
by evaluating its bits

| Bit | Description                                       |
|-----|---------------------------------------------------|
| 1   | 	An entity can walk into that coordinate          |
| 2   | 	The coordinate is filled with water              |
| 3   | 	PVP is disabled in that coordinate               |
| 8   | 	A guild building can be built in that coordinate |


## Composition
You can check the composition of the format and an example file
by [visualizing data formats with Kaitai](https://ide.kaitai.io/) and the kaitai struct below


**Kaitai Struct**: [attributes.ksy](files/attributes.ksy)

**Example file**: [attr.atr](files/map-example/attr.atr)
