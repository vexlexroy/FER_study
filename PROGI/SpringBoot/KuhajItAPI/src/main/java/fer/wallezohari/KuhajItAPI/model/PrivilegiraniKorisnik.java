package fer.wallezohari.KuhajItAPI.model;

import javax.persistence.*;

@Entity
@Table(name = "PrivilegiraniKorisnik")
public class PrivilegiraniKorisnik {

    @Id
    @Column(name = "KorisnickoIme")
    private String korisnickoime;

    @Column(name = "Email", length = 200)
    private String email;

    @Column(name = "Biografija", length = 2048)
    private String biografija;

    @ManyToOne
    @JoinColumn(name = "IDslika")
    private Slike idslika;

// Getters and setters
    public String getKorisnickoime() {
        return korisnickoime;
    }

    public void setKorisnickoime(String korisnickoime) {
        this.korisnickoime = korisnickoime;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getBiografija() {
        return biografija;
    }

    public void setBiografija(String biografija) {
        this.biografija = biografija;
    }

    public Slike getIdslika() {
        return idslika;
    }

    public void setIdslika(Slike idslika) {
        this.idslika = idslika;
    }  
}
