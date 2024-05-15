CREATE TABLE plivac
(
  imePlivac VARCHAR(50) NOT NULL,
  prezimePlivac VARCHAR(50) NOT NULL,
  sifPlivac INT NOT NULL,
  datRodPlivac DATE NOT NULL,
  PRIMARY KEY (sifPlivac)
);

CREATE TABLE drzava
(
  nazDrzava VARCHAR(50) NOT NULL,
  ISODrzava VARCHAR(2) NOT NULL,
  PRIMARY KEY (nazDrzava),
  UNIQUE (ISODrzava)
);

CREATE TABLE mjesto
(
  sifMjesto INT NOT NULL,
  postOznMjesto INT,
  nazMjesto INT NOT NULL,
  nazDrzava VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifMjesto),
  FOREIGN KEY (nazDrzava) REFERENCES drzava(nazDrzava)
);

CREATE TABLE rekreativac
(
  sifPlivac INT NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifPlivac),
  FOREIGN KEY (sifPlivac) REFERENCES plivac(sifPlivac),
  FOREIGN KEY (sifMjesto) REFERENCES mjesto(sifMjesto)
);

CREATE TABLE klub
(
  sifKlub INT NOT NULL,
  nazKlub VARCHAR(50) NOT NULL,
  nazDrzava VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifKlub),
  FOREIGN KEY (nazDrzava) REFERENCES drzava(nazDrzava),
  UNIQUE (nazKlub)
);

CREATE TABLE Organizira
(
  sifKlub INT NOT NULL,
  PRIMARY KEY (sifKlub),
  FOREIGN KEY (sifKlub) REFERENCES klub(sifKlub)
);

CREATE TABLE sportas
(
  brBodova INT NOT NULL,
  sifPlivac INT NOT NULL,
  sifKlub INT NOT NULL,
  PRIMARY KEY (sifPlivac),
  FOREIGN KEY (sifPlivac) REFERENCES plivac(sifPlivac),
  FOREIGN KEY (sifKlub) REFERENCES klub(sifKlub),
  CHECK chkbodovi (brBodova GREATER OR EQUAL 0)
);

CREATE TABLE plivačkaUtrka
(
  nazUtrka VARCHAR(100) NOT NULL,
  URLUtrka VARCHAR(200),
  datumUtrka DATE NOT NULL,
  udaljenost INT NOT NULL,
  godOsnUtrka INT NOT NULL,
  sifUtrka INT NOT NULL,
  sifKategorija INT NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifUtrka),
  FOREIGN KEY (sifKategorija) REFERENCES kategorija(sifKategorija),
  FOREIGN KEY (sifMjesto) REFERENCES mjesto(sifMjesto),
  UNIQUE (nazUtrka),
  UNIQUE (URLUtrka),
  CHECK chkudaljenost (udaljenost GREATER OR EQUAL 1000)
);

CREATE TABLE kategorija
(
  sifKategorija INT NOT NULL,
  nazKategorija VARCHAR(100) NOT NULL,
  sifNadredenaKategorija INT,
  PRIMARY KEY (sifKategorija),
  FOREIGN KEY (sifNadredenaKategorija) REFERENCES kategorija(sifKategorija),
  UNIQUE (nazKategorija)
);

CREATE TABLE Sudjeluje
(
  vrijemeDolaska INT,
  sifPlivac INT NOT NULL,
  sifUtrka INT NOT NULL,
  PRIMARY KEY (sifPlivac),
  FOREIGN KEY (sifPlivac) REFERENCES plivac(sifPlivac),
  FOREIGN KEY (sifUtrka) REFERENCES plivačkaUtrka(sifUtrka)
);