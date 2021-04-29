package ualbanycsi518.NBATrackr.Final.Services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import ualbanycsi518.NBATrackr.Final.Entities.User;
import ualbanycsi518.NBATrackr.Final.Repositories.UserRepository;

@Service
public class UserServiceJpaImpl implements UserService {
    @Autowired
    UserRepository userRepository;

    private int currentUserId;
    
    public User getCurrentUser() {
        return userRepository.findById(currentUserId);
    }

    public void saveUser(User user) {
        userRepository.save(user);
    }

    public void loginUser(String facebookId) {
        currentUserId = userRepository.findByFacebookId(facebookId).getId();
    }

    public User createUser(String facebookId, String firstName, String lastName) {
        User user = userRepository.findByFacebookId(facebookId);
        if (user == null) {
            user = new User(facebookId, firstName, lastName);
            userRepository.save(user);
            return userRepository.findByFacebookId(facebookId);
        }
        return user;
    }

    public List<User> findAll() {
        return userRepository.findAll();
    }

    public User findById(int id) {
        return userRepository.findById(id);
    }

    public User findByFacebookId(String facebookId) {
        return userRepository.findByFacebookId(facebookId);
    }

    public void setUserFavorites(int id, int[] favoriteTeams) {
        userRepository.findById(id).setFavoriteTeams(favoriteTeams);
    }

    public int[] getUserFavorites(int id){
        return userRepository.findById(id).getFavoriteTeams();
    }
}