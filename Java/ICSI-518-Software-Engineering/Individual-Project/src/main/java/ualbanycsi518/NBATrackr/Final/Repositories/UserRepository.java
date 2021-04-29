package ualbanycsi518.NBATrackr.Final.Repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import ualbanycsi518.NBATrackr.Final.Entities.User;

public interface UserRepository extends JpaRepository<User, Integer> {
    public User findById(int id);
	public User findByFacebookId(String facebookId);
}