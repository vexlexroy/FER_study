package fer.wallezohari.KuhajItAPI.model;

import javax.persistence.*;

@Entity
@Table(name = "Slike")
public class Slike {

    @Id
    @Column(name = "IDslika")
    private Integer idslika;

    @Lob
    @Column(name = "Slika")
    private byte[] slika;


// Getters and setters
    public Integer getIdslika() {
        return idslika;
    }

    public void setIdslika(Integer idslika) {
        this.idslika = idslika;
    }

    public byte[] getSlika() {
        return slika;
    }

    public void setSlika(byte[] slika) {
        this.slika = slika;
    }

    
    
}
