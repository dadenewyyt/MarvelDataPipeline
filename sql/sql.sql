--modified since-----

ALTER TABLE characters ADD COLUMN modified_at TIMESTAMP;
ALTER TABLE comics ADD COLUMN modified_at TIMESTAMP;

-----
CREATE TABLE etl_metadata (last_run TIMESTAMP);
