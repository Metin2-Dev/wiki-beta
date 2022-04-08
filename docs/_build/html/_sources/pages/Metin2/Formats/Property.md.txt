# Property
The Property format is a subset format of [Script Format](Script.md)
that hold information about properties of several types, telling
what 3D objects are so a Map knows how to display them



## Header

The header is used to identify the objects, it works as the object metadata
that is used on other files like AreaData

The first line has to be `YPRT`, the second line a CRC32 number and the
rest should be the [Script Format](Script.md) content as below in 
{ref}`Supported Properties <supported-properties>`


| Name  | Description                              | Value     |
|-------|------------------------------------------|-----------|
| Magic | First line in the file - Always the same | YPRT      |
| CRC32 | Second line in the file - Identification | Any CRC32 |


## Fields

| Name         | Description   | Possible Values                |
|--------------|---------------|--------------------------------|
| PropertyName | Property Name | String                         |
| PropertyType | Property Type | String of supported type below |


(supported-properties)=
## Supported Properties

A list of extensions and their respective properties type

| Name         | Extension | Description                            |
|--------------|-----------|----------------------------------------|
| None         | .pr       | Empty Property                         |
| Tree         | .ptr      | Tree object                            |
| Building     | .prb      | Map object                             |
| Effect       | .pte      | Unknown purpose                        |
| Ambience     | .pra      | Unknown purpose                        |
| DungeonBlock | .prd      | Block that represent area of a dungeon |


### Building

| Name         | Description | Possible Values |
|--------------|-------------|-----------------|
| buildingfile |             | String          |
| shadowflag   |             | Boolean Integer |


### Dungeon Block

| Name             | Description | Possible Values |
|------------------|-------------|-----------------|
| dungeonblockfile |             | String          |
