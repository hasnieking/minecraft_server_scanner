CREATE TABLE IF NOT EXISTS servers (
    id INT NOT NULL AUTO_INCREMENT,
    ip VARCHAR(15),
    current_players INT,
    max_players INT,
    mcversion varchar(128),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS players (
    id INT NOT NULL AUTO_INCREMENT,
    server_id INT,
    playeruuid VARCHAR(36),
    playername VARCHAR(16),
    PRIMARY KEY (id)
);