CREATE TABLE entities(id TEXT PRIMARY KEY, type TEXT, name TEXT);
CREATE TABLE attributes(entity_id TEXT, attr TEXT, value TEXT);
CREATE TABLE links(parent TEXT, child TEXT, rel TEXT);
