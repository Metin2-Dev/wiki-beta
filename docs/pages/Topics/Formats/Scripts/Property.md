# Property
The Property format is a subset format of [Script Format](Base.md)
that hold information about properties of several types, telling
what 3D objects are so a Map knows how to display them


## Header

The header is used to identify the objects, it works as the object metadata
that is used on other files like AreaData

The first line has to be `YPRT` for the magic check, the second
line a CRC32 number and the rest should be the [Script Format](Base.md) content as below in 
{ref}`Supported Properties <supported-properties>`

[//]: # (TODO: Add example file header and fields for each type)


| Name  | Description                              | Value     |
|-------|------------------------------------------|-----------|
| Magic | First line in the file - Always the same | YPRT      |
| CRC32 | Second line in the file - Identification | Any CRC32 |


## Script Fields

After the two lines, there is two required fields necessary,
used to tell its name and which type it is

| Name         | Description   | Possible Values          |
|--------------|---------------|--------------------------|
| PropertyName | Property Name | String                   |
| PropertyType | Property Type | String of supported type |

The PropertyType specifies which extension the file **must** have,
each specific type has its own fields


(supported-properties)=
## Supported Properties

List of property types and their extensions

| Name         | Extension | Description          |
|--------------|-----------|----------------------|
| None         | .pr       | No extra fields      |
| Tree         | .ptr      | Tree object          |
| Building     | .prb      | Map object           |
| Effect       | .pte      | Unknown              |
| Ambience     | .pra      | Unknown              |
| DungeonBlock | .prd      | Dungeon Block object |


### Building Fields

| Name         | Description                                    | Possible Values                            |
|--------------|------------------------------------------------|--------------------------------------------|
| buildingfile | GR2 Model Path                                 | String                                     |
| shadowflag   | Model Shadow Flag (presumably, however unused) | Boolean (1 = true, 0 or undefined = false) |


### Dungeon Block Fields

| Name             | Description                        | Possible Values |
|------------------|------------------------------------|-----------------|
| dungeonblockfile | GR2 Model Path (loaded as a block) | String          |
