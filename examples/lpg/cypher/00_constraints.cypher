CREATE CONSTRAINT employment_claim_id IF NOT EXISTS FOR (c:EmploymentClaim) REQUIRE c.id IS UNIQUE;
