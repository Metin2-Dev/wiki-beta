meta:
  id: chunk_areadata
  title: Chunk Area Data Map Format
  file-extension: adm
  endian: le

seq:
  - id: header
    type: header
  - id: objects
    type: object
    repeat: eos
    
  
types:
  header:
    seq:
      - id: object_count
        type: u2
  object:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: crc32
        type: u4
      - id: pitch
        type: f4
      - id: yaw
        type: f4
      - id: roll
        type: f4
      - id: height
        type: f4
      
    
      