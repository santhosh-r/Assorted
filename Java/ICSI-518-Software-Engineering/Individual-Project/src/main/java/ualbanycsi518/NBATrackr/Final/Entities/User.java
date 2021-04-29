package ualbanycsi518.NBATrackr.Final.Entities;

import java.util.stream.IntStream;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;

import lombok.Data;

@Data // using lombok.Data to take care of getter and setter methods
@Entity
@SequenceGenerator(name="debug", initialValue=0)
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator="debug")
    private int id;
    @Column(unique=true)
    private String facebookId;
    private String firstName;
    private String lastName;
    private String password;
    private int[] favoriteTeams;
    private boolean admin;
    private boolean blocked;
    
    public User() {
        this.admin = false;
        this.blocked = false;
    }

    public User(String facebookId, String firstName, String lastName) {
        this.facebookId = facebookId;
        this.firstName = firstName;
        this.lastName = lastName;
        this.admin = false;
        this.blocked = false;
    }

    public boolean hasFavorite(int teamId) {
        if (favoriteTeams == null)
            return false;
        return IntStream.of(favoriteTeams).anyMatch(id -> id == teamId);
    }
}