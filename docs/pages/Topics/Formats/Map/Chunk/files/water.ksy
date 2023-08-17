meta:
  id: chunk_water
  title: Chunk Water Map Format
  file-extension: wtr
  endian: le


seq:
  - id: header
    type: header
  - id: heights
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
      - id: enabled
        type: u1
      
    
  coordinate:
    seq:
      - id: height
        type: u4
      
    
  