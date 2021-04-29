package ualbanycsi518.NBATrackr.Final.Entities;

import java.util.ArrayList;

import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class OverallTeamStandings {
    String lastUpdatedOn;
    ArrayList<TeamStandingsEntry> teamstandingsentry;
}