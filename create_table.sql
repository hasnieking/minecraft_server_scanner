CREATE TABLE servers (
    id INT NOT NULL AUTO_INCREMENT,
    ip INT,
    current_players INT,
    max_players INT,
    version varchar(128),
    PRIMARY KEY (id)
);

CREATE TABLE player (
    id INT NOT NULL AUTO_INCREMENT,
    server_id INT,
    playeruuid VARCHAR(36),
    playername VARCHAR(16)
)