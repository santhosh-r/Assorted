package ualbanycsi518.NBATrackr.Final.Entities;

import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class TeamStandingsEntry {
    Team team;
    int rank;
}