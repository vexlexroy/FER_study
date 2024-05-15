Generate SQL

CREATE TABLE KATEGORIJA
(
  nazivKat VARCHAR(100) NOT NULL,
  sifraKat INT NOT NULL,
  PRIMARY KEY (sifraKat)
);

CREATE TABLE INS_UTRKA
(
  datumPoc DATE NOT NULL,
  PRIMARY KEY (datumPoc)
);

CREATE TABLE PLIVAC
(
  sifraPlivac VARCHAR(50) NOT NULL,
  ime VARCHAR(50) NOT NULL,
  prezime INT NOT NULL,
  datumR DATE NOT NULL,
  PRIMARY KEY (sifraPlivac)
);

CREATE TABLE REKREATIVAC
(
  sifraPlivac VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifraPlivac),
  FOREIGN KEY (sifraPlivac) REFERENCES PLIVAC(sifraPlivac)
);

CREATE TABLE SPORTAS
(
  brojBodova INT NOT NULL,
  sifraPlivac VARCHAR(50) NOT NULL,
  PRIMARY KEY (sifraPlivac),
  FOREIGN KEY (sifraPlivac) REFERENCES PLIVAC(sifraPlivac),
  CONSTRAINT chkBodovi CHECK (brojBodova >= 0)
);

CREATE TABLE DRZAVA
(
  ISO CHAR(2) NOT NULL,
  nazivDrz VARCHAR(50) NOT NULL,
  PRIMARY KEY (ISO)
);

CREATE TABLE plivac_inst
(
  vrijeme INT NOT NULL,
  sifraPlivac VARCHAR(50) NOT NULL,
  datumPoc DATE NOT NULL,
  PRIMARY KEY (sifraPlivac, datumPoc),
  FOREIGN KEY (sifraPlivac) REFERENCES PLIVAC(sifraPlivac),
  FOREIGN KEY (datumPoc) REFERENCES INS_UTRKA(datumPoc)
);

CREATE TABLE klub_inst
(
  datumPoc DATE NOT NULL,
  PRIMARY KEY (datumPoc),
  FOREIGN KEY (datumPoc) REFERENCES INS_UTRKA(datumPoc)
);

CREATE TABLE UTRKA
(
  sifraUtrka INT NOT NULL,
  nazivUtrka VARCHAR(100) NOT NULL,
  godinaOsn INT NOT NULL,
  URI VARCHAR(200),
  datumPoc DATE NOT NULL,
  PRIMARY KEY (sifraUtrka, datumPoc),
  FOREIGN KEY (datumPoc) REFERENCES INS_UTRKA(datumPoc),
  UNIQUE (nazivUtrka),
  UNIQUE (URI)
);

CREATE TABLE MJESTO
(
  sifraMjesto INT NOT NULL,
  postOznaka VARCHAR(10),
  nazivMjesto VARCHAR(50) NOT NULL,
  ISO CHAR(2) NOT NULL,
  PRIMARY KEY (sifraMjesto),
  FOREIGN KEY (ISO) REFERENCES DRZAVA(ISO)
);

CREATE TABLE KLUB
(
  nazivKlub VARCHAR(50) NOT NULL,
  sifraKlub INT NOT NULL,
  ISO CHAR(2) NOT NULL,
  PRIMARY KEY (sifraKlub),
  FOREIGN KEY (ISO) REFERENCES DRZAVA(ISO)
);

CREATE TABLE rek_preb
(
  sifraPlivac VARCHAR(50) NOT NULL,
  sifraMjesto INT NOT NULL,
  PRIMARY KEY (sifraPlivac, sifraMjesto),
  FOREIGN KEY (sifraPlivac) REFERENCES REKREATIVAC(sifraPlivac),
  FOREIGN KEY (sifraMjesto) REFERENCES MJESTO(sifraMjesto)
);

