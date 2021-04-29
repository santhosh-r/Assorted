package ualbanycsi518.NBATrackr.Final.Configuration;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.security.oauth2.resource.PrincipalExtractor;
import org.springframework.security.oauth2.client.OAuth2ClientContext;
import org.springframework.social.facebook.api.Facebook;
import org.springframework.social.facebook.api.impl.FacebookTemplate;
import org.springframework.stereotype.Component;

import ualbanycsi518.NBATrackr.Final.Entities.User;
import ualbanycsi518.NBATrackr.Final.Services.UserService;

@Component
public class FacebookPrincipalExtractor implements PrincipalExtractor {
  @Autowired
  private UserService userService;
  
  @Autowired
  private OAuth2ClientContext oAuth2ClientContext;

  @Override
  public Object extractPrincipal(Map<String, Object> map) {
    String facebookId = (String) map.get("id");
    
    User user = userService.findByFacebookId(facebookId); 
    if (user == null) {
      Facebook facebook = new FacebookTemplate(oAuth2ClientContext.getAccessToken().getValue());
      org.springframework.social.facebook.api.User fbUser = facebook.fetchObject("me", org.springframework.social.facebook.api.User.class, "first_name", "last_name");
      user = userService.createUser(facebookId, fbUser.getFirstName(), fbUser.getLastName());
    }
    userService.loginUser(facebookId);
    return user;
  }
}