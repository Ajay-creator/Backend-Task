-- messages table --
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    num_likes INTEGER DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- likes table --
CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Function to change the number of likes of a mesaage --
CREATE OR REPLACE FUNCTION update_message_likes_count() RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE messages SET num_likes = num_likes + 1 WHERE id = NEW.message_id;
    ELSIF (TG_OP = 'DELETE') THEN
        UPDATE messages SET num_likes = num_likes - 1 WHERE id = OLD.message_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Trigger to update number of likes of a message --
CREATE TRIGGER update_message_likes_count
AFTER INSERT OR DELETE ON likes
FOR EACH ROW
EXECUTE FUNCTION update_message_likes_count();
