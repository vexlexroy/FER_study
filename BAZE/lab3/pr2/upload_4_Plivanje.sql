CREATE TABLE Drzava
(
  ISO_kratica CHAR(2) NOT NULL,
  NazivDrzave VARCHAR(50) NOT NULL,
  PRIMARY KEY (ISO_kratica),
  UNIQUE (NazivDrzave)
);

CREATE TABLE Mjesto
(
  sifraMjesto INT NOT NULL,
  pbr VARCHAR(100),
  nazivMjesto VARCHAR(100) NOT NULL,
  ISO_kratica CHAR(2) NOT NULL,
  PRIMARY KEY (sifraMjesto),
  FOREIGN KEY (ISO_kratica) REFERENCES Drzava(ISO_kratica)
);

CREATE TABLE Utrka
(
  sifraUtrke INT NOT NULL,
  nazivUtrke VARCHAR(100) NOT NULL,
  godOsnutka DATE NOT NULL,
  URL_utrke VARCHAR(200),
  sifraKat INT NOT NULL,
  sifraMjesto INT NOT NULL,
  PRIMARY KEY (sifraUtrke),
  FOREIGN KEY (sifraKat) REFERENCES Kategorija(sifraKat),
  FOREIGN KEY (sifraMjesto) REFERENCES Mjesto(sifraMjesto),
  UNIQUE (nazivUtrke),
  UNIQUE (URL_utrke)
);

CREATE TABLE Kategorija
(
  sifraKat INT NOT NULL,
  nazivKat VARCHAR(100) NOT NULL,
  nadređenaKat_sifraKat INT,
  PRIMARY KEY (sifraKat),
  FOREIGN KEY (nadređenaKat_sifraKat) REFERENCES Kategorija(sifraKat),
  UNIQUE (nazivKat)
);

CREATE TABLE Plivac
(
  sifraPlivaca INT NOT NULL,
  ime VARCHAR(50) NOT NULL,
  prezime VARCHAR(50) NOT NULL,
  datRod DATE NOT NULL,
  sifraUtrke INT NOT NULL,
  PRIMARY KEY (sifraPlivaca),
  FOREIGN KEY (sifraUtrke) REFERENCES OdrzavanjaUtrke(sifraUtrke)
);

CREATE TABLE OdrzavanjaUtrke
(
  sifraUtrke INT NOT NULL,
  datPocetkaUtrke DATE NOT NULL,
  Udaljenost INT NOT NULL,
  sifraUtrke INT NOT NULL,
  CONSTRAINT chkUdaljenost CHECK (Udaljenost >=1000),
  PRIMARY KEY (sifraUtrke),
  FOREIGN KEY (sifraUtrke) REFERENCES Utrka(sifraUtrke)
);

CREATE TABLE Klub
(
  sifraKlub INT NOT NULL,
  nazivKlub VARCHAR(50) NOT NULL,
  ISO_kratica CHAR(2) NOT NULL,
  sifraUtrke INT NOT NULL,
  PRIMARY KEY (sifraKlub),
  FOREIGN KEY (ISO_kratica) REFERENCES Drzava(ISO_kratica),
  FOREIGN KEY (sifraUtrke) REFERENCES OdrzavanjaUtrke(sifraUtrke),
  UNIQUE (nazivKlub)
);

CREATE TABLE Rekreativac
(
  sifraPlivaca INT NOT NULL,
  sifraMjesto INT NOT NULL,
  PRIMARY KEY (sifraPlivaca),
  FOREIGN KEY (sifraPlivaca) REFERENCES Plivac(sifraPlivaca),
  FOREIGN KEY (sifraMjesto) REFERENCES Mjesto(sifraMjesto)
);

CREATE TABLE Sportas
(
  BrBodova INT NOT NULL,
  sifraPlivaca INT NOT NULL,
  sifraKlub INT NOT NULL,
  CONSTRAINT chkBodovi CHECK (BrBodova>0),
  PRIMARY KEY (sifraPlivaca),
  FOREIGN KEY (sifraPlivaca) REFERENCES Plivac(sifraPlivaca),
  FOREIGN KEY (sifraKlub) REFERENCES Klub(sifraKlub)
);