package fer.wallezohari.KuhajItAPI.model;



import javax.persistence.*;

@Entity
@Table(name = "Dijeta")
public class Dijeta {

    @Id
    @Column(name = "ImeDijeta")
    private String imedijeta;

    @Column(name = "Opis", length = 2048)
    private String opis;

    @Column(name = "MinEnergija")
    private Double minenergija;

    @Column(name = "MaxEnergija")
    private Double maxenergija;

    @Column(name = "MinMasnoce")
    private Double minmasnoce;

    @Column(name = "MaxMasnoce")
    private Double maxmasnoce;

    @Column(name = "MinZMKiseline")
    private Double minzmkiseline;

    @Column(name = "MaxZMKiseline")
    private Double maxzmkiseline;

    @Column(name = "MinUgljikohidrati")
    private Double minugljikohidrati;

    @Column(name = "MaxUgljikohidrati")
    private Double maxugljikohidrati;

    @Column(name = "MinSeceri")
    private Double minseceri;

    @Column(name = "MaxSeceri")
    private Double maxseceri;

    @Column(name = "MinBjelancevine")
    private Double minbjelancevine;

    @Column(name = "MaxBjelancevine")
    private Double maxbjelancevine;

    @Column(name = "MinSol")
    private Double minsol;

    @Column(name = "MaxSol")
    private Double maxsol;

    @Column(name = "DnevniMaxEnergija")
    private Double dnevnimaxenergija;

    @Column(name = "DnevniMaxMasnoce")
    private Double dnevnimaxmasnoce;

    @Column(name = "DnevniMaxZMKiseline")
    private Double dnevnimaxzmkiseline;

    @Column(name = "DnevniMaxUgljikohidrati")
    private Double dnevnimaxugljikohidrati;

    @Column(name = "DnevniMaxSeceri")
    private Double dnevnimaxseceri;

    @Column(name = "DnevniMaxBjelancevine")
    private Double dnevnimaxbjelancevine;

    @Column(name = "DnevniMaxSol")
    private Double dnevnimaxsol;
    
// Getters and setters
    public String getImedijeta() {
        return imedijeta;
    }

    public void setImedijeta(String imedijeta) {
        this.imedijeta = imedijeta;
    }

    public String getOpis() {
        return opis;
    }

    public void setOpis(String opis) {
        this.opis = opis;
    }

    public Double getMinenergija() {
        return minenergija;
    }

    public void setMinenergija(Double minenergija) {
        this.minenergija = minenergija;
    }

    public Double getMaxenergija() {
        return maxenergija;
    }

    public void setMaxenergija(Double maxenergija) {
        this.maxenergija = maxenergija;
    }

    public Double getMinmasnoce() {
        return minmasnoce;
    }

    public void setMinmasnoce(Double minmasnoce) {
        this.minmasnoce = minmasnoce;
    }

    public Double getMaxmasnoce() {
        return maxmasnoce;
    }

    public void setMaxmasnoce(Double maxmasnoce) {
        this.maxmasnoce = maxmasnoce;
    }

    public Double getMinzmkiseline() {
        return minzmkiseline;
    }

    public void setMinzmkiseline(Double minzmkiseline) {
        this.minzmkiseline = minzmkiseline;
    }

    public Double getMaxzmkiseline() {
        return maxzmkiseline;
    }

    public void setMaxzmkiseline(Double maxzmkiseline) {
        this.maxzmkiseline = maxzmkiseline;
    }

    public Double getMinugljikohidrati() {
        return minugljikohidrati;
    }

    public void setMinugljikohidrati(Double minugljikohidrati) {
        this.minugljikohidrati = minugljikohidrati;
    }

    public Double getMaxugljikohidrati() {
        return maxugljikohidrati;
    }

    public void setMaxugljikohidrati(Double maxugljikohidrati) {
        this.maxugljikohidrati = maxugljikohidrati;
    }

    public Double getMinseceri() {
        return minseceri;
    }

    public void setMinseceri(Double minseceri) {
        this.minseceri = minseceri;
    }

    public Double getMaxseceri() {
        return maxseceri;
    }

    public void setMaxseceri(Double maxseceri) {
        this.maxseceri = maxseceri;
    }

    public Double getMinbjelancevine() {
        return minbjelancevine;
    }

    public void setMinbjelancevine(Double minbjelancevine) {
        this.minbjelancevine = minbjelancevine;
    }

    public Double getMaxbjelancevine() {
        return maxbjelancevine;
    }

    public void setMaxbjelancevine(Double maxbjelancevine) {
        this.maxbjelancevine = maxbjelancevine;
    }

    public Double getMinsol() {
        return minsol;
    }

    public void setMinsol(Double minsol) {
        this.minsol = minsol;
    }

    public Double getMaxsol() {
        return maxsol;
    }

    public void setMaxsol(Double maxsol) {
        this.maxsol = maxsol;
    }

    public Double getDnevnimaxenergija() {
        return dnevnimaxenergija;
    }

    public void setDnevnimaxenergija(Double dnevnimaxenergija) {
        this.dnevnimaxenergija = dnevnimaxenergija;
    }

    public Double getDnevnimaxmasnoce() {
        return dnevnimaxmasnoce;
    }

    public void setDnevnimaxmasnoce(Double dnevnimaxmasnoce) {
        this.dnevnimaxmasnoce = dnevnimaxmasnoce;
    }

    public Double getDnevnimaxzmkiseline() {
        return dnevnimaxzmkiseline;
    }

    public void setDnevnimaxzmkiseline(Double dnevnimaxzmkiseline) {
        this.dnevnimaxzmkiseline = dnevnimaxzmkiseline;
    }

    public Double getDnevnimaxugljikohidrati() {
        return dnevnimaxugljikohidrati;
    }

    public void setDnevnimaxugljikohidrati(Double dnevnimaxugljikohidrati) {
        this.dnevnimaxugljikohidrati = dnevnimaxugljikohidrati;
    }

    public Double getDnevnimaxseceri() {
        return dnevnimaxseceri;
    }

    public void setDnevnimaxseceri(Double dnevnimaxseceri) {
        this.dnevnimaxseceri = dnevnimaxseceri;
    }

    public Double getDnevnimaxbjelancevine() {
        return dnevnimaxbjelancevine;
    }

    public void setDnevnimaxbjelancevine(Double dnevnimaxbjelancevine) {
        this.dnevnimaxbjelancevine = dnevnimaxbjelancevine;
    }

    public Double getDnevnimaxsol() {
        return dnevnimaxsol;
    }

    public void setDnevnimaxsol(Double dnevnimaxsol) {
        this.dnevnimaxsol = dnevnimaxsol;
    }


}