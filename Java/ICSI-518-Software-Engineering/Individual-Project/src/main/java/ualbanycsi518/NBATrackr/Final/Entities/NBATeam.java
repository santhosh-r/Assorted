package ualbanycsi518.NBATrackr.Final.Entities;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data // using lombok.Data to take care of getter and setter methods
@Entity
@NoArgsConstructor
public class NBATeam {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private int id;
    private String name;
    private String abbreviation;
    private String logoUrl;

    public NBATeam(String name, String abbreviation, String logoUrl) {
        this.name = name;
        this.abbreviation = abbreviation;
        this.logoUrl = logoUrl;
    }
}