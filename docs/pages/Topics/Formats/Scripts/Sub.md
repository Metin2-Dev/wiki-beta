# Sub Format (.sub)

The Sub-image format is a subset format of [Script Format](Base.md) that holds
a location rectangle that tells where an image inside an image is


## Format Structure
| Name    | Description                          | Possible Values                      |
|---------|--------------------------------------|--------------------------------------|
| title   | Tells which type of sub script it is | Must always be the value 'subimage'  |
| version | Version                              | 1.0, 2.0 (check possibilities below) |
| image   | Filename of the base image           | String (including commas)            |
| left    | Subimage X Start Position            | Integer                              |
| top     | SubImage Y Start Position            | Integer                              |
| right   | Subimage X End Position              | Integer                              |
| bottom  | Subimage Y End Position              | Integer                              |


## File Example
*sub-image-example.sub*
````
title subImage
version 1.0
image "image.dds"
left 0
top 0
right 100
bottom 100
````

### Image
image-example.dds (200x200)

![Base image example](../assets/image_example.png)


### Sub-image
result sub-image (100x100)

![Sub-image of base image example](../assets/sub-image_example.png)


## Versions
The version field tells which base path the image should be loaded from

### 1.0
The base directory of the file will be "D:/ymir work/ui"


**Example**

If image field is "sub-image_example.dds", the full path will be
"D:/ymir work/ui/sub-image_example.dds"


### 2.0
The base directory of the file will be the sub-image file directory

**Example**

if the sub file located in "sub/example/" and if 
the image field is "sub-image_example.dds", the full path will be
"sub/example/sub-image_example.dds"

