CREATE TABLE Država
(
  ISOkra CHAR(2) NOT NULL,
  Naziv VARCHAR(50) NOT NULL,
  PRIMARY KEY (ISOkra),
  UNIQUE (Naziv)
);

CREATE TABLE Klub
(
  KluŠifra INT NOT NULL,
  Naziv VARCHAR(50) NOT NULL,
  ISOkra CHAR(2) NOT NULL,
  PRIMARY KEY (KluŠifra),
  FOREIGN KEY (ISOkra) REFERENCES Država(ISOkra),
  UNIQUE (Naziv)
);

CREATE TABLE Mjesto
(
  MjeŠifra INT NOT NULL,
  PostBroj INT,
  Naziv VARCHAR(100) NOT NULL,
  ISOkra CHAR(2) NOT NULL,
  PRIMARY KEY (MjeŠifra),
  FOREIGN KEY (ISOkra) REFERENCES Država(ISOkra),
  UNIQUE (Naziv)
);
CREATE TABLE Kategorija
(
  KatŠifra INT NOT NULL,
  Naziv VARCHAR(100) NOT NULL,
  NadređenaKatŠifra INT,
  PRIMARY KEY (KatŠifra),
  FOREIGN KEY (NadređenaKatŠifra) REFERENCES Kategorija(KatŠifra),
  UNIQUE (Naziv)
);

CREATE TABLE Utrka
(
  UtrŠifra INT NOT NULL,
  Naziv VARCHAR(100) NOT NULL,
  GodOsnutka INT NOT NULL,
  URL VARCHAR(200),
  KatŠifra INT NOT NULL,
  MjeŠifra INT NOT NULL,
  PRIMARY KEY (UtrŠifra),
  FOREIGN KEY (KatŠifra) REFERENCES Kategorija(KatŠifra),
  FOREIGN KEY (MjeŠifra) REFERENCES Mjesto(MjeŠifra),
  UNIQUE (Naziv),
  UNIQUE (URL)
);
CREATE TABLE InstancaUtrke
(
  DatumPoc DATE NOT NULL,
  Udaljenost INT NOT NULL,
  UtrŠifra INT,
  PRIMARY KEY (DatumPoc, UtrŠifra),
  FOREIGN KEY (UtrŠifra) REFERENCES Utrka(UtrŠifra)
);
CREATE TABLE Plivač
(
  PliŠifra INT NOT NULL,
  Ime VARCHAR(50) NOT NULL,
  Prezime VARCHAR(50) NOT NULL,
  DatRođenja DATE NOT NULL,
  DatumPoc DATE,
  UtrŠifra INT,
  PRIMARY KEY (PliŠifra),
  FOREIGN KEY (DatumPoc, UtrŠifra) REFERENCES InstancaUtrke(DatumPoc, UtrŠifra)
);

CREATE TABLE Sportaš
(
  Bodovi INT NOT NULL,
  PliŠifra INT NOT NULL,
  KluŠifra INT NOT NULL,
  PRIMARY KEY (PliŠifra),
  FOREIGN KEY (PliŠifra) REFERENCES Plivač(PliŠifra),
  FOREIGN KEY (KluŠifra) REFERENCES Klub(KluŠifra)
);

CREATE TABLE Rekreativac
(
  PliŠifra INT NOT NULL,
  MjeŠifra INT NOT NULL,
  PRIMARY KEY (PliŠifra),
  FOREIGN KEY (PliŠifra) REFERENCES Plivač(PliŠifra),
  FOREIGN KEY (MjeŠifra) REFERENCES Mjesto(MjeŠifra)
);

CREATE TABLE Organizira
(
  DatumPoc DATE NOT NULL,
  UtrŠifra INT NOT NULL,
  KluŠifra INT NOT NULL,
  PRIMARY KEY (DatumPoc, UtrŠifra, KluŠifra),
  FOREIGN KEY (DatumPoc, UtrŠifra) REFERENCES InstancaUtrke(DatumPoc, UtrŠifra),
  FOREIGN KEY (KluŠifra) REFERENCES Klub(KluŠifra)
);
ALTER TABLE Sportaš ADD CONSTRAINT chkBodovi CHECK (Sportaš.Bodovi >= 0);
ALTER TABLE InstancaUtrke ADD CONSTRAINT chkUdaljenost CHECK (Udaljenost >= 1000);