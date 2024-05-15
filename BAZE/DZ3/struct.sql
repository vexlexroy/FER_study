CREATE TABLE Vrtic
(
  IdVrtic INT NOT NULL,
  Ulica VARCHAR(20) NOT NULL,
  Broj INT NOT NULL,
  PRIMARY KEY (IdVrtic)
);

CREATE TABLE Roditelj
(
  OIBroditelj CHAR(11) NOT NULL,
  imeRoditelj VARCHAR(20) NOT NULL,
  prezimeRoditelj VARCHAR(20) NOT NULL,
  KontaktBroj CHAR(13) NOT NULL,
  IdVrtic INT,
  PRIMARY KEY (OIBroditelj),
  FOREIGN KEY (IdVrtic) REFERENCES Vrtic(IdVrtic)
);

CREATE TABLE Djelatnik
(
  IdDjelatnik INT NOT NULL,
  OIBradnik CHAR(11) NOT NULL,
  ImeDjelatnik VARCHAR(20) NOT NULL,
  PrezimeDjelatnik VARCHAR(20) NOT NULL,
  OcjenaDjelatnik FLOAT,
  IdVrtic INT NOT NULL,
  PRIMARY KEY (IdDjelatnik),
  FOREIGN KEY (IdVrtic) REFERENCES Vrtic(IdVrtic),
  UNIQUE (OIBradnik)
);

CREATE TABLE Djete
(
  ImeDjete VARCHAR(20) NOT NULL,
  DatumRod DATE NOT NULL,
  OIBroditelj CHAR(11) NOT NULL,
  PRIMARY KEY (OIBroditelj),
  FOREIGN KEY (OIBroditelj) REFERENCES Roditelj(OIBroditelj)
);

CREATE TABLE Igracka
(
  IdIgracka INT NOT NULL,
  ImeIgracka VARCHAR(20) NOT NULL,
  PRIMARY KEY (IdIgracka)
);

CREATE TABLE Se_nalazi
(
  BrojIgracaka INT NOT NULL,
  IdIgracka INT NOT NULL,
  IdVrtic INT NOT NULL,
  PRIMARY KEY (IdIgracka, IdVrtic),
  FOREIGN KEY (IdIgracka) REFERENCES Igracka(IdIgracka),
  FOREIGN KEY (IdVrtic) REFERENCES Vrtic(IdVrtic),
  CONSTRAINT chkBrojIgracaka CHECK (BrojIgracaka BETWEEN 0 AND 100)
);

CREATE TABLE Ima
(
  IdDjelatnik_1 INT NOT NULL,
  ImaIdDjelatnik_2 INT NOT NULL,
  PRIMARY KEY (IdDjelatnik_1, ImaIdDjelatnik_2),
  FOREIGN KEY (IdDjelatnik_1) REFERENCES Djelatnik(IdDjelatnik),
  FOREIGN KEY (ImaIdDjelatnik_2) REFERENCES Djelatnik(IdDjelatnik)
);