meta:
  id: chunk_attributes
  title: Chunk Attributes Map Format
  file-extension: atr
  endian: le


seq:
  - id: header
    type: header
  
  - id: coordinates
    type: coordinate
    repeat: eos

types:
  header:
    seq:
      - id: identifier
        type: u2
      - id: width
        type: u2
      - id: height
        type: u2
    
  coordinate:
    seq:
      - id: walk
        type: b1
      - id: water
        type: b1
      - id: battle
        type: b1
      - id: empty1
        type: b1
      - id: empty2
        type: b1
      - id: empty3
        type: b1
      - id: empty4
        type: b1
      - id: build
        type: b1
      
    
