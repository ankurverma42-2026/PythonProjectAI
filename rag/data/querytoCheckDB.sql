SELECT
    c.name AS collection_name,
    e.id,
    em.key,
    em.string_value
FROM collections c
JOIN segments s
    ON c.id = s.collection
JOIN embeddings e
    ON s.id = e.segment_id
JOIN embedding_metadata em
    ON e.id = em.id
WHERE c.name = 'car_collection';