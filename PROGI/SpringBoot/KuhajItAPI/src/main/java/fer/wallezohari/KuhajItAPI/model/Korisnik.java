package fer.wallezohari.KuhajItAPI.model;


import javax.persistence.*;

@Entity
@Table(name = "Korisnik")
public class Korisnik {

    @Id
    @Column(name = "KorisnickoIme")
    private String korisnickoime;

    @Column(name = "Lozinka", length = 200)
    private String lozinka;

    @Column(name = "Ime", length = 50)
    private String ime;

    @Column(name = "Prezime", length = 50)
    private String prezime;

    @ManyToOne
    @JoinColumn(name = "ImeDijeta")
    private Dijeta imedijeta;

    @Column(name = "RazinaPrivilegije")
    private Integer razinaprivilegije;

// Getters and setters
    public String getKorisnickoime() {
        return korisnickoime;
    }

    public void setKorisnickoime(String korisnickoime) {
        this.korisnickoime = korisnickoime;
    }

    public String getLozinka() {
        return lozinka;
    }

    public void setLozinka(String lozinka) {
        this.lozinka = lozinka;
    }

    public String getIme() {
        return ime;
    }

    public void setIme(String ime) {
        this.ime = ime;
    }

    public String getPrezime() {
        return prezime;
    }

    public void setPrezime(String prezime) {
        this.prezime = prezime;
    }

    public Dijeta getImedijeta() {
        return imedijeta;
    }

    public void setImedijeta(Dijeta imedijeta) {
        this.imedijeta = imedijeta;
    }

    public Integer getRazinaprivilegije() {
        return razinaprivilegije;
    }

    public void setRazinaprivilegije(Integer razinaprivilegije) {
        this.razinaprivilegije = razinaprivilegije;
    }


}