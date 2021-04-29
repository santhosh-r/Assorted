package ualbanycsi518.NBATrackr.Final.Entities;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import lombok.Data;
import lombok.ToString;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
@ToString
public class NBATeamStandings {
    OverallTeamStandings overallteamstandings;
}