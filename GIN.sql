
-- Carga de los datos .csv a posgreSQL
CREATE TABLE tweets (
    id BIGINT PRIMARY KEY,
    "user" TEXT,
    text TEXT,
    processed_text TEXT
);

COPY tweets(id, "user", text, processed_text)
FROM '/var/lib/postgresql/data/tweets.csv' DELIMITER ',' CSV HEADER;

SELECT *
FROM tweets;

-- Modificación de la tabla para rank

ALTER TABLE tweets ADD COLUMN full_text tsvector; 

UPDATE tweets SET full_text = T.full_text
FROM (
    SELECT id, setweight(to_tsvector('english', processed_text), 'A') AS full_text
    FROM tweets
) T
WHERE T.id = tweets.id;

SET enable_seqscan = OFF;

-- Query example "I love my dog"
SELECT id, text, ts_rank_cd(full_text, query) AS rank
FROM tweets, to_tsquery('english', 'I|love|my|dog') query
WHERE query @@ full_text
ORDER BY RANK ASC
LIMIT 100;

-- Index with GIN
CREATE INDEX tweets_search_idx ON tweets USING gin(text gin_trgm_ops);

SELECT id, text, ts_rank(full_text, query) AS rank
FROM tweets, to_tsquery('english', 'I | love | my | dog') query
WHERE query @@ full_text
ORDER BY rank DESC
LIMIT 100;
