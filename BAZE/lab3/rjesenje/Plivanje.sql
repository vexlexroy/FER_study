CREATE TABLE PLIVAC
(
  sifPlivac INT NOT NULL,
  imePlivac VARCHAR(50) NOT NULL,
  prezPlivac VARCHAR(50) NOT NULL,
  datRodj DATE NOT NULL,
  PRIMARY KEY (sifPlivac)
);

CREATE TABLE DRZAVA
(
  ISO CHAR(2) NOT NULL,
  nazDrzava VARCHAR(50) NOT NULL,
  PRIMARY KEY (ISO),
  UNIQUE (nazDrzava)
);

CREATE TABLE MJESTO
(
  sifMjesto INT NOT NULL,
  postOznaka VARCHAR(10),
  nazMjesto VARCHAR(100) NOT NULL,
  ISO CHAR(2) NOT NULL,
  PRIMARY KEY (sifMjesto),
  FOREIGN KEY (ISO) REFERENCES DRZAVA(ISO)
);

CREATE TABLE KLUB
(
  sifKlub INT NOT NULL,
  nazKlub VARCHAR(50) NOT NULL, 
  ISO CHAR(2) NOT NULL,
  PRIMARY KEY (sifKlub),
  FOREIGN KEY (ISO) REFERENCES DRZAVA(ISO),
  UNIQUE (nazKlub)
);

CREATE TABLE REKREATIVAC
(
  sifPlivac INT NOT NULL,
  sifMjesto INT NOT NULL,
  PRIMARY KEY (sifPlivac),
  FOREIGN KEY (sifPlivac) REFERENCES PLIVAC(sifPlivac),
  FOREIGN KEY (sifMjesto) REFERENCES MJESTO(sifMjesto)
);

CREATE TABLE SPORTAS
(
  brojBodova INT NOT NULL,
  sifPlivac INT NOT NULL,
  sifKlub INT NOT NULL,
  PRIMARY KEY (sifPlivac),
  FOREIGN KEY (sifPlivac) REFERENCES PLIVAC(sifPlivac),
  FOREIGN KEY (sifKlub) REFERENCES KLUB(sifKlub),
  CONSTRAINT chkBodovi CHECK (brojBodova >= 0)
);

CREATE TABLE UTRKA
(
  sifUtrka INT NOT NULL,
  nazUtrka VARCHAR(100) NOT NULL,
  godinaOsnutka INT NOT NULL,
  URIUtrka VARCHAR(200),
  sifKateg INT NOT NULL,
  PRIMARY KEY (sifUtrka),
  FOREIGN KEY (sifKateg) REFERENCES KATEGORIJA(sifKateg),
  UNIQUE (URIUtrka)
);

CREATE TABLE KATEGORIJA
(
  sifKateg INT NOT NULL,  
  nazKateg VARCHAR(100) NOT NULL,
  jeNadKateg_sifKateg INT,
  PRIMARY KEY (sifKateg),
  FOREIGN KEY (jeNadKateg_sifKateg) REFERENCES KATEGORIJA(sifKateg),
  UNIQUE (nazKateg)
);

CREATE TABLE INST_UTRKE
(
  datPocetak DATE NOT NULL,
  udaljenost INT NOT NULL,
  sifUtrka INT NOT NULL,
  PRIMARY KEY (datPocetak, sifUtrka),
  FOREIGN KEY (sifUtrka) REFERENCES UTRKA(sifUtrka),
  CONSTRAINT chkUdaljenost CHECK (udaljenost >= 1000)
);

CREATE TABLE pliva
(
  vrijeme INT NOT NULL,
  sifPlivac INT NOT NULL,
  datPocetak DATE NOT NULL,
  sifUtrka INT NOT NULL,
  PRIMARY KEY (sifPlivac, datPocetak, sifUtrka),
  FOREIGN KEY (sifPlivac) REFERENCES PLIVAC(sifPlivac),
  FOREIGN KEY (datPocetak, sifUtrka) REFERENCES INST_UTRKE(datPocetak, sifUtrka)
);

CREATE TABLE organizira
(
  sifKlub INT NOT NULL,
  datPocetak DATE NOT NULL,
  sifUtrka INT NOT NULL,
  PRIMARY KEY (sifKlub, datPocetak, sifUtrka),
  FOREIGN KEY (sifKlub) REFERENCES KLUB(sifKlub),
  FOREIGN KEY (datPocetak, sifUtrka) REFERENCES INST_UTRKE(datPocetak, sifUtrka)
);
