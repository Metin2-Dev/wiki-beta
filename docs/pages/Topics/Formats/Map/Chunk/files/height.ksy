meta:
  id: chunk_height
  title: Chunk Height Map Format
  file-extension: raw
  endian: le


seq:
  - id: coordinates
    type: coordinate
    repeat: eos

types:    
  coordinate:
    seq:
      - id: height
        type: u2
      
    
  