package ualbanycsi518.NBATrackr.Final.Repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import ualbanycsi518.NBATrackr.Final.Entities.NBATeam;

public interface NBATeamRepository extends JpaRepository<NBATeam, Long> {

    public NBATeam findById(int id);
    
}