MERGE (claim:EmploymentClaim {id:"claim-alice-acme-ceo", confidence:0.93}) MERGE (claim)-[:SOURCE]->(:Document {id:"acme-2020-annual-report"});
