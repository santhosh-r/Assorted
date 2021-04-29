package ualbanycsi518.NBATrackr.Final.Configuration;

import org.springframework.boot.autoconfigure.security.oauth2.client.EnableOAuth2Sso;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
//import org.springframework.security.web.csrf.CookieCsrfTokenRepository;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.security.Principal;

@EnableOAuth2Sso
@RestController
public class SecurityConfiguration extends WebSecurityConfigurerAdapter {

	@RequestMapping("/user")
	public Principal user(Principal principal) {
	  return principal;
	}

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http
		.antMatcher("/**")
		.authorizeRequests()
			.antMatchers("/", "/login**", "/webjars/**", "/error**")
			.permitAll()
		.anyRequest()
			.authenticated()
		.and().logout().logoutSuccessUrl("/").permitAll()
		.and().csrf().disable();
		//.and().csrf().csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse());
	}
}