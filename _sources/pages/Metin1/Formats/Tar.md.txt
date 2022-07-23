Tar Format (.tar)
==================

The Tar format is a file format used to compress Metin1 Data files

It starts with 4 bytes specifying the amount of file entries present
and then followed by the file entries


**NOTE:** The file entry data is encrypted with an unknown encryption format/algorithm


## Format Structure (in order)
| Color                                  | Bytes                      | Description              |
|----------------------------------------|----------------------------|--------------------------|
| <span style="color:black">Black</span> | 4                          | Number of file entries   |
| Any                                    | File Entry Structure Below | One or more File Entries |


### File Entry Structure (in order)
| Color                                        | Bytes | Description                                |
|----------------------------------------------|-------|--------------------------------------------|
| <span style="color:green">Green</span>       | 32    | File name (encoded in Windows-949)         |
| <span style="color:blueviolet">Purple</span> | 4     | Offset of the file (relative to the start) |
| <span style="color:royalblue">Blue</span>    | 4     | Size of the files                          |
| <span style="color:grey">Grey</span>         | Any   | Start of a new entry                       |

