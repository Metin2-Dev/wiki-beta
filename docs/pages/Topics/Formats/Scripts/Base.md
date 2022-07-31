# Script Format

## Summary
The Script format is a text file that uses a declarative way of
telling information, being like a dictionary that can contain
Groups and Lists, considering it the JSON format of Metin2

Comments can be declared by * or // being present in the start of a line


## Group

````
Groups Foo
{
  Value  "val"
  Value2  10
}
````

## List

**Example**:
````
List Foo
{
  10, 20, 30, "bar"
}
````


[//]: # (TODO: refer from their own pages instead of having this list)

## Used In

### Subsets
.msm (Metin2 Script Mesh)
.txt (various text files, see below)
.mss (Metin2 Script Sound)
.prt (Object Property)
.mse (Metin2 Script Effect)
.msf (Metin2 Script ?)
.msa (Metin2 Script animation)
.sub (Subimage)
.msenv (Metin2 Script Environment)


### Files
#### Text files (root/locale)

 - atlasinfo.txt
 - npclist.txt
 - item_list.txt
 - item_scale.txt
 - loading_tip_list.txt
 - grkblk.txt
 - monster_card.txt
 - monster_card_achiev.txt
 - partymatch_info.txt
 - race_height.txt
 - skilltable.txt
 - user_situation.txt
 - locale/map/point txt files
 - locale/shungmahee tower
 - guildbuildinglist.txt
 - itemdesc.txt
 - locale_string.txt
 - locale_quest.txt
 - locale_quiz.txt
 - locale_interface.txt
 - locale_game.txt
 - loading_tip_vnum.txt
 - pet_skill.txt
 - shop_deco.txt
 - skilldesc.txt
 - web_linked_banner.txt
