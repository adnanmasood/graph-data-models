MATCH (p:Person)-[r:CEO_OF]->(:Company {id:"acme"}) RETURN p.name;
