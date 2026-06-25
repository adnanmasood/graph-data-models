MATCH (a:Person)-[r:CEO_OF]->(c:Company {id:"acme"}) WHERE date(r.start_date) <= date("2021-06-15") <= date(r.end_date) RETURN a.name;
