CREATE TABLE servers (
    ip int,
    current_players int,
    max_players int,
    version varchar(100),
    players varchar(500),
    PRIMARY KEY (ip)
);
