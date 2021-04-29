package ualbanycsi518.NBATrackr.Final.Entities;

import com.fasterxml.jackson.annotation.JsonProperty;

import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class Team {
	@JsonProperty("ID")
    int ID;
    
	@JsonProperty("City")
	String City;
    
    @JsonProperty("Name")
	String Name;
    
    @JsonProperty("Abbreviation")
	String Abbreviation;
}