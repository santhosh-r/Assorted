package ualbanycsi518.NBATrackr.Final.Services;

import java.util.List;

import ualbanycsi518.NBATrackr.Final.Entities.User;

public interface UserService {
    void loginUser(String facebookId);
    User getCurrentUser();
    void saveUser(User user);
    User createUser(String facebookId, String firstName, String lastName);
    List<User> findAll();
    User findById(int id);
    User findByFacebookId(String facebookId);
    void setUserFavorites(int id, int[] favoriteTeams);
    int[] getUserFavorites(int id);
}